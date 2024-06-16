# Email Sender

This project is a simple Python script for sending emails using yagmail. It allows you to send emails with attachments and customize the email content.

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/email-sender.git
   ```

2. Install the required dependencies:

   ```sh
   pip install yagmail keyring
   ```

3. Set up your email address and app password:

   Run the script for the first time.
   It will prompt you to enter your email address and app password. This information will be saved securely in a .env file.
   Note: Make sure to enable "Less secure app access" in your Gmail settings and use an app password for security.

4. Run the script:
   ```
   python send_email.py
   ```

This project is licensed under the MIT License - see the LICENSE file for details.
