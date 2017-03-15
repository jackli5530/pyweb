#coding=utf-8
from django.shortcuts import render_to_response
from mydb.models import myuesr
class userregister():
    input_request=None
    def __init__(self,r):
        self.input_request=r
        
    def run(self):  #注册功能与登录类似，都是获取post表单的数据
        database={"result":""}
    
        if self.input_request.method=="POST":
            rename=self.input_request.POST.get("rename")
            repass=self.input_request.POST.get("repass")
            print rename,repass
            results=myuesr.objects.filter(user_name=rename)  #获取注册时的用户名
            if  (len(results)==0 or results[0].user_name!=rename) and rename!="":  #判断用户唯一且不为空
                u=myuesr(user_name=rename,user_pass=repass)
                u.save()  #将注册信息写入数据库
                database["result"]=u"注册成功"
            elif rename=="":
                database["result"]=u"用户名不能为空"
            else:
                database["result"]=u"用户名不唯一"
        re=render_to_response("register.html",database)
        return re
            
        