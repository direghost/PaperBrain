import pinecone
import os


pinecone.init(api_key=os.environ.get("PINECONE_API_KEY"), environment="us-west1-gcp")

quickstart = "quickstart"
pinecone.create_index(str(quickstart), dimension=1536, metric="euclidean", pod_type="p1")