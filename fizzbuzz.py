def fizz_count(string):
  count = 0
  for value in string:
    if value == "fizz":
    	count += 1
  return count
    
def fizz_buzz(number):
  print("\n".join(["Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i) for i in range(1,number + 1)]))
  
