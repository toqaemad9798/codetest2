# vulnerable_app.py
username = input("Enter your username: ")
query = "SELECT * FROM users WHERE name = '" + username + "'"
print("Running query:", query)
# vulnerable_script.py

user_input = input("Enter a math expression: ")
result = eval(user_input)
print(f"The result is: {result}")
