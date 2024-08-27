# Leap year checker.

# Year =int(input("please enter the year you want to check:--"))
# if ( Year % 400 == 0 )  and  ( Year % 100 == 0 ):
#     print(Year, "is a leap year")
# elif (Year % 4 == 0) and (Year % 100 != 0):
#     print(Year, "is a leap year")
# else:
#     print(Year, "is not a leap year")


# Triangle is equilateral, isosceles or scalene
#
# a=float(input("enter the length of side a"))
# b=float(input("enter the length of side b"))
# c=float(input("enter the length of side c"))
#
# if a==b and  b==c and a==c:
#     print("this is equilateral triangle")
# elif a==b or b==c or  c==a:
#     print("this is Isosceles triangle")
# else:
#     print("This is a scalene triangle")


#  Write a program that prints numbers from 1 to 100. # Loop For
#However, for multiples of 3, print "Fizz" instead of the number, and
#for multiples of 5, print "Buzz."
#For numbers that are multiples of both 3 and 5, print "FizzBuzz."


# n = int(input("enter one number :="))
# if n % 3 == 0 and n % 5 == 0:
#     print("fizz- buzz")
# elif n % 5 == 0:
#     print("buzz")
# elif n % 3 == 0:
#     print("fizz")
# else:
#     print(n)



# or

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizz- buzz")
#     elif i % 5 == 0:
#         print("buzz")
#     elif i % 3 == 0:
#         print("fizz")
#     else:
#         print(i)


# #Factorial n
#
# n=int(input("enter the number : "))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f)
#
# #using while loop
#
# n1=int(input("enter the number : "))
# fact=1
# i=1
# while i<=n1:
#     fact=fact*i
#     i=i+1
# print(fact)


#fibonacchi series

n2=int(input("enter the number : "))
x=0
y=1
fi=0
for i in range(1,n2+1):
    print(fi)
    x=y
    y=fi
    fi=x+y


