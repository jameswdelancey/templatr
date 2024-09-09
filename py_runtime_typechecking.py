from functools import wraps
from inspect import signature

def typecheck(method):
    method_sig = signature(method)
    param_types = {param.name: param.annotation for param, param_type in method_sig.parameters.items()}
    return_type = method_sig.return_annotation

    @wraps(method)
    def wrapper(*args, **kwargs):
        bound_args = method_sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for name, value in bound_args.arguments.items():
            if name in param_types and param_types[name] is not param_types[name].__class__:
                if not isinstance(value, param_types[name]):
                    raise TypeError(f"Argument {name} must be of type {param_types[name].__name__}")

        result = method(*args, **kwargs)

        if return_type is not method.__annotations__['return'].__class__:
            if not isinstance(result, return_type):
                raise TypeError(f"Return value must be of type {return_type.__name__}")

        return result

    return wrapper

# Usage:
# @typecheck
# def my_function(a: int, b: str) -> float:
#     return float(a)
