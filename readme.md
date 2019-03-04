<h1 align = "center">:rocket: RestfulApi :facepunch:</h1>

---
> 模型部署

## Usage
```python
from restful_api import Api

pred1 = lambda x, y: x + y
pred2 = lambda x, y: x - y

api = Api(['feat1', 'feat2'], '/post1', pred1)
api = Api(['feat1', 'feat2'], '/post2', pred2, app=api.app)
api.app.run()
```

## Test
```python
import requests
json = {'feat1': 1, 'feat2': 10}
requests.post('http://127.0.0.1:5000/post1', json=json).json()
requests.post('http://127.0.0.1:5000/post2', json=json).json()
```