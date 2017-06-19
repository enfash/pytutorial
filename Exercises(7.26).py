#function to count how many odd numbers are in a list.

def count_odd(n):
    counter = 0
    for i in n:
        if i % 2 != 0:
            counter = counter + 1
    print("odd numbers are: ", counter)
    
    

#Sum up all the even numbers in a list

def sum_even(n):
    counter = 0
    for i in n:
        if i % 2 == 0:
            counter = counter + i
    print("the sum are: ", counter)
    

#This is to test the function if it is correct before running or execute

def test(did_pass):
    """ Print the result of the test."""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok. ".format(linenum)
    else:
        msg = "Test at line {0} FAILED. ".format(linenum)

    print(msg)


#Sum up all the negative numbers in a lis

def add_list(n):
    counter = 0
    for i in n:
        if i <  0:
            counter = counter + 1

    print("the sum list are: ", counter)


#Count how many words in a list have length 5
def count_word(n):
    counter = 0
    for i in n:
        if len(i) == 5:
            counter = counter + 1
    print("the words are: ", counter)
    
    
'''Write a function
print_triangular_numbers(n)
that prints out the first n tri-
angular numbers.  A call to
print_triangular_numbers(5)
would produce the
following output:
'''

def print_triangular_numbers(n):
    x = 1
    while x <= n:
        formula = int(x * (x + 1) / 2)
        print(x, '\t', formula)
        x += 1


#######################################################

wrds = ["lang", "language", "Doggy", "Style", "Elija"]
marks = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
count_odd(marks)

sum_even(marks)

count_word(wrds)

add_list(marks)

print(sum(marks))




print_triangular_numbers(5)


