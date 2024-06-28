from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        strength = check_password_strength(password)
        return render_template('user.html', strength=strength)
    return render_template('user.html')

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in '!@#$%^&*(),.?":{}|<>' for char in password):
        score += 1
    
    if score == 0 or score == 1:
        return 'Weak'
    elif score == 2:
        return 'Medium'
    elif score == 3:
        return 'Strong'
    else:
        return 'Very Strong'

if __name__ == '__main__':
    app.run(debug=True)