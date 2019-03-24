# Coding    :   UTF-8
# Team      :   Vincent
# Author    :   Vincent
# Created on:   2019/3/24 15:17
# File Name :   hello_flask.py
# Tool      :   PyCharm
from flask import Flask, url_for, request, render_template

app = Flask(__name__)


'''
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Sub Path %s' % subpath


# 自动补全斜杠的 URL 重定向
@app.route('/projects/')
def projects():
    """
    该 URL 尾部有一个斜杠，看起来就如同一个文件夹。如果访问这样一个末尾带斜杠的 URL 时没有在结尾带上斜杠，Flask 会自动进行重定向，
    帮你在尾部加上一个斜杠
    """
    return 'The project page'
'''
'''
# 唯一的 URL
@app.route('/about')
def about():
    """
    该 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这个 URL 时添加了尾部斜杠就会得到一个 404 错误, 这样可以保
    持 URL 唯一，并帮助搜索引擎避免重复索引同一页面
    """
    return 'The about page'
'''

'''
# rul_for() 用于重建URL。它把函数名称作为第一个参数，它还可以接受任意个关键字参数，每个关键字参数对应 URL 中的变量，未知变量
# 将添加到 URL 中作为查询参数。
@app.route('/')
def index():
    return 'index'
'''


@app.route('/login')
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'rosydawn':
            if request.form['password'] == '123456':
                return render_template('user.html', name='rosydawn')
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


# 测试url_for()方法对url的构造
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('profile', username='John Doe'))
    print(url_for('profile', username='John Doe', language='zh-cn'))


'''
# 默认情况下，一个路由只回应 GET 请求。 可以使用 route() 装饰器的 methods 参数来处理不同的 HTTP 方法
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # return do_the_login()
        pass
    else:
        # return show_the_login_form()
        pass
'''


# 渲染模板
# Flask 会在 templates 文件夹内寻找模板。因此，如果你的应用是一个模块， 那么模板文件夹应该在模块旁边；如果是一个包，那么就应该在包里面
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/user/<username>')
def show_user_profile(username):
    # 显示该用户名的用户信息
    return render_template('user.html', name=username)


with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

if __name__ == '__main__':
    app.run(debug=True)

