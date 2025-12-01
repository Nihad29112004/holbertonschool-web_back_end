#!/usr/bin/env python3
from auth import Auth

auth = Auth()
auth.register_user("bob@bob.com", "MyPwdOfBob")

token = auth.get_reset_password_token("bob@bob.com")
print(token)  # Nümunə çıxış: 'd290f1ee-6c54-4b01-90e6-d701748f0851'

# Invalid user
try:
    auth.get_reset_password_token("unknown@email.com")
except ValueError as e:
    print(e)  # No user found with email: unknown@email.com
