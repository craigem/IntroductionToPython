'''
Exercise 20 - Working List

Working List

* Make a list that includes four careers, such as 'programmer' and 'truck driver'.
* Use the list.index() function to find the index of one career in your list.
* Use the in function to show that this career is in your list.
* Use the append() function to add a new career to your list.
* Use the insert() function to add a new career at the beginning of the list.
* Use a loop to show all the careers in your list.
'''

# Create a list with 4 careers
CAREERS = [ 'Programmer', 'Truck Driver', 'Comedian', 'Nurse' ]
print "The current list of careers is:\n"
for CAREER in CAREERS:
    print(CAREER)

# Get the index of a career and use the "in" function to test this career is
# in the list:
CAREER = 'Comedian'
if CAREER in CAREERS:
    print "\nComedian is in the careers list and has an index of", CAREERS.index( 'Comedian' ), ".\n"
else:
    print "Comedian is not in the careers list.\n"

# Use the append function to add another career:
CAREERS.append('Concert Flautist')
print "Appended Concert Flautist to the list of careers:"
print(CAREERS)

# Use the insert function to add a career to the beginning"
CAREERS.insert(0, 'Garbologist')
print "\nInserted Garbologist into the list of careers:"
print(CAREERS), "\n"

# Use a loop to show all the careers:
print "The final list of careers is:"
for CAREER in CAREERS:
    print(CAREER)


