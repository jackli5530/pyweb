#coding=utf-8
from django.shortcuts import render_to_response
from mydb.models import myuesr
class index():
    input_request=None
    def __init__(self,r):
        self.input_request=r
    
    
    def run(self):
        dataset={"result":"","current":u"游客"}
             
        #u=myuesr(user_name='王五',user_pass='456456')
        #u.save()
        #print u.id
        
        if self.input_request.COOKIES.get("UserLoginName")!=None:  #如果cookie不为空
            dataset["current"]=self.input_request.COOKIES.get("UserLoginName")  #获取设置cookie中的用户名
        
        #users=myuesr.objects.filter(user_name="jack")
        #for user in users:
            #print user
        
        myresponse=render_to_response("index.html",dataset)  #返回首页
        return myresponse