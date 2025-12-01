#!/usr/bin/env python3
from auth import Auth

auth = Auth()
user = auth.register_user("bob@bob.com", "MyPwdOfBob")

session_id = auth.create_session("bob@bob.com")

# Valid session
print(auth.get_user_from_session_id(session_id).email)  # bob@bob.com

# Invalid session
print(auth.get_user_from_session_id("fake_session"))   # None

# None session
print(auth.get_user_from_session_id(None))             # None
