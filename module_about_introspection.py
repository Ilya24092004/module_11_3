from inspect import getmodule


def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': obj.__dir__(),
        'methods': dir(obj),
        'module': getmodule(obj)
    }

number_info = introspection_info(42)
print(number_info)