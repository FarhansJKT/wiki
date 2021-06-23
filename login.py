import os
import time

banner = """
LOGIN SIMPLE ( LU BISA UBAH APA AE NI)
""" # UBAH AJA INI TAMPILANNYA

pw = "FHANS" # UBAH AJA CUK PASSWORD NYA

print(banner)
p = input("[+] PASSWORD : ")
if p == pw:
   os.system("clear")
   os.system("login")
else :
   print("[!] PASSWORD SALAH!!")
   time.sleep(1)
   os.system("clear")
   os.system("python3 login.py")
