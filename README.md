# mini_RAG_Application
Minimal Implementation of RAG Model for Question Answering.

## Requirements
- Python version 3.11 or later.
### Install python using Miniconda:
#### (Optional) for better readability in command line (to start writing commands from the next line use the following command) :
```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

1) Download and install Miniconda form [here](https://www.anaconda.com/docs/getting-started/miniconda/install).
2) Create new environment using the following command:
```bash
$ conda create -n miniRAG python=3.11
```
3) Activate the new environment using the following command:
```bash
$ conda activate miniRAG
```

## Installation
### Install the required packages using the following command:
```bash
$ pip install -r requirements.txt
```
### Setup the environment variables
```bash
$ cp .env.example .env
```
Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run the FastAPI server using the following command:
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
## POSTMAN collection
Download the POSTMAN collection from [/assets/mini_RAG_App.postman_collection.json](/assets/mini_RAG_App.postman_collection.json)