# For loops

again, like other languages, except just a little more verbose

can be used specifically for keys

    webster = {
    "Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
    }

    for key in webster:
      print webster[key]
    
    > A star of a popular children's cartoon show.
    Goes on the floor.
    A small amount.
    The sound a goat makes.

works with conditional logic
       
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    for number in a:
     if number % 2 == 0:
    	print number

strings are simply lists of characters as elements

    for letter in "Codecademy":
        print letter
    
    # Empty lines to make the output pretty
    print
    print

    word = "Programming is fun!"

    for letter in word:
        # Only print out the letter i
        if letter == "i":
            print letter
