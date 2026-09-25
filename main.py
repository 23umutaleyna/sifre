import random

karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre=""

sifre_uzunlugu=int(input("şifreniz kaç haneli olsun?"))

for i in range(sifre_uzunlugu):
    secilen_karakter=random.choice(karakterler)
    sifre+=secilen_karakter

print("şifreniz:",sifre)   
