# kong-dbless-sample

This is nothing more than a simple kong db-less sample. It has a kong db-less instance, and a simple [Falcon](https://falcon.readthedocs.io/) API which is configured as a service inside kong.

kong's configuration is inside [kong.json](./kong.json) file, which is also mapped as a volume inside kong container.

To run it all, simply execute `docker-compose up`.

The main requests are mapped inside the [use.http](./use.http) file. If you want to change any kong configuration, just update `kong.json` and then call the `Update kong config` endpoint from `use.http` file.

## About `/customers` endpoint

Our sample API has a single endpoint, `/customers`, which (shockingly) returns a list of customers, with Id and name. You can call it directly (with no parameters) or pass one or all of the parameters below:

- `n`: the number of clients you want to return. Default is `10`
- `t`: the number of seconds you want the API to wait before returning the results. Default is `0`
