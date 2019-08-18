import responder

from infrastructure.waf.responder.router import set_route


def main():
    api = responder.API()
    set_route(api)
    api.run(address='0.0.0.0', port=5042)


if __name__ == '__main__':
    main()
