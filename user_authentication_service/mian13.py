#!/usr/bin/env python3
from auth import Auth

auth = Auth()
user = auth.register_user("bob@bob.com", "MyPwdOfBob")
session_id = auth.create_session("bob@bob.com")
print(auth.get_user_from_session_id(session_id).email)  # bob@bob.com

auth.destroy_session(user.id)
print(auth.get_user_from_session_id(session_id))       # None
