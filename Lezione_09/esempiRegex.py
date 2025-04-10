import re
text:str = "my Email is lucadambra422@gmail.com"
result:list[str] = re.findall(r'\S+@\S+',text)
print(result)