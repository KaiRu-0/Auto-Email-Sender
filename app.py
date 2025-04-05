from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'your_secret_key'

SENDER_EMAIL = 'sidharthravi2005@gmail.com'
APP_PASSWORD = 'lddy mpux ueej vaif'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        recipient_email = request.form['email']
        subject = request.form['subject']
        body = request.form['body']

        try:
            # 1. Send "Thanks" to the user
            thank_you_msg = EmailMessage()
            thank_you_msg['Subject'] = 'Thank you!'
            thank_you_msg['From'] = SENDER_EMAIL
            thank_you_msg['To'] = recipient_email
            thank_you_msg.set_content("Thanks")

            notify_msg = EmailMessage()
            notify_msg['Subject'] = f"New message: {subject}"
            notify_msg['From'] = SENDER_EMAIL
            notify_msg['To'] = SENDER_EMAIL
            notify_msg.set_content(f"New message from: {recipient_email}\n\n{body}")

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(SENDER_EMAIL, APP_PASSWORD)
                smtp.send_message(thank_you_msg)
                smtp.send_message(notify_msg)

            flash('Emails sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send emails: {e}', 'danger')

        return redirect('/')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
