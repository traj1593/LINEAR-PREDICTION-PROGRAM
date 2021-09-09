'''
Program: LINEAR PREDICTION
Filename: linearPrediction-tRaj-00.py
Author: Tushar Raj
Description: The program accepts two integers from a user at the console and uses them to predict the next number in the linear sequence.
Revisions: No revisions made
'''
### Step 1: Announce, prompt and get response

#Announce
print("LINEAR PREDICTION");
print("predict the 3rd number in a sequence\n");

#Prompt user to get response
first_number = input("Enter the 1st number: ")
second_number = input("Enter the 2nd number: ")

###Step 2: Compute the next number in the linear sequence

#convert the string into integer data type
converted_first_number = int(first_number)
converted_second_number = int(second_number)

#Calculate the difference between the first number and second number and store in a variable
difference = converted_first_number - converted_second_number
#Subtract the difference from the second number to get the predicted number
predicted_number = converted_second_number - difference

###Step 3: Print the linear sequence along with the predicted number

print("The linear sequence is: ",first_number,second_number,predicted_number)
