class Singleton(object):
    # really working class
    class Wrapper_class(object):
 
        def __init__(self, name):
            self.name = name
 
        def show_id(self):
            return id(self)
 
        def work(self):
            print('i am working')
 
    # save Wrapper_class instance
    _instance = None
 
    def __init__(self):
        if Singleton._instance is None:
            Singleton._instance = Singleton.Wrapper_class('wrapper')
    # when get attribute if not exist, call this function. it return getattr function. 
    def __getattr__(self, item):
        return getattr(self._instance, item)
    # getattr include three params: instance name, attribute or method name, default value when instance not include attribute
 
if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    print(a)
    print(b)
    print(a.show_id())
    print(b.show_id())