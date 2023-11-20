#Password maker
import random
i = 0
char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
leng = int(input("Longitud de la contraseña: "))
password = ""
while i < leng:
    pas = random.choice(char)
    password += pas
    i += 1
print(password)