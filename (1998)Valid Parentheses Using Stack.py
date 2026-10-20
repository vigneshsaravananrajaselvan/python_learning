braket_string = input().strip()
while "[]" in braket_string or "{}" in braket_string or "()" in braket_string:
    braket_string = braket_string.replace("[]","")
    braket_string = braket_string.replace("{}","")
    braket_string = braket_string.replace("()","")
if len(braket_string) == 0 :
    print("Balanced")
else:
    print("Not Balanced")