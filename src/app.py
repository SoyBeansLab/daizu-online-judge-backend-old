from fastapi import FastAPI
import uvicorn

from infrastructure.waf.fastapi.router import set_route


def main():
    title = "Daizu Online Judge API"
    description = "daizu online judge developping is contest site of the competitive programming"
    version = "0.1.0"

    api = FastAPI(
        title=title,
        version=version,
        description=description,
    )
    set_route(api)
    uvicorn.run(app=api)


if __name__ == "__main__":
    main()
