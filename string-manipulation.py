message = "Hello, please tell sarah i want to speak to her"

print(message)

print(message.lower())
print(message.upper())

# print(message.split(" "))
message_list = message.split(" ")
print (message_list)

for item in message_list:
    print(item)

comma_separated = message.split(", ")

print(comma_separated[1])



