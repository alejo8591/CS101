#!/usr/bin/env python# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.

def sum3(a,b,c):
    return a+b+c

#print sum3(1,2,3)
#>>> 6

#print sum3(93,53,70)
#>>> 216

# Define a procedure, square, that takes one number 
# as its input, and returns the square of that 
# number (result of multiplying
# the number by itself).

def square(n):
    return n*n

# To test your procedure, uncomment the print 
# statement below, by removing the hash mark (#) 
# at the beginning of the line.

# Do not remove the # from in front of the line 
# with the arrows (>>>). Lines which begin like 
# this (#>>>) are included to show the results
# you should see when run your procedure.

#print square(5)
#>>> 25

# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.

def sum3(a,b,c):
    return a+b+c

#print sum3(1,2,3)
#>>> 6

#print sum3(93,53,70)
#>>> 216

# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.


def abbaize(a,b):
    return a+b*2+a

#print abbaize('a','b')
#>>> 'abba'

#print abbaize('dog','cat')
#>>> 'dogcatcatdog'

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(a,b):
    if(a>b):return a
    return b

#print bigger(2,7)
#>>> 7

#print bigger(3,2)
#>>> 3

#print bigger(3,3)
#>>> 3

# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'


def is_friend(a):
    if a[0].lower() == 'd': return True
    return False

#print is_friend('Diane')
#>>> True

#print is_friend('Fred')
#>>> False

# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(a):
    if(a[0].lower() == 'd' or a[0].lower() == 'n'): return True
    return False


#print is_friend('Diane')
#>>> True

#print is_friend('Ned')
#>>> True

#print is_friend('Moe')
#>>> False

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a,b,c):
    if(a > b and a > c):
        return a
    elif(b > c and b > a):
        return b
    elif(c > a and c > b):
        return c
    else:
        return a

#print biggest(3, 6, 9)
#>>> 9

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(a):
    i=0
    while(i<a):
        i +=1
        print i
        
# Other solution
def print_numbers1(a):
    i=1
    while True:
        if i > a: break
        print i
        i = i + 1
    

#print_numbers(3)
#>>> 1
#>>> 2
#>>> 3

# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.
def factorial(n):
    if(n==0):return 1
    i, o= n, 1
    while(i!=0):
     o=o*i
     i-=1 
    return o
#print factorial(4)
#>>> 24
#print factorial(5)
#>>> 120
#print factorial(6)
#>>> 720
# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

def get_next_target(page):
    start_link = page.find('<a href=')
    #Insert your code below here
    while start_link != -1: 
         start_quote = page.find('"', start_link)
         end_quote = page.find('"', start_quote + 1)
         url = page[start_quote + 1:end_quote]
         return url, end_quote
    return None, 0

url, endpos = get_next_target('hola mundo <a href="yopiando.com">Asi es</a>')
if url: print "Yes"
print "No"
# Other Option
def get_next_target1(page):
    start_link = page.find('<a href=')
    #Insert your code below here
    if start_link != -1: return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
url, endpos = get_next_target('hola mundo <a href="yopiando.com">Asi es</a>')
if url: print "Yes"
print "No"

# Print all links
def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
            # return "No"

#-------------------- Udacify --------------------------------
# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'

# Make sure your procedure has a return statement.

def udacify(a):
    return 'U'+a

# Remove the hash, #, from infront of print to test your code.

#print udacify('dacians')
#>>> Udacians

#print udacify('turn')
#>>> Uturn

#print udacify('boat')
#>>> Uboat

# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b: return a
    return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    m = biggest(a,b,c)
    if(a == m and a == b and a == c): return a
    elif (a == m and a == b and a!= c): 
        if a < c: return c
        return a
    elif (a == m and a == c and a != b):
        if a < b: return b
        return a
    elif(b == m and b == c and b != a):
        if b < a: return a
        return b
    elif (a == m and a != b and a != c):
        if b < c: return c
        return b
    elif (b == m and b != a and b != c):
        if a < c: return c
        return a
    elif (c == m and c !=a and c != b):
        if a < b: return b
        return a
   
#print(median(1,2,3))
#>>> 2

#print(median(9,3,6))
#>>> 6

#print(median(7,8,7))
#>>> 7
# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(n):
    while True:
        if(n!=1):
            print n
            n -=1
        else:
            if(n==1):
                print n
                print 'Blastoff!'
                break

#countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!

# .......... Other option ........
# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(n):
    while True:
        if(n!=0):
            print n
            n -=1
        else:
            print 'Blastoff!'
            break

#countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!

# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(a,b):
    if len(b) == 1: 
        return a.find(b, -1)
    elif b == "":
        return len(a)
    elif len(b) > 1:
        find_next, find_first, find_lasts = -1, 0, 0
        while True:
            if find_lasts != -1:
                find_first = a.find(b, find_next+1)
                find_next = a.find(b, find_first+1)
                find_lasts = a.find(b, find_next+1)
            else:
                return find_next     
    return -1
#Other option and best option

def find_last(a,b):
    find_lasts, posit = -1, 0
    while True:
        posit = a.find(b, find_lasts+1)
        if posit == -1: return find_lasts
        find_lasts = posit

       
#print find_last('aaaa', 'a')
#>>> 3

#print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0

# 2 GOLD STARS

# Define a procedure, print_multiplication_table,
# that takes as input a positive whole number, and prints out a multiplication,
# table showing all the whole number multiplications up to and including the
# input number. The order in which the equations are printed matters.

# Hint: You can not add an integer and a string, but in homework 1.9
# you came across a method, str, for turning an integer into a string.

def print_multiplication_table(n):
    i,j= 0,0
    while i < n:
        j = 0
        i+=1
        while j < n:
            j+=1
            print '%s * %s = %s' %(i, j, i*j)
            
            
def print_multiplication_table(n):
    i= 1
    while i <= n:
        j = 1
        while j <= n:
            print '%s * %s = %s' %(i, j, i*j)
            j+=1
        i+=1
#print_multiplication_table(2)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4

#print_multiplication_table(3)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 1 * 3 = 3
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4
#>>> 2 * 3 = 6
#>>> 3 * 1 = 3
#>>> 3 * 2 = 6
#>>> 3 * 3 = 9
# Problem extra set Unit 2
# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    # your code here
    if day.capitalize() == 'Saturday' or day.capitalize() == 'Sunday': return True
    return False
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False