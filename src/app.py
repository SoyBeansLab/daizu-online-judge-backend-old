from logging import getLogger, StreamHandler, DEBUG, Formatter
from os import environ

from fastapi import FastAPI
import uvicorn

from infrastructure.waf.fastapi.router import set_route
from exceptions.waf import APIError, api_error_handler

from docs.openapi_conf import (
    TITLE,
    DESCRIPTION,
    VERSION,
    tags_metadata,
)


## Configuration Logger
logger = getLogger("daizu")
formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger.setLevel(DEBUG)
logger.propagate = False

if environ.get("DAIZU_LOG_STREAM", "") == "1":
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

if environ.get("DAIZU_LOG_FILE", "") == "1":
    fh = FileHandler(filename="daizu_online_judge.log")
    fh.setLevel(DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)


def main():
    api = FastAPI(
        title=TITLE,
        version=VERSION,
        description=DESCRIPTION,
        openapi_tags=tags_metadata,
    )
    set_route(api)
    api.add_exception_handler(APIError, api_error_handler)

    uvicorn.run(app=api)


if __name__ == "__main__":
    main()
