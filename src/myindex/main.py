#coding=utf-8

from django.http.response import HttpResponse
from com.CommonFucsh import loadClass


def index(request,c1,c2,):
    
    
    getclass=loadClass("com."+c1+"."+c2+"Controller",c2,request)
    if getclass==None:
        return HttpResponse("404")
    return getclass.run()

