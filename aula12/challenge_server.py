# Challenge Session 12: gRPC Server-Side Streaming Example
# Problem: Create a gRPC service that supports server-side streaming to send multiple messages for a single request.
# Hint: Modify the .proto definition to use a stream for the response.

import grpc
from concurrent import futures
import time

import challenge_pb2
import challenge_pb2_grpc

class StreamerServicer(challenge_pb2_grpc.StreamerServicer):
    def StreamNumbers(self, request, context):
        for i in range(1, request.count + 1):
            yield challenge_pb2.StreamReply(number=i)
            time.sleep(0.5)  # Simulate delay

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    challenge_pb2_grpc.add_StreamerServicer_to_server(StreamerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
