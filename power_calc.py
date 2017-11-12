def power(base, exponent):
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

#####################################################################

def cube(number):
  return number ** 3

def by_three(number):
  if number % 3 == 0:
  	return cube(number)
  else:
    return False
  
