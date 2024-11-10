# Save this script as darkai.py
import random

def generate_code(language, task):
    # Example responses for various languages and tasks
    code_snippets = {
        "python": {
            "calculator": """
def calculator():
    operation = input("Enter operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        print(num1 / num2)
    else:
        print("Invalid operation")
calculator()
            """,
            "fibonacci": """
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
fibonacci(10)
            """
        },
        "html": {
            "login_form": """
<!DOCTYPE html>
<html>
<head>
    <title>Login Form</title>
</head>
<body>
    <form action="/login" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
            """,
            "table": """
<!DOCTYPE html>
<html>
<head>
    <title>Sample Table</title>
</head>
<body>
    <table border="1">
        <tr>
            <th>Name</th>
            <th>Age</th>
        </tr>
        <tr>
            <td>John</td>
            <td>30</td>
        </tr>
        <tr>
            <td>Jane</td>
            <td>25</td>
        </tr>
    </table>
</body>
</html>
            """
        },
        "javascript": {
            "alert_button": """
<!DOCTYPE html>
<html>
<head>
    <title>Alert Button</title>
</head>
<body>
    <button onclick="showAlert()">Click Me</button>

    <script>
        function showAlert() {
            alert("Hello, this is an alert!");
        }
    </script>
</body>
</html>
            """
        },
        "css": {
            "basic_style": """
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    color: #333;
}

h1 {
    color: #0056b3;
}
            """
        }
    }
    
    # Select a code snippet based on language and task
    return code_snippets.get(language, {}).get(task, "Sorry, I don't have that code snippet.")

def main():
    print("Welcome to DarkAI Code Generator!")
    print("You can generate code in Python, HTML, JavaScript, CSS.")
    
    while True:
        language = input("Enter the language (python, html, javascript, css) or 'quit' to exit: ").lower()
        if language == 'quit':
            break
        task = input(f"What type of {language} code would you like to generate? ").lower()
        
        code = generate_code(language, task)
        print("\nGenerated Code:\n")
        print(code)
        print("\n")

if __name__ == "__main__":
    main()
