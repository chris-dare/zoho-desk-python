# Serenity Customer Support Service

Todo: Add build status

## About
Microservice bridging Serenity's support desk on Zoho with our decentralized apps.


## Setup
Packages are installed and managed by [poetry](https://python-poetry.org/). 
To install poetry (linux/OSX) run the following command:
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
Detailed setup instructions for poetry are available [here](https://python-poetry.org/docs/)

Dependencies for the project are available at `./pyproject.toml`. 
Install dependencies with:
```bash
poetry install
```

The package structure is yet to be finalized. Check back in a week or contact [Chris Dare](mailto:chris@clearspacelabs.com?subject=Enquiry%3A%20Serenity%20support%20service) 
to learn more.

## Launching: Running the service
Run the bash script `startup.sh`
```bash
bash startup.sh
```
This service runs on host port 80. If you'd like to change the port, bind a different port to the 
docker app in `./docker-compose.yml`