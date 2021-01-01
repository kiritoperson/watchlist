from flask import Flask,render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import click

Win = sys.platform.startswith('win')
if Win: #如果是Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #关闭对模型的修改

db = SQLAlchemy(app)

class  User(db.Model):
    id = db.Column(db.Integer, primary_key = True) #主键
    name = db.Column(db.String(20)) #名字

class Movie(db.Model): #表名将会是movie
    id = db.Column(db.Integer, primary_key = True) #主键
    title = db.Column(db.String(60))    #电影标题
    year = db.Column(db.String(4))  #电影年份


@app.route('/test')
def index():
    user = User.query.first() #读取用户记录
    movies = Movie.query.all()  #读取所有电影记录
    return render_template('index.html', user=user, movies=movies)

def test_url_for():
    # 下面是一些调用示例
    print(url_for('hello'))

    print(url_for('test_url_for')) #输出/test
    #下面这个调用传人多余的关键字参数
    print(url_for('test_url_for', num=2))
    return 'test page'

@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()
#全局的两个变量移动到这个函数内

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
{'title': 'Dead Poets Society', 'year': '1989'},
{'title': 'A Perfect World', 'year': '1993'},
{'title': 'Leon', 'year': '1994'},
{'title': 'Mahjong', 'year': '1996'},
{'title': 'Swallowtail Butterfly', 'year': '1996'},
{'title': 'King of Comedy', 'year': '1999'},
{'title': 'Devils on the Doorstep', 'year': '1999'},
{'title': 'WALL-E', 'year': '2008'},
{'title': 'The Pork of Music', 'year': '2012'},
]

user = User(name=name)
db.session.add(user)
for m in movies:
    movie = Movie(title=m['title'], year=m['year'])
    db.session.add(movie)

db.session.commit()
click.echo('Done.')
    