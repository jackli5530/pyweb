#coding=utf-8
def loadClass(pkgPath,className,r):
    try:
        pkg_main=__import__(pkgPath)
        pkg_split=pkgPath.split(".")
        for p in pkg_split[1:]:     #["com","user","userloginController"]
            pkg_main=getattr(pkg_main, p) #加载到文件
        pkg_main=getattr(pkg_main, className)#加载到类
        relclass=pkg_main(r)
        return relclass
    except Exception,e:
        print e
        return None