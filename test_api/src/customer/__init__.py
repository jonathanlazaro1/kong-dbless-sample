import time

from faker import Faker
from falcon.asgi import Request, Response


class CustomerResource:

    def __init__(self) -> None:
        self.__fake = Faker()

    async def on_get(self, req: Request, resp: Response):
        ns = req.get_param_as_int("n", min_value=1, default=10)
        t = req.get_param_as_int("t", min_value=0, default=0)

        result = []

        for n in range(ns):
            result.append({
                "id": n + 1,
                "name": self.__fake.name()
            })

        time.sleep(t)

        resp.media = result
