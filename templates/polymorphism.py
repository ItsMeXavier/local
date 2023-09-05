                    # method of overriding  in single inheritance

# class inner():
#     def show(self):
#         print("this is a man")
# class outer(inner):
#     def show(self):
#         print ("this is  women")
# s=outer()
# s.show()



# # method of overloading
# class area():
#     def find_area(self,a=None,b=None):
#         if (a!=None and b!=None):
#             print("area of the square", a*b)
#         elif  a!=None:
#             print(f"area of square {a**2}")
#         else:
#             print("nothing to find")
# Area=area()
# Area.find_area(2)
# Area.find_area(2,3)
# Area.find_area()


class ab():

    def A(self,a):
        print(a*2)
    def A(self,a,b):
        print(a*b)


s=ab()
s.A(1,2)
print(s.A)




