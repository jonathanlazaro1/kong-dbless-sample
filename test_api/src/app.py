import os
import falcon
import falcon.asgi

from src.customer import CustomerResource



def build_app():
    app = falcon.asgi.App()

    customer = CustomerResource()

    app.add_route(f"/customers", customer)


    return app
