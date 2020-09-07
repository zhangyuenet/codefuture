
# 链式操作只需要在操作方法中将自己返回即可。
class Foo2():
    def __init__(self, path=''):
        self._path = path

    def operation(self ,path):
        return Foo2('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

d = Foo2().operation('param1').operation('param2').operation('param3').operation('addparams')
print(d)



#更简单和实用的做法是，可以使用__getattr__简单的获取所有的参数。
class Foo(object): 
    def __init__(self, path=''):
        self._path = path
 
    def __getattr__(self, path):
        return Foo('%s/%s' % (self._path, path))
 
    def __str__(self):
        return self._path


c = Foo().param1.param2.param3.add1.add2.add3.add4
print(c)
