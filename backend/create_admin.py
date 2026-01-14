''' contrasena del usuario administrado
user Admin
pass 1234


from app.auth.hash import hash_password

print(hash_password("1234"))
'''