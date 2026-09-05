text=input().replace(" ","")
lowest_count = len(text)
for char in text:
    current_count = text.count(char)
    if current_count < lowest_count:
        lowest_count = current_count
result = ""
for char in text:
    if text.count(char) == lowest_count:
        if char not in result:
            result = result + char
print(result)