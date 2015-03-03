""" Introduction to Python - Exercise 18

First Neat List - Loop

* Repeat First Neat List, but this time use a loop to print out your
statements. Make sure you are writing the same sentence for all values in your
list. Loops are not effective when you are trying to generate different output
for each value in your list.
"""

LANGUAGES = ['python', 'c', 'java']

for language in LANGUAGES:
    print "A nice programming language is %s." % language
