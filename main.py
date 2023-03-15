def decor_flask(func):
    
    def wrapp(*args, **kwargs):

        func(*args, **kwargs)
        return func
    
    return wrapp
