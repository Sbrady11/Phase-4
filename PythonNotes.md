## Python Notes

Looks like its mostly like ruby (just oo)

dont need a def or anything, or let, just ascribe a value

    eg. my_variable = 10
    pring my_variable

booleans require capitalization
     
     True/False

## INDENTATION IS SUPER IMPORTANT

     def spam():
      eggs = 12
      return eggs

    print spam()

Comments '#'
  triple " for making a multi line commment
  """Comment
  yes
  """
  
math can be inside of variables
powers can be **, so 
     
     2**3 = 8

when coming to escaping characters, use a '\' within a string

value of strings, accesing by index:
Use "somestring"[0] returns 's'

## String Concatination
just need to add together different strings

    print "Spam " + "and " + "eggs"

also allowed

    print "The value of pi is around " + str(3.14)
    
The % operator after a string is used to combine a string with variables. The % operator will replace a %s in the string with the string variable that comes after it.

    name = "Mike"
    print "Hello %s" % (name)
    
    > Hello Mike
    
    
    string_1 = "Camelot"
    string_2 = "place"
    print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)
    
    > Let's not go to Camelot. 'Tis a silly place.

## Data input

        name = raw_input("What is your name? ")
        quest = raw_input("What is your quest? ")
        color = raw_input("What is your favorite color? ")

        print "Ah, so your name is %s, your quest is %s, " \
        "and your favorite color is %s." % (name, quest, color)
 
        >What is your name? simon
        What is your quest? i seek the holy grail
        What is your favorite color? blue
        Ah, so your name is simon, your quest is i seek the holy grail, and your favorite color is blue.
        
You use 'raw_input' in order to prompt the user in the console

## DateTime

        from datetime import datetime

        now = datetime.now()
        print now
        
        > 2017-11-09 20:39:07.431010

Looks like were getting access to it, like requiring a gem or a module, then you can call methods on it. It looks like its a 'datetime' object too.

        print now.year
        print now.month
        print now.day
        
        > 2017
        11
        9

can use string interpolation here too

        from datetime import datetime
        now = datetime.now()

        print '%s/%s/%s' % (now.year, now.month, now.day)
        
        > 2017/11/9
        
        from datetime import datetime
        now = datetime.now()

        print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
        
        > 1/9/2017 20:44:15


## Lists

    list_name = [1,2]

It seems in python that arrays are known as lists?

follows the same rules, can access using the index value. is equivalent to stuff youve done in JS and Ruby

slicing the list
    
    some_list = [1,2,3]
    first = some_list[0:2]
    
    print first
    > [1,2]
    
## String slicing
    
    animals = "catdogfrog"

    # The first three characters of animals
    cat = animals[:3]

    # The fourth through sixth characters
    dog = animals[3:6]

    # From the seventh character to the end
    frog = animals[6:]
    
Open ended colon means either from the front (:x) or to the end (x:)

    
## Ordering lists

This is valid

        animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
        
        duck_index = animals.index("duck")
        
        animals.insert(duck_index, 'cobra')
        
        print animals
        
        > ['aardvark', 'badger', 'cobra', 'duck', 'emu', 'fennec fox']
 

ordering your list by finding the index itme is valid, returns the index value of the searched term

## Loops

- for
runs over a list, executes code over a variable you assign

        for number in my_list:
            print 2 * number
            
        start_list = [5, 3, 1, 2, 4]
        square_list = []

        for numbers in start_list:
            square_list.append(numbers ** 2)
  
        square_list.sort()

        print square_list

## Dictionaries

sounds like the hashes

same thing, you can add things to the hash with the similar key:value pairing methods

        menu = {} # Empty dictionary
        menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
        print menu['Chicken Alfredo']

        menu['spaghetti'] = 99.99
        menu['yes'] = 1
        menu['k']= 2

        print "There are " + str(len(menu)) + " items on the menu."
        print menu
        
More dictionary examples

        # key - animal_name : value - location 
        zoo_animals = { 'Unicorn' : 'Cotton Candy House',
        'Sloth' : 'Rainforest Exhibit',
        'Bengal Tiger' : 'Jungle House',
        'Atlantic Puffin' : 'Arctic Exhibit',
        'Rockhopper Penguin' : 'Arctic Exhibit'}
        # A dictionary (or list) declaration may break across multiple lines

        # Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
        del zoo_animals['Unicorn']

        del zoo_animals['Sloth']
        del zoo_animals['Bengal Tiger']

        zoo_animals['Rockhopper Penguin'] = "Yemen"

        print zoo_animals
        
  

