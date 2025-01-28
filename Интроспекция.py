class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value * 2


def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__


    attributes = [attr for attr in dir(obj) if not attr.startswith('__') and not callable(getattr(obj, attr))]
    info['attributes'] = attributes


    methods = [method for method in dir(obj) if method.startswith('__') or callable(getattr(obj, method))]
    info['methods'] = methods


    info['module'] = getattr(obj, '__module__', None)


    info['doc'] = getattr(obj, '__doc__', None)

    return info



number_info = introspection_info(42)
print(number_info)

my_object = MyClass(10)
class_info = introspection_info(my_object)
print(class_info)
