from flask import Flask, request

app = Flask(__name__)

# Questions aur unke options
questions = [
    {"q": "Python kya hai?", "a": "Language", "b": "Snake", "ans": "a"},
    {"q": "Website ke liye kya use hota hai?", "a": "Flask", "b": "Free Fire", "ans": "a"},
    {"q": "Variable kya hai?", "a": "Ek Box", "b": "Error", "ans": "a"},
    {"q": "User input ke liye command?", "a": "take()", "b": "input()", "ans": "b"},
    {"q": "GitHub kiske liye hai?", "a": "Code save karne", "b": "Chatting", "ans": "a"},
    {"q": "Render kya karta hai?", "a": "Live website", "b": "Game khelna", "ans": "a"},
    {"q": "Coding kahan likhte hain?", "a": "WhatsApp", "b": "Editor/Pydroid", "ans": "b"},
    {"q": "Aapka naam kya hai?", "a": "Jenish", "b": "Rahul", "ans": "a"}
]

@app.route('/')
def home():
    html = "<h1>Welcome to Jenish's Mega Quiz!</h1><p>Niche sawaalon ke jawab dein:</p><form action='/result' method='POST'>"
    for i, q in enumerate(questions):
        html += f"<p>{i+1}. {q['q']}<br>"
        html += f"<input type='radio' name='q{i}' value='a'> {q['a']} <br>"
        html += f"<input type='radio' name='q{i}' value='b'> {q['b']} </p>"
    html += "<button type='submit'>Check Score</button></form>"
    return html

@app.route('/result', methods=['POST'])
def result():
    score = 0
    for i, q in enumerate(questions):
        user_ans = request.form.get(f'q{i}')
        if user_ans == q['ans']:
            score += 1
    return f"<h1>Jenish, aapka score hai: {score}/8</h1><a href='/'>Wapas koshish karein</a>"

if __name__ == "__main__":
    app.run()
