d = {"a": 1}
e = {"b": 2}
d["m"] = 10   

#  Method 1  
"""if key m will exist in dictionary d 
then value of the m will be updated by the 10
otherwise a new key-value pair will be added to the dictionary"""
print(d)

#  Method 2
e["b"] = 50
print(e)

#  Method 3
d.update(e)
print(d)