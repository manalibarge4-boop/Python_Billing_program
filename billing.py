"""Write a python program which will keep adding a
 stream of numbers inputed by the user. the adding 
 stops as soon as user pressed 'q' keyon the 
 keyboard """

sum = 0  #created a variable called sum and start it at 0
while True: #Keep repeating forever until we explicitly tell the loop to stop. (python will repeatedly ask Enter price)
    
    userInput = input("Enter price: \n") #taking input from the user, input is string not number '100'
    
    if userInput != 'q': #100 is not q → True → continue. q is equal to q → False → go to else.
        
        sum = sum + int(userInput) #Suppose you enter: 100, Initially: sum=0, then sum=0+100, so sum=100
        
        print(f"Order total so far: {sum}") #the f string allows Python to put the value of sum inside the sentence.
    
    else:
        
        print(f"Your billing total is {sum}. Thanks for shopping with us ")  
        
        break #Stop the loop immediately.

