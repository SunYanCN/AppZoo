<h1 align = "center">:rocket: RestfulApi :facepunch:</h1>

---
> 模型部署

## Install
```bash
pip install restful_api -U
```
## Usage
```python
import jieba
from restful_api import Api


pred1 = lambda **kwargs: kwargs['x'] + kwargs['y']
pred2 = lambda x=1, y=1: x + y
pred3 = lambda text='小米是家不错的公司': jieba.lcut(text)

api = Api('/post1', pred1)
api = Api('/post2', pred2, app=api.app)
api = Api('/post3', pred3, app=api.app)
api.app.run()
```

## Test
```python
import requests
json = {'x': 1, 'y': 10}
requests.post('http://127.0.0.1:5000/post1', json=json).json()
requests.post('http://127.0.0.1:5000/post2', json=json).json()
requests.post('http://127.0.0.1:5000/post2', json=json).json()
```