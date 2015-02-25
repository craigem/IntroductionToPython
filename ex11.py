"""Introduction to Python - Exercise 11

Python 2 or Python 3?
* Use integer division to show whether your Python interpreter is using Python
2 or Python 3."""

DIVISION_1 = 6 / 4
try:
    isNumberint = int(DIVISION_1)
    print "6 divided 4 is: %s, which is an integer" % DIVISION_1
    print "You are using Python 2"
except:
    print "6 divided 4 is: %s, which is not an integer" % DIVISION_1
    print "You are using Python 3"
