import yagmail
import os


def send_email(to_address, attachment_path, body):
    # Initialize the yagmail.SMTP object with the email
    yag = yagmail.SMTP('gal.oiring@gmail.com')

    # Email content
    subject = 'Gal Oiring - Software Developer CV'

    # Send the email
    try:
        yag.send(
            to=to_address,
            subject=subject,
            contents=body,
            attachments=attachment_path
        )
        # \033[92m is the ANSI escape code for green color
        print("\033[92mEmail sent successfully!\033[0m")
    except Exception as e:
        print(f"Failed to send email: {e}")


def main():
    attachment_path = 'Gal Oiring.pdf'  # Path to the CV file in the same folder
    body = """
    Hi !

    I'm emailing because I'm interested in Software Developer jobs at your company.

    I'm a highly motivated Full Stack Developer with experience in Python, React, and other popular technologies like Django REST and Git. 
    I've attached my resume for you to look at, and I'd love to chat about new opportunities.

    Gal

    p.s
    Attached here my portfolio website: 
        http://Gal-oiring.netlify.app
    """

    try:
        while True:
            to_address = input("Enter the recipient's email address: ")
            print("\nEmail content:")
            print(body)
            confirm = input(
                f"\nSend this email to {to_address}? (y/n): ").strip().lower()
            if confirm == 'y':
                send_email(to_address, attachment_path, body)

            # Loop back to the email input step
            print("Enter another recipient's email address or press Ctrl+C to exit.")
    except KeyboardInterrupt:
        print("\nExiting the email sender. Goodbye!")
        exit()


if __name__ == "__main__":
    main()
