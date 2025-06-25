from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Gmail SMTP Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'theachal123@gmail.com'       # 👉 Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'bvlr feie exxl nygt'          # 👉 Replace with 16-digit App Password
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Prepare email
    msg = Message(
        subject=f"New Contact Form Submission from {name}",
        recipients=[app.config['MAIL_USERNAME']],  # Your Gmail inbox
        body=f"""
        You received a new message from your portfolio website:

        Name: {name}
        Email: {email}
        Message:
        {message}
        """
    )

    try:
        mail.send(msg)
        flash("Thank you! Your message has been sent.")
    except Exception as e:
        print("Mail failed:", e)
        flash("Something went wrong. Please try again later.")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

