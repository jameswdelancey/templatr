def ensure_type(value, type_):
    if not isinstance(value, type_):
        raise TypeError(f"Value must be of type {type_.__name__}")
    return value

# Usage:
# value = ensure_type(value, str)  # Ensures that value is a string
