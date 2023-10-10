def allcaps(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs).upper())
    return wrapper