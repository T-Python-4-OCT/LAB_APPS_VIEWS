from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.

def homepage(request):
    return HttpResponse("""
        <div style="
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 150px;
        ">
            <h1 style="color: #2563eb;">
                Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.
            </h1>

            <a href="/about/">About Us</a>
            |
            <a href="/password/generate/">Password Generator</a>
        </div>
    """)

def about(request):
    return HttpResponse("""
        <div style="
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 150px auto;
            max-width: 650px;
        ">
            <h1 style="color: #2563eb;">About CarsRental</h1>

            <p style="
                font-size: 18px;
                color: #475569;
                line-height: 1.8;
            ">
                Welcome to CarsRental! We provide reliable, affordable,
                and convenient car rental services to make your journey
                easier. Whether you're traveling for business or leisure,
                our goal is to help you find the perfect car for your needs.
            </p>

            <a href="/">Back to Home</a>
        </div>
    """)

def randomly_generated_password(request):
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Password Generator | CarsRental</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f1f5f9;
                min-height: 100vh;
                margin: 0;
                display: flex;
                align-items: center;
                justify-content: center;
            }}

            .card {{
                background: white;
                padding: 45px;
                width: 420px;
                max-width: 85%;
                border-radius: 16px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            }}

            h1 {{
                color: #2563eb;
                margin-bottom: 12px;
            }}

            p {{
                color: #64748b;
                line-height: 1.6;
            }}

            .password {{
                background: #eff6ff;
                color: #1d4ed8;
                padding: 20px;
                border: 1px solid #bfdbfe;
                border-radius: 10px;
                font-size: 23px;
                font-weight: bold;
                letter-spacing: 2px;
                margin: 25px 0;
                overflow-wrap: anywhere;
                font-family: monospace;
            }}

            .buttons {{
                display: flex;
                gap: 10px;
                justify-content: center;
                flex-wrap: wrap;
            }}

            .btn {{
                padding: 12px 20px;
                border-radius: 8px;
                text-decoration: none;
                font-size: 14px;
                font-weight: bold;
                transition: 0.2s;
            }}

            .primary {{
                background: #2563eb;
                color: white;
            }}

            .secondary {{
                background: #e2e8f0;
                color: #334155;
            }}

            .btn:hover {{
                opacity: 0.85;
            }}
        </style>
    </head>

    <body>
        <div class="card">
            <h1>Password Generator</h1>

            <p>Generate a random 10-character password.</p>

            <div class="password">{password}</div>

            <div class="buttons">
                <a href="/password/generate/" class="btn primary">
                    Generate Again
                </a>

                <a href="/" class="btn secondary">
                    Back to Home
                </a>
            </div>
        </div>
    </body>
    </html>""")