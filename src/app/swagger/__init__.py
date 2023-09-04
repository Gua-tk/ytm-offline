from flask import current_app as app
from flasgger import Swagger

swagger = Swagger(app)
