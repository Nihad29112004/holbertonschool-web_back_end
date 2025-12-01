user = my_db.add_user("test@test.com", "hashedPwd")
print(user.id)

my_db.update_user(user.id, hashed_password="NewPwd")
print("Password updated")
