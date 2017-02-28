#coding=utf-8
from django.shortcuts import render_to_response

from UserClass import Userlgoin
from django.http.response import HttpResponse
from anaconda_navigator.utils.py3compat import request


def index(request,c1,c2):
    if c1=="index":
        return hi(request)
    if c1=="login":
        return login(request)
    packg=__import__("myindex")
    pyfile=getattr(packg, "UserClass")
    #pyfile.test()
    getclass=getattr(pyfile,"Userlgoin")
    uc=Userlgoin("jack","123")
    uc.run()
    return HttpResponse('404')

def hi(request):
    dataset={"result":"","current":u"游客"}
    
    if request.COOKIES.get("UserLoginName")!=None:
        dataset["current"]=request.COOKIES.get("UserLoginName")
        
    myresponse=render_to_response("index.html",dataset)
    return myresponse




def login(request):
    beijing={"id":1,"name":"北京"}
    shanghai={"id":2,"name":"上海"}
    arase=[beijing,shanghai]
    dataset={"result":"","Arase":arase}
        
    if request.method=="POST":
        getusername=request.POST.get("txtUserName")
        getuserpass=request.POST.get("txtPassWord")
        uLogin=Userlgoin(getusername,getuserpass)
        if uLogin.login():
            myresponse=HttpResponse("<script>self.location='/index'</script>")
            myresponse.set_cookie("UserLoginName",getusername,3600)
            return myresponse
        else:
            dataset["result"]="用户名密码错误"
    myresponse=render_to_response("login.html",dataset)
    return myresponse

def unlogin(request):
    r=HttpResponse()
    r.delete_cookie("UserLoginName")
    r.write("<script>self.location='/index'</script>")
    return r

