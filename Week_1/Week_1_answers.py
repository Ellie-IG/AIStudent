'''
Uppgift 1 

* Create variables to store the name, age, phone number, and email address of a contact.
* Display the contact information in a readable format using f-strings.
'''

print('  Uppgift 1: ')

# Contact information
name: str = 'Ellen Grönholm'
age: int = 20
phone_number: str = '0733976992'
email = 'ellen.gronholm@hotmail.com'

# Display contact information
print("Contact Information:\n--------------------")
print(f"Name: {name} \nAge: {age} \nPhone number: {phone_number} "
      "\nEmail: {email}")

print('______________________________________________')

'''
 Uppgift 2 

Create a list of contact names.
Use a loop to iterate over the list and display a welcome message for each contact.
If the name starts with 'A', display a special message.
'''
    
print('   Uppgift 2:')

# List of contact names
contacts = ["George Washington", "John Adams", "Thomas Jefferson", 
            "James Madison", "James Monroe", "John Quincy Adams", 
            "Andrew Jackson", "Martin Van Buren", "William Hendry Harrison", 
            "John Tyler", "James K.Polk", "Zachary Taylor"]

# Display welcome message for each contact
# Remember, special message for names starting with 'A'
for name in contacts:
    if name.startswith('A'):
        print(f'Hi {name}.')
    else:
        print(f'Hello {name}')

print('______________________________________________')

'''
 Uppgift 3
 
You are building a simple program to manage a list of contacts. You want to create functions to add a new contact, update an existing contact, and display all contacts.

Tasks:
Create functions add_contact, update_contact, and display_contacts.
Implement the functions to add a new contact, update an existing contact, and display all contacts.
Test the functions by adding a new contact, updating an existing contact, and displaying all contacts.
 
'''

print('   Uppgift 3:')

# List of contacts. Each contact is a dictionary with keys 'name', 'phone_number', and 'email'
contacts = []

def add_contact(name: str, phone_number: str, email: str) -> int:
    contacts.append({'name':name, 'phone_number':phone_number, 'email':email})
    contact_id = len(contacts)-1
    # contact_id is the index of the contact in the contacts list
    return contact_id

def update_contact(id: int, name: str, phone_number: str, email: str) -> None:
    contacts[id] =  ({'name':name, 'phone_number':phone_number, 
                      'email':email})

def display_contacts():
    print('The list contains the following people:')
    for logg in contacts:
        print(f'{logg}\n')

# Test the functions
contact_id = add_contact("John Doe", "123-456-7890", "john@example.com")
_ = add_contact("Alice Smith", "123-456-7777", "alice@example.com")
update_contact(
    id=contact_id,
    name="John Doe",
    phone_number="555-555-5555",
    email="john@example.com"
)
display_contacts()

print('______________________________________________')

'''
 Uppgift 4  
You are building a program which stores information about books in a library to disk. You want to use a dictionary to store the book information and save it to a JSON file for persistence.

Tasks:
Create a dictionary to store information about a book, including title, author, year, and ISBN.
Save the book information to a JSON file using the json module.
Load the book information from the JSON file and display it.
 
'''

print('   Uppgift 4:')

import json

# Book information
book = {'title': 'Konsten att höra hjärtslag', 'author': 'Jan-Philipp Sendker',
        'year': 2014, 'ISBN': '9137139517'}

# Save book information to a JSON file
with open("book.json", "w") as file:
    json.dump(book, file)

# Load book information from the JSON file
with open("book.json", "r") as file:
    book_info = json.load(file)

print(f"""
    Book Information:
       Title: {book_info["title"]}
       Author: {book_info["author"]}
       Year: {book_info["year"]}
       ISBN: {book_info["ISBN"]}
    """)

print('______________________________________________')
 
'''    
 Uppgift 5
 
 You manage the inventory for a car dealership. The dealership sells various types of vehicles like cars and trucks. You need to organize vehicle information, including calculating the total inventory value and displaying information about each vehicle in a readable format.

Tasks:
Create a base Vehicle class with attributes for make, model, year, and price.
Create a Car and a Truck subclass, each with a specific feature. Cars have num_doors, and trucks have payload_capacity.
Implement the __str__ dunder method to display vehicle information neatly.
Using the class attributes, calculate the total value of the inventory consisting of a 2023 Toyota Camry, worth $24,000, a 2022 Ford F-150, worth $35,000, and a 2021 Honda Civic, worth $22,000. The Ford F-150 has a payload capacity of 1000 kg and the other two vehicles have 4 doors.

'''

print('   Uppgift 5:')

# Base class Vehicle
class Vehicle:
    def __init__(self, make:str, model:str, year:int, price:int) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        
    def __str__(self):
        return(f'{self.year} {self.make} {self.model} - ${self.price}')
        
