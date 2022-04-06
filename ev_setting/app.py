from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from .settings import SWAGGER_URL, REDOC_URL, APP_NAME
from fastapi.middleware.cors import CORSMiddleware

# CODE BELOW



tags_metadata = [
    {
        "name": 'EV',
        "description": ""
    }
]

app = FastAPI(openapi_tags=tags_metadata, redoc_url=REDOC_URL, docs_url=SWAGGER_URL)



origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=APP_NAME,
        version="1.0.0",
        description="This micro service is based on python 3+ langugage with fastapi rest framework used to build\
         we are Managing",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": ""
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi