docker stop conch
docker rm conch
docker build -t magicconch:latest .
docker run -d --restart=always -e TOKEN='Yourfavoriteprivatetoken' --name conch magicconch:latest