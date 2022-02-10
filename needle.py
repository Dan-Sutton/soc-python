# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle, so:
# find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
# should return "found the needle at position 5" (in COBOL "found the needle at position 6")


#Comments use HASH symbol
#Use snake_case 

#USE "def" to define a function rather than "function"
def find_needle(haystack):
    #No curly brackets to enclose a function's logic
    #We use a colon and indentation instead

    needle_index = haystack.index("needle")
    #When declaring variables, no key word needed e.g "let"

    print("Found the needle at position " f'{needle_index}')
    #print() instead of console.log
    #Instead of `${string interpolation}`, we use 'f string' -> (f'{string})'



find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])
