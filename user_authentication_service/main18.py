#!/usr/bin/env python3
from auth import Auth

auth = Auth()
user = auth.register_user("bob@bob.com", "OldPwd")

token = auth.get_reset_password_token("bob@bob.com")
print("Token:", token)

auth.update_password(token, "NewPwd")

# Login with new password should succeed
print(auth.valid_login("bob@bob.com", "NewPwd"))  # True

# Old password should fail
print(auth.valid_login("bob@bob.com", "OldPwd"))  # False
