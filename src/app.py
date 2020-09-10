from logging import getLogger, StreamHandler, DEBUG, Formatter
from os import environ

from fastapi import FastAPI
import uvicorn

from infrastructure.waf.fastapi.router import set_route


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
    title = "Daizu Online Judge API"
    description = "daizu online judge developping is contest site of the competitive programming"
    version = "0.1.0"

    api = FastAPI(title=title, version=version, description=description,)
    set_route(api)
    uvicorn.run(app=api)


if __name__ == "__main__":
    main()
