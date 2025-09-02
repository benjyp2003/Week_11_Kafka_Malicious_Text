docker stop tweets-preprocessor-container 2>nul
docker rm tweets-preprocessor-container 2>nul

docker login
docker build -t benjyfeffer/tweets-preprocessor:latest .
docker push benjyfeffer/tweets-preprocessor:latest
docker run -d --name tweets-preprocessor-container benjyfeffer/tweets-preprocessor:latest

