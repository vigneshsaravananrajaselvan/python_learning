import string
sentence="python ai python ml ai python data science"
cleanes_semtence=sentence.translate(str.maketrans("", "", string.punctuation))
word=sentence.split()
count={}
longest=max(count,key=len)
print(longest)
