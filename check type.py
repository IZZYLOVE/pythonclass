# CHECKING INPUT TYPE (NUMBER OR STRING)
""" Sometimes our work, mostly our functions and classes will be tested beyond our User Interface (UI)
to see how well we have handled errors.
"""
# Note it is a bad practice to allow the user see an unhandled error
def testme(num):
    num=num
    print(f"My number is {num} .")

# be = int(input("Enter enter a number: ")).strip()
# testme(be)
# parse the variable be to the function testme above

"""
In the variable above, a lot of errors have been handled at the user end.
like we just said be must be an integer.

Running this program and inputting a string will throw an unhandled error to the user, 
which is a bad practice.

It is better to handle such errors within our function methods or classes
than from the user (input) end

If we comment out the variable 'be' and the call to the function 'testme(be)' as define above and define 
a new variable 'cee' and parse it to the function call 'testme(cee)', we will not be seeing that unhandled 
error thrown to the user.

then we can proceed to handle the error from within our function
"""

cee =  input("Enter enter a number: ").strip()
testme(cee)