def fizz_count(string):
  count = 0
  for value in string:
    if value == "fizz":
    	count += 1
  return count
    
def fizz_buzz(num):
  i = 0
  for value in num: 
    if value % 3 == 0 and value % 5 == 0:
      print "fizzbuzz"
    elif value % 3 == 0:
      print "fizz"
    elif value % 5 == 0:
      print "buzz"
    else:
      print value
