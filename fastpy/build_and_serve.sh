# export currently used libraries
poetry export -f requirements.txt --output requirements.txt --without-hashes

# build
docker-compose build

# serve
docker-compose up -d

# find the app at http://localhost:8004/ping