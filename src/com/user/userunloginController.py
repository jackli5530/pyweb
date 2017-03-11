#coding=utf-8
from django.http.response import HttpResponse
class userunlogin():
    input_request=None
    def __init__(self,r):
        self.input_request=r
    def run(self):
        r=HttpResponse()
        r.delete_cookie("UserLoginName")
        r.write("<script>self.location='/index/index'</script>")
        return r