# Detector
This sofware detects robotic mowers on lawn and save its coordinates to a postgresql database.
## Architecture
## Local setup
1. Install docker
2. Run this command in terminal:
   ```
   docker run --name postgresql -e POSTGRES_USER=dbuser -e POSTGRES_PASSWORD=nadiJd24hSd3hs -e POSTGRES_DB=detector -p 5432:5432 -v /data:/var/lib/postgresql/data -d postgres
   ```