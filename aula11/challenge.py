# Challenge Session 11: GraphQL API with Nested Queries and Authenticated Mutations
# Problem: Implement a GraphQL API that supports nested queries and authenticated mutations.
# Hint: Integrate an authentication check in the resolver.

import strawberry
from fastapi import FastAPI, Depends, HTTPException
from strawberry.fastapi import GraphQLRouter

# Simulação de autenticação simples
def get_current_user(token: str = ""):
    if token != "valid-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return "authenticated_user"

@strawberry.type
class Profile:
    bio: str

@strawberry.type
class User:
    id: int
    name: str
    profile: Profile

users_db = [
    User(id=1, name="Alice", profile=Profile(bio="Bio Alice")),
    User(id=2, name="Bob", profile=Profile(bio="Bio Bob")),
]

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User:
        for user in users_db:
            if user.id == id:
                return user
        return None

@strawberry.type
class Mutation:
    @strawberry.mutation
    def update_bio(self, info, id: int, bio: str, token: str = "") -> Profile:
        get_current_user(token)
        for user in users_db:
            if user.id == id:
                user.profile.bio = bio
                return user.profile
        raise HTTPException(status_code=404, detail="User not found")

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

