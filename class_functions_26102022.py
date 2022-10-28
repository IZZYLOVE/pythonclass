from multipledispatch import dispatch
# #functions
# def function_name():
#     pass
#     #statement
#
# #eg
# def Addnumbers(num1,num2):
#     print(num1+num2)
#
# Addnumbers(5,7)

# def FullName(first_name,last_name,middle_name=''):
#     if middle_name:
#         fprmated_name=f"{first_name} {last_name} {middle_name}"
#     else:
#         fprmated_name = f"{first_name} {last_name} {middle_name}"
#     return fprmated_name
# print(FullName("Victor","Okoro","Peter"))

def RSum(*args):
    xsum=0
    for number in args:
        xsum=xsum+number
    return f"The running sum is {xsum}"
print(RSum(11,2,3))


@dispatch(int,int,int)
def calc(num1,num2,num3):
    print(num1+num2+num3)


@dispatch(int,int)
def calc(num1,num2):
    print(num1+num2)

#calc(2,4,4)

