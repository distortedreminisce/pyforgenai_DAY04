
try: 
	a = int(input("Input an integer"))
	b = int(input("Input another integer"))
  
	result = a/b
except ZeroDivisionError:
	print("cannot divide by zero")
except ValueError:
	print("not a number")
  
  
