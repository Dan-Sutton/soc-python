# Write a function that will check if two given characters are the same case.

# If any of characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters and not the same case, return 0

def same_case(a, b): 
    
    if a.isalpha() == False or b.isalpha() == False:
        return -1
    elif a.isupper() and b.isupper() or a.islower() and b.islower():
        return 1
    else:
        return 0

# if, elif, else

# if comparison here :
    #Code stuff

# == is the equal to comparison operator
# and or instead of && ||
# isalpha() checks if item is a letter (boolean)
# isupper() islower() checks if a string is uppercase or lowercase