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
        
        if self.input_request.COOKIES.get("UserLoginName")!=None:
            dataset["current"]=self.input_request.COOKIES.get("UserLoginName")
        
        #users=myuesr.objects.filter(user_name="jack")
        #for user in users:
            #print user
        
        myresponse=render_to_response("index.html",dataset)
        return myresponse