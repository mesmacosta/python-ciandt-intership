"""Main flask app."""
from os.path import join, dirname

import connexion
import yaml

from jinja2 import Environment, PackageLoader
from filters import get_all_apis_router, get_entity_fields


SWAGGER_PATH = "backend/swagger/"
API_PATH = 'endpoints'

app = connexion.App(__name__, specification_dir=SWAGGER_PATH)
application = app.app
application.url_map.strict_slashes = False


_env = Environment(loader=PackageLoader('swagger'))
swagger_string = _env.get_template("main.yaml").render(
    lstrip=False,
    api=get_all_apis_router("api", SWAGGER_PATH),
    schemas=get_all_apis_router("schemas", SWAGGER_PATH),
    **get_entity_fields(),
)
import pprint
pprint.pprint(swagger_string)

specification = yaml.safe_load(swagger_string)

app.add_api(
    specification,
    resolver=connexion.RestyResolver(API_PATH),
    options={"swagger_ui": True},
)

if __name__ == '__main__':
    app.run()
