import re
msg = "hello world"
stuff = re.findall('[aeiouAEIOU]+?', msg)
print(stuff)
