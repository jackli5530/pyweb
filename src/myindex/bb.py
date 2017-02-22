#coding=utf-8
from django.shortcuts import render_to_response

def hi(request):
    dataset={"result":"必须输入数字"}
    if "mustnum" in request.POST and isMyNumber(request.POST.get("mustnum")):
        dataset["result"]="输入正确"
    else:
        dataset["result"]="输入不正确"
    
    return render_to_response("index.html",dataset)

def isMyNumber(num):
    if num.isnumeric() and int(num)>1:
        return True
    else:
        return False