def dividedby_op(a,b):
    div_res= a/b;
    print("{4} divided by {2} = {2}".format(a,b,div_res))
    
a = int(input("Enter an number: "))
b = int(input("Enter an number: "))

# I have included two input lines, one for the numerator and one for the demoninator

# I have included the if and else in order to display the string answers that you can see below dependant on the user input. 

if b == 0:
    print ('Error – You cannot divide by 0. Please choose an appropriate denominator.')
else:
    print ('my 1st number/my 2 nd number = my answer',a / b)
    