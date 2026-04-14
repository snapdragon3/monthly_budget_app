#Ask the user their name
# name = input("What's your name? ").strip().title()

#Say hello to the user
# print("hello" ,name, "\nHow's it going?")
# print("hello, ", end="")
# print(name)

# #Using the f-string
# # print(f"Hello {name} + You're too good")

# """
# This is a multi-line comment
# """
# # Split user's name into first name and last name
# first, last = name.split(" ")


# print(f"Hello, {last}")


# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z= int(x)+int(y)

# z = round(x / y, 2)
# z = x /y 

# print(z)

# print(f"{z:.2f}")

# print(x + y)
# print=round(1[ 2])



#Functions

# def main():
#     name = input("What's your name? ")
#     hello(name)
    
# def hello(to="world"):
#     print("hello,", to)
    

# main()

# def chat(to):
#     print(f"You're my love, {to}")

# chat("This message")


# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")
    
    
# greet("Mosh", "Hamedani")
# greet("Adam", "Latif")


# def greet(name):
#     print(f"Hi {name}")
    
# print(greet("Mosh"))
    
    
# def get_greeting(name):
#     return f"Hi {name}"    

# message = get_greeting("Mosh")
# file = open("content.txt", "w")
# file.write(message)


# def increment(number, by=1):
#     return number + by

# print(increment(number=2,by=1))


# def multiply(*numbers):
#     print(numbers)
#     return x * y

# multiply(2,3,4,5)


#CONDITIONS
# x = int(input("What's x?"))
# y = int(input("What's y?"))

# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")


# score = int(input("Score: "))

# if score>=90:
#     print("Grade: A")
# elif score>=80:
#     print("Grade: B")
# elif score>=70:
#     print("Grade: C")
# elif score>=60:
#     print("Grade: D")
# else:
#     print("Grade: F")


# def main():
#     x = int(input("Whats x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")
        
# def is_even(n):
#     # if n%2==0:
#     #     return True
    
#     # else:
#     #     return False
    
#     # return True if n % 2 == 0 else False
#     return n % 2 == 0
    
# main()


# name = input("Whats your name? ")

# if name == "Harry" or name=="Hermione" or name=="Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")


# match name:
#     case "Harry" | "Hermione" | "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")
        
        
# Algorithm for Daily Mood Tracker
# Start the program

# Display a welcome message (e.g., “Welcome to Mood Tracker”).

# Show menu options

# Example:

# Add today’s mood

# View past moods

# Exit

# Get user choice

# Ask the user to type a number (1, 2, or 3).

# If choice = Add mood

# Ask the user: “How do you feel today?”

# Capture the input (e.g., “Happy”).

# Get today’s date (using Python’s datetime).

# Store the mood + date in a list or dictionary.

# If choice = View moods

# Loop through the stored moods.

# Print each entry with its date (e.g., “2026-04-05: Happy”).

# If choice = Exit

# Print a goodbye message.

# End the program.

# Repeat steps 2–6 until user exits

# Use a loop so the program keeps running until the user chooses Exit.

# print("===========================")
# print("Welcome to Mood Tracker")
# print("===========================")

# option_1 = int(input("1. Add today’s mood"))
# option_2 = int(input("2. view past moods"))
# option_3 = int(input("3. Exit"))


# if option_1 == 1:
# # Ask the user: “How do you feel today?”
#     print("How do you feel today? ")
# # Capture the input (e.g., “Happy”).
#     choice_1 = int(input("1. Excited"))
#     chioce_2 = int(input("2. Neutral"))
#     choice_3 = int(input("2. Sad"))

# from datetime import date

# today = date.today()

# moods = []
# moods.append({"date": today, "mood": "Excited"})
  
# if choice_1==1:
    



from datetime import date   # Import the date class to get today’s date

moods = []   # Create an empty list to store mood entries

print("===========================")   # Print a decorative line
print("Welcome to Mood Tracker")      # Print the welcome message
print("===========================")   # Print another decorative line

while True:   # Start an infinite loop so the app keeps running until you exit
    print("\nChoose an option:")        # Show the menu options
    print("1. Add today’s mood")        # Option 1: Add a mood
    print("2. View past moods")         # Option 2: View stored moods
    print("3. Exit")                    # Option 3: Exit the program

    choice = input("Enter your choice: ")   # Ask the user to type a choice

    if choice == "1":   # If the user chooses option 1
        print("\nHow do you feel today?")   # Ask for today’s mood
        print("1. Excited")                 # Mood option 1
        print("2. Neutral")                 # Mood option 2
        print("3. Sad")                     # Mood option 3

        mood_choice = input("Enter your mood number: ")   # Get the user’s mood choice

        if mood_choice == "1":   # If user picked 1
            mood = "Excited"     # Set mood to Excited
        elif mood_choice == "2": # If user picked 2
            mood = "Neutral"     # Set mood to Neutral
        elif mood_choice == "3": # If user picked 3
            mood = "Sad"         # Set mood to Sad
        else:                    # If user typed something invalid
            print("Invalid mood choice.")   # Show error message
            continue                        # Skip back to the menu

        today = date.today()   # Get today’s date
        moods.append({"date": str(today), "mood": mood})   # Store date + mood in the list
        print(f"Mood saved: {mood} on {today}")   # Confirm to the user

    elif choice == "2":   # If the user chooses option 2
        if not moods:     # Check if the list is empty
            print("\nNo moods recorded yet.")   # Tell user no moods exist
        else:             # If there are moods stored
            print("\nYour past moods:")         # Print header
            for entry in moods:                 # Loop through each mood entry
                print(f"{entry['date']}: {entry['mood']}")   # Print date and mood

    elif choice == "3":   # If the user chooses option 3
        print("Goodbye!") # Print exit message
        break             # Break the loop to end the program

    else:                 # If the user typed something invalid
        print("Invalid choice, try again.")   # Show error message