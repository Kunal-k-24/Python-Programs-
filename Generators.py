def generators ( ):
    print('1')
    print('2')
    print('3')
    yield
    print('4')
    print('5')
    print('6')
    yield
    print('7')
    print('8')
    print('9')
    yield               # it must ends with 'yield'

# We have to start the main body like as shown below we don't have to apply indentation to it

print("Main Area Starts")   # program starts from here like "void main (){ " in C
rec=generators()            # We called the Function here which we created above as "def generators"
print("1st Portion before yield")
rec.__next__()              # Member Function __next__()
rec2=generators()
print("2nd Portion after yield-1")
rec.__next__()
print("3rd Portion after yield-3 ")
rec3=generators()
rec.__next__()
print("Main Area Ends")

# This Is the end of the program and if you want to logical blocks then start indentation from here
# Because Indentation represents the body of that particular logical block or function
