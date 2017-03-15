#coding=utf-8
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from mydb.models import myuesr
class userlogin():
    input_request=None
    def __init__(self,r):
        self.input_request=r
    def run(self):
        beijing={"id":1,"name":"北京"}
        shanghai={"id":2,"name":"上海"}
        arase=[beijing,shanghai]
        dataset={"result":"","Arase":arase}
        if self.input_request.method=="POST":  #如果为post请求
            getusername=self.input_request.POST.get("txtUserName")  #获取用户名
            getuserpass=self.input_request.POST.get("txtPassWord")  #获取密码
            Login_result=self.login(getusername, getuserpass) #调用登录函数，判断登录情况
            if Login_result:  #如果登录成功
                myresponse=HttpResponse("<script>self.location='/index/index'</script>")  #跳转页面
                myresponse.set_cookie("UserLoginName",getusername,3600) #设置cookie
                return myresponse
            else:
                dataset["result"]="用户名密码错误"
        
        myresponse=render_to_response("login.html",dataset)  #返回登录页
        return myresponse
      
    def login(self,uname,upass):  #判断登录情况函数
        results=myuesr.objects.filter(user_name=uname) #获该用户名的对象
       
        if len(results)==1 and results[0].user_pass==upass:  #如果该对象唯一且密码一致，则返回真
            return True
        return False