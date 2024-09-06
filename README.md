
# Python Face validation

Face validation micro service for WanderLK application




## Installation

setup with docker 

```bash
  docker build -t my-python-face-app .
  docker run -p 8082:8082 --name my-python-face-app-container  my-python-face-app
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`=

`EMAIL`=

`PASSWORD`=


## Running the app

```bash
fastapi dev server.py
```
