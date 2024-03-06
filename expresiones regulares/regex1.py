import re

text='The quick brown fox jumps over the lazy dog'

first_end = re.findall("^The.*dog$", text) 
# busca que inicie con ^The, . todo monos saltos en linea, * afecta al carácter anterior y trae 0 o más ocurrencias, y que termine en dog $


if first_end:
    print("SI")
    print(first_end)
else:
    print("NO")
    print(first_end)