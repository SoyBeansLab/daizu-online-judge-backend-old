import responder

from infrastructure.waf.responder.router import set_route, set_schema


def main():
    description: str = "daizu online judge developping is contest site of" \
            " the competitive programming"
    api = responder.API(
        title="daizu online judge",
        version="0.1.0",
        openapi="3.0.2",
        description=description
    )
    set_route(api)
    set_schema(api)
    api.run(address="0.0.0.0", port=5042)


if __name__ == "__main__":
    main()
