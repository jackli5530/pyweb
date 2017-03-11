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
        if self.input_request.method=="POST":
            getusername=self.input_request.POST.get("txtUserName")
            getuserpass=self.input_request.POST.get("txtPassWord")
            Login_result=self.login(getusername, getuserpass)
            if Login_result:
                myresponse=HttpResponse("<script>self.location='/index/index'</script>")
                myresponse.set_cookie("UserLoginName",getusername,3600)
                return myresponse
            else:
                dataset["result"]="用户名密码错误"
        
        myresponse=render_to_response("login.html",dataset)
        return myresponse
    
    
            
    
    def login(self,uname,upass):
        results=myuesr.objects.filter(user_name=uname)
       
        if len(results)==1 and results[0].user_pass==upass:
            return True
        return False