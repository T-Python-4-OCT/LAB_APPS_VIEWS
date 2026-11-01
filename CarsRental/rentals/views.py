from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string

def home_view(request: HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def about_view(request: HttpRequest):
    content = "A simple paragraph about Car Rentals."
    return HttpResponse(content)

def password_generator_view(request: HttpRequest):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(10))
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <title>مولد كلمه السر</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background-color: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 400px;
                width: 100%;
            }}
            .password-box {{
                font-size: 22px;
                font-weight: bold;
                letter-spacing: 2px;
                color: #2c3e50;
                background-color: #eef2f7;
                padding: 15px;
                border-radius: 8px;
                margin: 20px 0;
                word-break: break-all;
            }}
            .btn {{
                background-color: #007bff;
                color: white;
                border: none;
                padding: 12px 25px;
                font-size: 16px;
                border-radius: 6px;
                cursor: pointer;
                transition: 0.3s;
            }}
            .btn:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🔑 مولد كلمات المرور</h2>
            <div class="password-box">{password}</div>
            <button class="btn" onclick="window.location.reload();">توليد كلمة سر جديدة 🔄</button>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)