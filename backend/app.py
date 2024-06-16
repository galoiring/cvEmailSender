from flask import Flask, jsonify, request
import yagmail
import os

app = Flask(__name__)

default_body = """
Hi !
I'm emailing because I'm interested in Software Developer jobs at your company.
I'm a highly motivated Full Stack Developer with experience in Python, React, and other popular technologies like Django REST and Git.
I've attached my resume for you to look at, and I'd love to chat about new opportunities.
Gal
p.s
Attached here my portfolio website:
http://Gal-oiring.netlify.app
"""

default_attachment_path = 'Gal Oiring.pdf'


@app.route('/default_data', methods=['GET'])
def get_default_data():
    default_data = {
        'body': default_body,
        'attachmentPath': default_attachment_path
    }
    return jsonify(default_data)


@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    body = data.get('body')
    title = data.get('title')

    # Send email using yagmail
    yag = yagmail.SMTP(email, password)
    yag.send(to=email, subject=title, contents=body)

    return 'Email sent successfully!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
