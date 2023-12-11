# Hugging Face Text Generation Flask Application  

[![CI/CD Pipeline](https://github.com/nogibjj/mjh140_individual4/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/mjh140_individual4/actions/workflows/cicd.yml)

## Summary

The objective of this repository is to build a publicly available auto-scaling web application using Flask. The application is containerized into a Docker image and pushed to DockerHub for container storage. The container is then deployed to a public endpoint using Azure Web App.

For this project, I am deploying a Hugging Face Text Generation LLM in a simple application that returns five recommeded books when provided a list of the user's favorite authors.

Here is a video walkthrough of the project: [Hugging Face Text Generation Flask Application](https://youtu.be/O8N_M_vYYnA)

## Web Application

Below are screenshots from the web application using an example city of `San Francisco`.

![image](https://github.com/nogibjj/mjh140_individual4/assets/114833075/3a16f9ee-5806-4ae6-9112-2d55b141e104)

![image](https://github.com/nogibjj/mjh140_individual4/assets/114833075/6c30e6f9-bd20-4075-9f0e-11dbc8c312c4)

## Docker

The flask application is containerized using a [Docker File]. The docker container is stored in DockerHub. 

![image](https://github.com/nogibjj/mjh140_individual4/assets/114833075/377354e5-27dd-4d3b-b749-064ad056bbf0)

## Azure Deployment

Unfortunately I have used up all my university sponsored Azure money :( Not to worry though, the screenshots below walk through the process of deploying the docker container through Azure Web App Service.

Two critical parts to deploying the container:

1. Ensure the latest version of the container is called from your web app. This means adding the `:latest` tag to the end of your docker container name
   `matthewholden86/myimage2:latest`
2. Ensure the port used in your public endpoint is the same port defined in your flask application. i.e. port 5000

![image](https://github.com/nogibjj/mjh140_individual4/assets/114833075/5b95e301-b519-49fe-9b9c-3afeccb7c383)

![image](https://github.com/nogibjj/mjh140_individual4/assets/114833075/c5eaab93-bb89-4754-af34-274b63b75d9d)

![image](https://github.com/nogibjj/mjh140_individual4/assets/114833075/fc67b1d9-f60d-4fb5-8006-069d9949f89b)

