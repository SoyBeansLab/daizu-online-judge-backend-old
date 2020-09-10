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

## Configuration Documents
tags_metadata = [
    {"name": "contests", "description": "Operations the Contest.",},
    {"name": "problems", "description": "Operations the Problem.",},
    {"name": "submissions", "description": "Operations the Submission.",},
    {
        "name": "registrations",
        "description": "Operations the Registrations. Register for the contest or cancel it.",
    },
    {
        "name": "notifications",
        "description": "Operations the Notifications. Manage notifications to users.",
    },
    {"name": "languages", "description": "Operations the Languages.",},
]


def main():
    title = "Daizu Online Judge API v1"
    description = "daizu online judge developping is contest site of the competitive programming"
    version = "0.1.0"

    api = FastAPI(
        title=title,
        version=version,
        description=description,
        openapi_tags=tags_metadata,
    )
    set_route(api)
    uvicorn.run(app=api)


if __name__ == "__main__":
    main()
