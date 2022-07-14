#1.What are the two values of the Boolean data type? How do you write them?

#1. True
#2. False

#2. What are different type of boolean operators?
# and
# or
# not

#4. What are the values of the following expressions?
(5 > 4) and (3 == 5)
#False
not (5 > 4)
#False
(5 > 4) or (3 == 5)
#True
not ((5 > 4) or (3 == 5))
#False
(True and True) and (True == False)
#False
(not False) or (not True)
#True

#5. What are the six comparison operators?
# ==
# >=
# <=
# >
# <
# !=

#6. How do you tell the difference between the equal to and assignment operators?Describe a
#condition and when you would use one.

# assignment operator :- =
# equal to operator :- ==

#Assignment
check = 0

# equal to
if check == 0:
    print(True)



#7. Identify the three blocks in this code:
spam = 0
#First block
if spam == 10:
    print('eggs')
#Second block
if spam > 5:
    print('bacon')
#Third block
else:
    print('ham')
    print('spam')
    print('spam')


#8. Write code that prints Hello if 1 is stored in spam,
# prints Howdy if 2 is stored in spam, and prints Greetings!
# if anything else is stored in spam.


#You can insert different values in spam to check
spam = 1


if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")

#9.If your programme is stuck in an endless loop, what keys you’ll press?

# ctrl + f2 in pycharm


#10. How can you tell the difference between break and continue?

#Break terminates the loop
#Continue skips the iteration

#11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# No difference

#12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
#program that prints the numbers 1 to 10 using a while loop.

for i in range(1,11):
    print(i)

i=1
while i<=10:
   print(i)
   i+=1

#13. If you had a function named bacon() inside a module named spam, how would you call it after
#importing spam?

#bacon()

