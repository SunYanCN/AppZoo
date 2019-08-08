<h1 align = "center">:rocket: RestfulApi :facepunch:</h1>

---
> 模型部署

## Install
```bash
pip install iapp -U
```
## Usage
```python
import jieba
from iapp import App

pred1 = lambda **kwargs: kwargs['x'] + kwargs['y']
pred2 = lambda x=1, y=1: x - y
pred3 = lambda text='小米是家不错的公司': jieba.lcut(text)

app = App()
app.add_route(pred1, "/f1")
app.add_route(pred2, "/f2")
app.add_route(pred3, "/f3")

app.run()
```