print("hello world")
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Dummy user credentials for demonstration
USER_CREDENTIALS = {'username': 'admin', 'password': 'admin123'}

# HTML Template with Inline CSS
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clinic Homepage</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 50px;
            text-align: center;
        }
        h1 {
            color: #2c3e50;
        }
        .btn {
            background-color: #3498db;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #2980b9;
        }
        .error {
            color: red;
        }
        form input {
            padding: 10px;
            margin: 5px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        form button {
            background-color: #3498db;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        form button:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        {% if not username %}
            <h1>Welcome to Our Clinic</h1>
            <p>Your health is our priority. Please sign in to access the clinic portal.</p>
            <a href="{{ url_for('sign_in') }}" class="btn">Sign In</a>
        {% else %}
            <h1>Welcome, {{ username }}!</h1>
            <p>Welcome to the clinic's dashboard.</p>
            <a href="/" class="btn">Logout</a>
        {% endif %}
    </div>

    {% if request.endpoint == 'sign_in' %}
        <div class="container">
            <h1>Sign In to Your Account</h1>
            {% if error %}
                <p class="error">{{ error }}</p>
            {% endif %}
            <form method="POST">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required><br><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required><br><br>
                <button type="submit" class="btn">Sign In</button>
            </form>
        </div>
    {% endif %}
</body>
</html>
'''


