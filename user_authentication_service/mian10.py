#!/usr/bin/env python3
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.create_session(email))           # Nümunə: '5a006849-343e-4a48-ba4e-bbd523fcca58'
print(auth.create_session("unknown@email.com"))  # None
