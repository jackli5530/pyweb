#coding:utf-8
class Userlgoin:
    username=""
    userpass=""
    def __init__(self,uname,upass):
        self.username=uname
        self.userpass=upass
    def login(self):
        if self.username=="jack" and self.userpass=="123":
            return True
        return False