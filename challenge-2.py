users =[
    {
        "name": "John",
        "age": 25,
        "gender": "male",
        "hobbies": ["swimming", "reading", "dancing"]

    },
    {
        "name": "Sarah",
        "age": 36,
        "gender": "female",
        "hobbies": ["reading", "horse riding", "dancing"]

    },
    {
        "name": "Peter",
        "age": 16,
        "gender": "male",
        "hobbies": ["climbing", "tennis", "scuba diving"]
    },
    {
        "name": "Amy",
        "age": 18,
        "gender": "female",
        "hobbies": ["reading", "scuba diving", "dancing"]
    },
]

# # 1. Print out the names of all users who are male
print("These are the male users:")
for user in users:
    #print(user["gender"])
    if user["gender"] == "male":
        print(user["name"])
    else:
        pass



# 2. print out all the users who are 18 years old or older

print("users who are 18 years or older: ")
for user in users:
    if user["age"] >= 18:
        print(user["name"])
        print(f"user {user['name']} is {user['age']} years old")





# # 3. print out all the users who like reading
print("users who like reading: ")
for user in users:
    #print(user["hobbies"])
    for hobby in user["hobbies"]:
        if hobby == "reading":
         print(user["name"])


# 4. print out all the users that like scuba diving
print("users who like scuba diving: ")
for user in users:
    #print(user["hobbies"])
    for hobby in user["hobbies"]:
        if hobby == "scuba diving":
         print(user["name"])


         

# 5. print out all of the second users details, so Sarah's details
print("The second users details: ")
print(users[1])



