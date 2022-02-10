#It's pretty straightforward. Your goal is to create a function that 
# removes the first and last characters of a string. You're given one parameter, 
# the original string. You don't have to worry with strings with less than two characters.

def remove_char(string):
    #Works like split, but a lot more convienient!
    #string[starting index: last index -1 ]
    print(string[1:-1]) 

remove_char("Sloppy")