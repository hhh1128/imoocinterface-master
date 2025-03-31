#coding=utf-8
from flask import Flask
from flask import request #跟requests不一样，这里可以理解为请求上下文
import json
app =Flask(__name__)

@app.route('/passport/user/login',methods=['GET'])
def Login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username and password:
        data =json.dumps({
            "username":username,
            "password":password,
            "code":"200",
            "message":"登录成功",
            "info":"www.baidu.com"
        })
    else:
        data =json.dumps({
        "message":"请传递参数"
        })

@app.route('/passport/user/post_login',methods=['POST'])
def post_login():
    request_method =request.method
    if  request_method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        data = json.dumps({
        "username":username,
        "password":password,
        "code":"200",
        "message":"登录成功",
        "info":"www.baidu.com"
        })
    else:
        data =json.dumps({
        "message":"请求不合法"
        })

    return data   #return不能返回字典，所以用json.dumps()转换成json格式
if  __name__=="__main__":
    app.run()

