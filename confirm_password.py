import keyring

# Retrieve the password stored for the given service and username
service_name = "yagmail"
username = "gal.oiring@gmail.com"
stored_password = keyring.get_password(service_name, username)

if stored_password:
    print(f"Password found for {username}: {stored_password}")
else:
    print(f"No password found for {username}")
