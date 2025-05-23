# Challenge Session 9: Django REST API Test Suite with pytest
# Problem: Develop a full test suite for a Django REST API endpoint (e.g., listing BlogPosts) using pytest fixtures and parametrization.
# Hint: Create fixtures for BlogPost objects and test the API response structure.


import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from myapp.models import BlogPost

@pytest.fixture
def create_blogposts(db):
    BlogPost.objects.create(title="Post 1", content="Content 1")
    BlogPost.objects.create(title="Post 2", content="Content 2")

@pytest.mark.django_db
def test_blogpost_list_api(create_blogposts):
    client = APIClient()
    url = reverse('blogpost-list')  # Ajuste para o nome correto do endpoint
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    titles = [item['title'] for item in data]
    assert "Post 1" in titles and "Post 2" in titles

@pytest.mark.parametrize("title", ["Post 1", "Post 2"])
@pytest.mark.django_db
def test_blogpost_titles(create_blogposts, title):
    client = APIClient()
    url = reverse('blogpost-list')
    response = client.get(url)
    data = response.json()
    titles = [item['title'] for item in data]
    assert title in titles

