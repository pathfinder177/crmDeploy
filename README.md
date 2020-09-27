Requirements:
    - OS: 
        - x86_64 arch
        - can install rpm packets
        - access to dockerhub 

Here is a very deployment project consists of the two stages:

1) Installing all dependencies with ansible
2) Checking two services with simple gitlab pipeline this way: \
SCAN: Pulling two Bitnami images and scan it with Trivy
DEPLOY: Running the images with docker-compose
TEST: Testing the main page of CRM's container return 200 with PyTest
