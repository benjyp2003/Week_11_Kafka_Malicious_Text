docker stop tweets-retriever-container 2>nul
docker rm tweets-retriever-container 2>nul

docker login
docker build -t benjyfeffer/tweets-retriever:latest .
docker push benjyfeffer/tweets-retriever:latest
docker run -d --name tweets-retriever-container benjyfeffer/tweets-retriever:latest

docker logs -f tweets-retriever-container