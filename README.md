# sklearn-restful

```python
from model_restful_api import restful_api
from flask_restful.reqparse import RequestParser


class Model(object):

    def __init__(self, routing='/xx', *args, **kwargs):
        self.routing = routing
        self.parser = RequestParser()
        self.parser.add_argument("id_", type=str, default='xxxxxxxxxxxx')
        self.parser.add_argument("id", type=str,  # type=lambda x: x.split(',')
                                 location="args",
                                 required=True,
                                 case_sensitive=False,
                                 help=None)

    def predict(self, **kwargs):
        """kwargs = self.parser.parse_args(strict=True)"""
        return kwargs

    def preprocessing(self, *args, **kwargs):
        pass

restful_api(Model).app()
```
