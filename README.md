Flask-Token
===
## Flask-Token: 快速生成API认证令牌<br/>

## 基于令牌的认证<br/>
目前API认证有两种方式：1.基于用户名和密码的认证 2. 基于token令牌的认证<br/>
基于用户名和密码的认证会很方便，只需在请求API时加上用户名和密码，但是密码是通过HTTP明文传输的，
这是很不安全的，即使通过诸如HTTPS这样安全的HTTP传输也有被盗用的风险。<br/>
而基于令牌的认证则是依据用户信息生成令牌，依靠具有一定寿命期限的令牌交换进行认证，虽然生成令牌的
加密算法不是很复杂，但是令牌短暂的寿命则可以有效的减少被破解后带来的危害<br/>

## 使用 flask-token 扩展<br/>
使用 flask-token 扩展可以很方便的帮我们生成认证令牌<br/>
### 1. 导入并初始化扩展:

    from flask.ext.token import Token

    token = Token(app)

### 2. 在User类模型中继承TokenBase类:

    from flask.ext.token import TokenBase

    class User(db.Model, TokenBase):
        ...

### 3. 创建获取令牌的视图函数

    @app.route('/api/token')
    @token.login_required
    def get_token():
        token = g.user.generate_token(3600)
        return jsonify({'token':token.decode('ascii')})

### 4. 获取令牌

    在终端使用命令:

    $ curl -u <username>:<password> -i -X GET http://127.0.0.1:5000/api/token

    即可获取令牌<br/>


## NextStep
有了令牌后就可以思考如何在请求中使用令牌进行验证了。<br/>


## 例子：
可以参考 example 文件夹中的示例程序<br/>


## API
### TokenBase类
TokenBase 类实现了 generate_token 方法和 verify_token 方法<br/>

### generate_token([time])
生成令牌，令牌寿命是time参数指定的值<br/>

### verify_token()
验证令牌，返回令牌的对应的用户<br/>
