from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例
    print(url_for('hello'))

    print(url_for('test_url_for')) #输出/test
    #下面这个调用传人多余的关键字参数
    print(url_for('test_url_for', num=2))
    return 'test page'

