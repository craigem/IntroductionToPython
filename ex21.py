'''
Exercise 21 - Starting From Empty

* Create the list you ended up with in Working List, but this time start your
file with an empty list and fill it up using append() statements.
* Print a statement that tells us what the first career you thought of was.
* Print a statement that tells us what the last career you thought of was.
'''

# Create an empty list of careers:
CAREERS = []

# Fill it up using append statments:
CAREERS.append('Garbologist')
CAREERS.append('Programmer')
CAREERS.append('Truck Driver')
CAREERS.append('Comedian')
CAREERS.append('Nurse')
CAREERS.append('Concert Flautist')

# Print a statement naming the first career:
FIRSTCAREER = 'Programmer'
if FIRSTCAREER in CAREERS:
    print "The first career I thought of was %s." % FIRSTCAREER
else:
    print "Your first career is not in the list."

# Print a statement naming the first career:
LASTCAREER = 'Garbologist'
if LASTCAREER in CAREERS:
    print "The last career I thought of was %s." % LASTCAREER
else:
    print "Your last career is not in the list."
