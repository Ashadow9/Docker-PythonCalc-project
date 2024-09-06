from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def hello():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Docker Course with Calculator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f4f4;
            }
            .container {
                text-align: center;
                background: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 800px;
            }
            .header {
                margin-bottom: 20px;
            }
            .title {
                color: #0044cc;
                font-weight: bold;
                font-size: 24px;
                font-family: 'Berlin Sans FB', sans-serif;
            }
            .subtitle {
                font-style: italic;
                color: #000;
                font-family: 'Times New Roman', Times, serif;
            }
            .name {
                font-weight: bold;
                font-size: 24px;
                font-family: 'Pacifico', cursive;
            }
            .message {
                font-style: italic;
                margin-bottom: 10px;
            }
            .button {
                display: inline-block;
                padding: 10px 20px;
                margin: 10px;
                font-size: 16px;
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
                display: flex;
                align-items: center;
            }
            .docker-button {
                background-color: #0db7ed;
            }
            .linkedin-button {
                background-color: #0077b5;
            }
            .footer {
                margin-top: 20px;
                font-family: 'Times New Roman', Times, serif;
            }
            .profile-pic {
                position: absolute;
                bottom: 10px;
                right: 10px;
                border-radius: 50%;
                width: 120px;
                height: 120px;
            }
            .calculator {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 10px;
                max-width: 200px;
                margin: 20px auto;
            }
            .calculator input {
                grid-column: span 4;
                padding: 10px;
                font-size: 18px;
            }
            .calculator button {
                padding: 15px;
                font-size: 18px;
                border: none;
                background-color: #e0e0e0;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .calculator button:hover {
                background-color: #d0d0d0;
            }
        </style>
        <script>
            function appendValue(value) {
                document.getElementById('result').value += value;
            }
            function clearResult() {
                document.getElementById('result').value = '';
            }
            function calculate() {
                let result = eval(document.getElementById('result').value);
                document.getElementById('result').value = result;
            }
        </script>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="bold">Welcome Everyone,</div>
                <div class="message">Here's a simple calculator for you!</div>
            </div>
            <div class="calculator">
                <input type="text" id="result" readonly>
                <button onclick="appendValue('7')">7</button>
                <button onclick="appendValue('8')">8</button>
                <button onclick="appendValue('9')">9</button>
                <button onclick="appendValue('/')">/</button>
                <button onclick="appendValue('4')">4</button>
                <button onclick="appendValue('5')">5</button>
                <button onclick="appendValue('6')">6</button>
                <button onclick="appendValue('*')">*</button>
                <button onclick="appendValue('1')">1</button>
                <button onclick="appendValue('2')">2</button>
                <button onclick="appendValue('3')">3</button>
                <button onclick="appendValue('-')">-</button>
                <button onclick="appendValue('0')">0</button>
                <button onclick="appendValue('.')">.</button>
                <button onclick="clearResult()">C</button>
                <button onclick="appendValue('+')">+</button>
                <button onclick="calculate()" style="grid-column: span 4;">=</button>
            </div>
            <div class="footer">
                Enjoy your session!<br>
                &copy; Docker Basics to Brilliance
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
