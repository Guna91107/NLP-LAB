import re

text = "My email is test@gmail.com"

pattern = r'\S+@\S+'

result = re.findall(pattern, text)

print("Found email:", result)