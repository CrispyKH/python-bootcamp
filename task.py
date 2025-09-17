import random

'''
#2025-09-09

#TASK 1
#Create coin flip program

number = random.randint(0 , 1)
if number == 0:
    print("Heads!")
else:
    print("Tails!")


#List Formatting
states_of_america = ["Delaware", "Pennsylvania"]

states_of_america.append("Wonderland") #adds to list
states_of_america.extend(["DisneyLand", "Chicago"]) #brings current list into existing
print(states_of_america)

#Task 2
#How to pick a random name from a list of friends

#Option 1 -- good if you know the length of list but impractical
friends = ["Lucas", "Oliver", "Aaron", "Karl", "Robert"] 
a = random.randint(0 , 4)
print(friends[a])
#Option 2 -- better choice, no need for list length, more practical
print(random.choice(friends)) 

#Use lists to separate fruits and vegetables while remaining in a container
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples","Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery","Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

    print these lines for better clarification on how lists work
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
'''
#2025-09-17

#Task 3
#Replicate the max function using knowledge of for loops and lists 
student_scores = [45, 67, 89, 90, 23, 56, 78, 99, 100, 34, 67]
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"This is the maximum score: {max_score}")

