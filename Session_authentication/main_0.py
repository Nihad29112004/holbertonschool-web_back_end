#!/usr/bin/env python3
import base64
from models.user import User

user_email = "bob@hbtn.io"
user_clear_pwd = "H0lbertonSchool98!"

user = User()
user.email = user_email
user.password = user_clear_pwd
user.save()

basic = "{}:{}".format(user_email, user_clear_pwd)
print("Basic Base64:", base64.b64encode(basic.encode("utf-8")).decode("utf-8"))
