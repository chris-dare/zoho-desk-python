# Serenity Customer Support Service

[![Build Status](https://travis-ci.com/dexios1/serenity-service-desk.svg?branch=development)](https://travis-ci.com/dexios1/serenity)

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
### Running locally
Make sure you have [docker installed](https://docs.docker.com/get-docker/)
Run the bash script `startup.sh` if on linux:
```bash
$ bash startup.sh
```
Or use docker directly:
```console
docker-compose build
docker-compose up -d
```

This service runs on host port 80. If you'd like to change the port, 
bind a different port to the docker app in `./docker-compose.yml`

### Development
A development instance of this server is currently available on AWS at the time of this writing.

Link: http://serenity-customer-support-dev.us-east-1.elasticbeanstalk.com/


If you need to deploy a new development instance, consider using heroku or AWS. 
Here are instructions to deploy to EB2:
```console
eb init
eb create
eb setenv env_key=env_value env_key2=env_value2 and=so_on
eb deploy
```
Refer to `./env.sample` for a list of all required environment variables
