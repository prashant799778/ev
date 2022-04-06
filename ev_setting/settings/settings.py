from urllib.parse import quote
import os
# CODE BELOW



# Project Settings
APP_NAME = 'ev-address'

HOST_ADDRESS = os.getenv("HOST_ADDRESS", "127.0.0.1")
# Project Documentation URL

SWAGGER_URL = "/swagger-ui.html/"
REDOC_URL = "/docs/"
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")

# if ENVIRONMENT not in ["dev", "prod", "qa","demo"]:
#     raise TypeError(f"Incorrect {ENVIRONMENT} name, should be dev,demo,prod or qa")

