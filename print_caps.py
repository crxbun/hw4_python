def allcaps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper