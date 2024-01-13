#Q1.
# From this message, create a new list called fruits_list and using indexing put only the fruits in the message in the list
# message = "My favourite fruits are: apples, bananas, pears"
# #print(message.split(":")[1].split(", "))
# fruits_list = (message.split(":")[1].split(", "))
# print(fruits_list)



#Q2
# #create a new list called new_list and using for loops and only the numbers greater than 50 into the new list

# number_list = [10, 50, 80, 150, 300, 16, 24]
# new_list = []
# for number in number_list:
#     #print(number)
#     if number > 50:
#         new_list.append(number)
# print(new_list)


#Q3
# # create a function called maximum number that takes in 3 parameters or number and return the largest number
    
def maximum_number(num1, num2, num3):
    """
    Returns the largest number among the three input parameters.
    """
    return max(num1, num2, num3)

# Example usage:
result = maximum_number(45, 78, 32)
print("The maximum number is:", result)