class Car(Vehicle):
    def __init__(self, make:str, model:str, year:int, price:int) -> None:
        super().__init__(make, model, year, price)
        self.num_doors = 4
    
    def __str__(self):
        return(f'{self.year} {self.make} {self.model} - ${self.price} '
              f'(Car, {self.num_doors} doors)')
        
class Truck(Vehicle):
    def __init__(self, make:str, model:str, year:int, price:int, 
                 payload_capacity:int) -> None:
        super().__init__(make, model, year, price)
        self.payload_capacity = payload_capacity
    
    def __str__(self):
        return(f'{self.year} {self.make} {self.model} - ${self.price} '
              f'(Truck, Payload capacity: {self.payload_capacity}')

# Inventory list
inventory = [Car('Honda', 'Civic', 2021, 22000), 
             Truck('Ford', 'F-150', 2022, 35000, 1000), 
             Car('Toyota', 'Camry', 2023, 24000)
]
# Display all vehicles and calculate total value
total_value = 0
for vehicle in reversed(inventory):
    total_value += vehicle.price
    print(str(vehicle))
print(f"Total inventory value: ${total_value}")

print('______________________________________________')
 
'''    
 Uppgift 6
 
You are building a user management system that logs user actions like logging in, updating profiles, and making purchases for regulatory reasons. You want to add a decorator to log the timestamp of each action.

Tasks:
Create a decorator function log_action that logs the action name and timestamp.
Decorate the login, update_profile, and make_purchase functions with the log_action decorator.
Test the decorated functions by calling them with sample arguments.
'''

print('   Uppgift 6:')

import time
from functools import wraps

# Decorator to log actions
def log_action(func):
    @wraps(func)
    def log_this_function(*args, **kwargs):
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f'Action: {func.__name__}  | Timestamp: {formatted_time}')
        return func(*args, **kwargs)
    return log_this_function

@log_action
def login(username):
    print(f"{username} logged in successfully.")

@log_action
def update_profile(username, new_email):
    print(f"{username} updated their profile. New email: {new_email}")

@log_action
def make_purchase(username, item):
    print(f"{username} purchased {item}.")

# Test the decorated functions
login("johndoe")
update_profile("johndoe", "john@example.com")
make_purchase("johndoe", "laptop")

print('______________________________________________')
 
'''    
 Uppgift 7
 
 In python, the standard package manager is pip. You can use pip to install external libraries that are not part of the standard library. In this task, you will install the requests library and use it to make a simple HTTP GET request to a public API. The requests library is a popular library for making HTTP requests in Python and does not come pre-installed with Python.

We will install the package into a virtual environment, using venv. Virtual environments help us separate the dependencies for different projects and is a best practice in Python development.

Tasks:
Create a virtual environment using venv.
Activate the virtual environment.
Install the requests library using pip.
Use the requests library to make a GET request to the URL https://jsonplaceholder.typicode.com/posts/1 and display the response content.

'''

print('   Uppgift 7:')

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.content)

print('______________________________________________')
 
'''    
 Uppgift 8
 
Activate the virtual environment again you created in Task 7. 
We will now decode the JSON response from the API into a Python dataclass. 
Dataclasses are a typed alternative to dictionaries ({}). 
Dataclasses provide extend the functionality of dictionaries by allowing you to make the dictionary conform to a schema. 
Dataclasses are also a class which means you can add methods to them unlike to dictionaries.

Tasks:
Create a dataclass Post with attributes userId, id, title, and body.
Decode the JSON response from the API into an instance of the Post dataclass. Repeat for 3 posts.

'''

print('   Uppgift 8:')

import requests
import json

from dataclasses import dataclass

@dataclass
class Post:
    def __init__(self, userId:int, post_id:int, title:str, body:str) -> None:
        self.userId = userId
        self.post_id = post_id 
        self.title = title 
        self.body = body 
 
def get_posts() -> list:
    post_amount = range(1,4)
    posts = []
    # Decode the JSON response into a Post instance
    for post_number in post_amount:
        # post_id is a number from 1 to max number of posts
        response = requests.get(f'https://jsonplaceholder.typicode.'
                                f'com/posts/{post_number}')
        post_data = json.loads(response.content)
        
        post = Post(userId=post_data["userId"], post_id=post_data["id"],
                    title=post_data["title"], body=post_data["body"])
        posts.append(post)
    return posts
    
def print_all_posts(posts_list:list):
    post_number = 1
    for post in posts_list:
        print(f'Post {post_number}:\n'
              f'     User ID: {post.userId}\n'
              f'     ID: {post.post_id}\n'
              f'     Title: {post.title}\n'
              f'     Body: {post.body}\n')
        post_number += 1
        
posts_list = get_posts()
print_all_posts(posts_list)








