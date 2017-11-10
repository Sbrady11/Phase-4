Looks slightly different to other languages
    
    if answer == 'left' or answer == 'l'
      do this..
    elif answer == 'right' or answer == 'r'
      do this..
    else: 
      do that..
      
## Operators
    ==
    !=
    <=
    <
    >=
    >
    
## Standard Rules
    True and True is True
    True and False is False
    False and True is False
    False and False is False

    True or True is True
    True or False is True
    False or True is True
    False or False is False

    Not True is False
    Not False is True
    
## Order of Operations

Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:

    not is evaluated first;
    and is evaluated next;
    or is evaluated last.
    
For example, True or not False and False returns True. If this isn't clear, look at the Hint.

Parentheses () ensure your expressions are evaluated in the order you want. Anything in parentheses is evaluated as its own unit.

## If/Else
Indentation and notation are like this:

        answer = "'Tis but a scratch!"

        def black_knight():
            if answer == "'Tis but a scratch!":
                return True
            else:             
                return False       # Make sure this returns False

        def french_soldier():
            if answer == "Go away, or I shall taunt you a second time!":
                return True
            else:             
                return False       # Make sure this returns False


