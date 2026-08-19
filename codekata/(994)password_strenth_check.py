password=input("ENTER PASSWORD :")
has_alpha=False
has_digit=False
has_special=False
for check in password :
    if check.isalpha():
        has_alpha=True
    elif check.isdigit():
        has_digit=True
    else:
        has_special=True
if (len(password)<8):
    print("Weak password")
elif has_alpha and has_digit and has_special:
    print("Strong Password")
elif has_alpha and has_digit:
    print("Medium Password")
else:
    print("Weak Password")