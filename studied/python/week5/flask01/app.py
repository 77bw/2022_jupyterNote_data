from flask import Flask
from flask import request
from flask import render_template
import utils
#导入能转换成json数据包
from flask import jsonify

app=Flask(__name__)
#1.创建一个flask实列
@app.route("/")#我们使用route装饰器来告诉flask触发函数url,返回两种结果，一个是字符串，一个是整个页面
def hello_word():  #返回字符串
    return render_template("main.html")

#2.构建一个复杂一点页面元素，复制一个路由
@app.route("/ab")
def hell_word1():
    return f"""
    <form>
    账号:<input ><br>
    密码:<input >
    <input type="submit">
    </form>
    """

#3.传递参数，需要引入包:from flask import request
@app.route("/abc")#我们使用route装饰器来告诉flask触发函数url,返回两种结果，一个是字符串，一个是整个页面
def hello_word2():  #返回包含页面元素
    id=request.values.get("id") #使用flask的request的get传递参数
    return f"""
    <form action="/login">
    账号:<input name="name" value="{id}"><br>
    密码:<input name="pwd"  >
    <input type="submit">
    </form>
    """

#在定义一个login的路由
@app.route("/login")#我们使用route装饰器来告诉flask触发函数url,返回两种结果，一个是字符串，一个是整个页面
def hello_word3():  #返回字符串
    name=request.values.get("name")
    pwd = request.values.get("pwd")
    return f"name={name},pwd={pwd}"

#4.使用render_template返回一个模板页面，导入包from flask import render_template
#构建一个index.html页面，然后再定义一个路由
@app.route("/tem",methods=["get","post"])#我们使用route装饰器来告诉flask触发函数url,返回两种结果，一个是字符串，一个是整个页面,增加请求方式
def hello_word4():  #返回字符串
    return render_template("index.html") #返回一个模板

#5.我们如果需要局部的变化而不是整个页面，就用ajiax发送异步请求，这里需要jquer框架，方便些ajiax代码
#在html里面引入jquery.编写ajax请求代码
@app.route("/ajax",methods=["get","post"])#我们使用route装饰器来告诉flask触发函数url,返回两种结果，一个是字符串，一个是整个页面,增加请求方式
def hello_word5():  #返回字符串
    name=request.values.get("name")
    number = request.values.get("number")
    print(f"name={name},pwd={number}")
    return '10000'   

#6.定义一个工具类进行函数功能模块utils.py,再定义一个路由/time,调用utils.py获取时间函数，所以要引入utils.py包
#修改根路由，直接调用main.html
@app.route("/time",methods=["get","post"])
def hello_word6():  #返回字符串
    return utils.get_time()


#7.定义在utils.py定义获取四个1数字的查询，在定义一个c1路由，调用ytils.py的get_c1_data()函数转为字典，回到前端写ajax
@app.route("/c1",methods=["get","post"])
def hello_word7():  #返回字符串
    data= utils.get_c1_data()
    #转换为json数据（字典）
    return jsonify({"confirm":str(data[0]),"suspect":str(data[1]),"heal":str(data[2]),"dead":str(data[3])})


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app.run()