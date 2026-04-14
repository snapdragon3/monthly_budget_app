# Write a function that prints a greeting.

# def greet():
#     print("Hey, Good afternoon! What's up!")
    
# greet()

# Write a function that takes a name as input and prints “Hello, [name]”.

# def tag():
#     name = input("What's your name: ")
#     print(f"Hello, {name}")
    
# tag()

# Write a function that adds two numbers and returns the result.
# def add():
#     x = int(input("What's x? "))
#     y = int(input("What's y? "))
#     return x + y

# results=add()

# print(f"The sum of the inputted figure is {results}")


# Write a function that multiply two numbers and returns the result.

# Write the four functions

# add() → asks for two numbers, returns their sum.

# subtract() → asks for two numbers, returns their difference.

# multiply() → asks for two numbers, returns their product.

# divide() → asks for two numbers, returns their quotient (but handle division by zero).
# print("================================")
# print("Menu Calculator")
# print("================================")

# def add():
#     x = int(input("What's x? "))
#     y = int(input("What's y? "))
#     return x + y

# def subtract():
#     x = int(input("What's x? "))
#     y = int(input("What's y? "))
#     return x - y

# def multiply():
#     x = int(input("What's x? "))
#     y = int(input("What's y? "))
#     return x * y

# def divide():
#     x = int(input("What's x? "))
#     y = int(input("What's y? "))
#     if y == 0:
#         return "Error: Cannot divide by zero"
#     return x / y

# Create Menu
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")
# print("5. Exit")

# option = int(input("Choose your option: "))

# # Use an if or match block
# # If the user chooses 1, call add().
# # If they choose 2, call subtract().
# # If they choose 3, call multiply().
# # If they choose 4, call divide().

# if option == 1:
#     print("Addition:",add())
# elif option == 2:
#     print(subtract())
# elif option== 3:
#     print(multiply())
# elif option==4:
#     print(divide())
# elif option==5:
#     print("Exiting program....")
# else:
#     print("Wrong Input, Re-run the program")

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# NumPy: create some sample data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # features
y = np.array([2, 4, 6, 8, 10])  # target

# Pandas: put data into a DataFrame
df = pd.DataFrame({'X': x.flatten(), 'Y': y})
print("DataFrame:\n", df)

# Scikit-Learn: train a simple linear regression model
model = LinearRegression()
model.fit(x, y)

# Predict new values
predictions = model.predict(np.array([[6], [7]]))
print("Predictions for X=6 and X=7:", predictions)








