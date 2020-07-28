# Find My Market API

Welcome to Find My Market! This repo is the backend that our app uses to store it's users and their favorites.

## Technology & Framework

The API for Find My Market was built in python using the [FastAPI](https://pypi.org/project/fastapi/) framework. Find My Market is hosted on Heroku, and we used TravisCI for contiunous integration. You can view the swagger docs of this API's endpoints [here](https://find-my-market-api.herokuapp.com/docs).

## Why FastAPI?

FastAPI is a newer python framework that offers high performance, is easy to learn, and shortens the process from development to production. We only had two weeks to complete this so a framework with an easier learning curve was a great choice for us. Another awesome feature of FastAPI is that it generates swagger [docs](https://find-my-market-api.herokuapp.com/docs) for your endpoints automatically. 

![docs](https://user-images.githubusercontent.com/58053916/88704900-02606900-d0cc-11ea-9041-fb83ef12599e.png)

Here you can see a sample of the endpoints on this API. It also generates previews of your schemas defined in your code.

## Documentation for API Endpoints

Type | HTTP request | Description
------------- | ----------------- | -------------
**users** | **GET** /users/ | Get all users
**users** | **POST** /users/ | Create a new user
**users**| **GET** /users/{user_id} | Get single user by ID
**users** | **POST** /users/{user_id}/favorites | Add a favorite to the user, request must include a fmid identifier for the market
**users** | **GET** /users/{user_id}/favorites | Get all favorites from one user
**markets** | **GET** /markets/ | Get all markets

## Schema Design

We went with a very simple design for this API. We pulled most of the farmers market data used in the app from a separate API we built out, which allowed us to keep this API lightweight and keep our tables simple.

![schema](https://user-images.githubusercontent.com/58053916/88712085-66882a80-d0d6-11ea-946a-db632eb2525f.png)

**Note:** The fmid column shown on markets here is pulled from an external api. You can view those docs [here](https://github.com/tylerpporter/us_farmers_market_api).

## Running Locally

To run this api you need to have python installed on your local machine. [MacOS](https://docs.python-guide.org/starting/install3/osx/) [Windows](https://docs.python.org/3/using/windows.html)

Fork and clone.

CD into the local directory and run `source ./env/bin/activate` to start up a local python environment.

Run `pip install fastapi` and `pip install uvicorn` to install fastapi

Run `pip install -r requirements.txt` and `pip install -r dev-requirements.txt` to install the API dependencies.

This API uses a postgresql database so you'll need to create two: `market_api` and `market_api_test`.

Next run `alembic upgrade head` to run all the migrations. **Note:** You may need to set your `PYTHONPATH` variable if you get the error `module app not found`. This can be done by running the command `export PYTHONPATH="$PYTHONPATH:/path/to/where/the/folder/is/located"` and then you can run `alembic upgrade head`.

The API should be set up now and you can our test suite by using the command `bash test.sh`

**Note on Environment Variables:** If you'd like to change environmental varaibles, they are defined in config.py using a Pydantic Settings object.

![DevelopmentTeam](assets/images/team_index.png)
