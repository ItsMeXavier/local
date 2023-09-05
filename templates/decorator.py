def smart_Div(div):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return div(a,b)
    return inner
@smart_Div
def div(a,b):
    print (a/b)
div(2,4)







                                            # decorator
# def decorator(greed):
#     def inner():
#         print("xxxxxxxxxxxxxxxxx")
#         greed()
#         print("vvvvvvvvvvvvvvvvv")
#     return inner
# @decorator
# def greed():
#     print("vikas")
# greed()
    

                                # febonicciserie
# def f(n):
#     if n<=1:
#         return n
#     else:
#         return f(n-1) + f(n-2)

# print(f(12))
