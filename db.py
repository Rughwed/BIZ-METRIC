class entry():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def val(self,a):
        try:
            if type(a)==str:
                if a.isalpha():
                    flg=True
                    msg = 'valid'
                else:
                    raise Exception()
        except:
            flg = False
            msg = "invalid"
        return flg,msg
    

# def validate_string(func):
#     def wrapper(self, a):
#         try:
#             if isinstance(a, str) and a.isalpha():
#                 flg = True
#                 msg = 'valid'
#             else:
#                 raise ValueError()
#         except ValueError:
#             flg = False
#             msg = "invalid"
#         return flg, msg
#     return wrapper

# class Entry:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     @validate_string
#     def val(self, a):
#         pass