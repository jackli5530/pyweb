#coding:utf-8
def test():
    print"test"
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
    
    def run(self):
        print "run"