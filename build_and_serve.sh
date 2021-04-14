# if permission denied try chmod -R 777 ./build_and_serve.sh

# move to fastpy
cd fastpy

# export currently used libraries
poetry export -f requirements.txt --output requirements.txt --without-hashes

# build and serve
docker-compose up -d --build

# find the app at http://localhost:8004/ping