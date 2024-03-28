# FizzBuzz printing numbers 1 to 101

for num in range (101):
   #  print(num)

 # number is dividable by 3 print Fizz, number is dividable by 5 print buzz, number is dividable by 3 and 5
     
     if    num % 3==0 and num % 5==0:
           print("fizzbuzz")
           continue
     elif  num % 3==0: 
           print("fizz")
           continue
     elif  num % 5==0: 
           print("buzz")
           continue
     print(num)
                

                 
