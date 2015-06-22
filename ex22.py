'''
Exercise 22 - Ordered Working List

* Start with the list you created in Working List.
* You are going to print out the list in a number of different orders.
* Each time you print the list, use a for loop.
* Print a message each time telling us what order we should see the list in.
  * Print the list in its original order.
  * Print the list in alphabetical order.
  * Print the list in its original order.
  * Print the list in reverse alphabetical order.
  * Print the list in its original order.
  * Print the list in the reverse order from what it started.
  * Print the list in its original order
  * Permanently sort the list in alphabetical order, and then print it out.
  * Permanently sort the list in reverse alphabetical order & print it out.
'''

# Start with the list from ex20 - Working List
CAREERS = [
    'Garbologist', 'Programmer', 'Truck Driver',
    'Comedian', 'Nurse', 'Concert Flautist']

# Print the original order:
print "\nThis is the original order:"
for CAREER in CAREERS:
    print CAREERS.index(CAREER), CAREER

# Print the list sorted alphabetically:
print "\nThis is the career list sorted alphabetically:"
for CAREER in sorted(CAREERS):
    print CAREERS.index(CAREER), CAREER

# Print the original order:
print "\nThis is the original order again:"
for CAREER in CAREERS:
    print CAREERS.index(CAREER), CAREER

# Print the list sorted reverse alphabetically:
print "\nThis is the career list sorted reverse alphabetically:"
for CAREER in sorted(CAREERS, reverse=True):
    print CAREERS.index(CAREER), CAREER

# Print the original order:
print "\nThis is the original order again:"
for CAREER in CAREERS:
    print CAREERS.index(CAREER), CAREER

# Print the list in reverse:
print "\nThis is the career list in reverse:"
CAREERS.reverse()
for CAREER in CAREERS:
    print CAREERS.index(CAREER), CAREER

# Print the original order:
print "\nThis is the original order again:"
CAREERS.reverse()
for CAREER in CAREERS:
    print CAREERS.index(CAREER), CAREER

# Print the list sorted permanently alphabetically:
print "\nThis is the list sorted permanently alphabetically:"
CAREERS.sort()
for CAREER in CAREERS:
    print CAREERS.index(CAREER), CAREER

# Print the list sorted permanently reverse alphabetically:
print "\nThis is the list sorted permanently reverse alphabetically:"
CAREERS.sort(reverse=True)
for CAREER in CAREERS:
    print CAREERS.index(CAREER), CAREER
