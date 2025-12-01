user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

print(my_db.find_user_by(email="test@test.com").id)

try:
    my_db.find_user_by(email="nope@test.com")
except NoResultFound:
    print("Not found")

try:
    my_db.find_user_by(no_email="test@test.com")
except InvalidRequestError:
    print("Invalid")
