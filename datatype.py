#set data type
set1= {"abc", 34, True, 40, "male"}
print(set1)
print(type(set1))

thisset = set(("apple", "banana", "cherry"))
print(thisset)

#dictionary data type
#key:value pair
dictionary ={
    "brand":"Ford",
    "model" : "Mustang",
    "year": 1964,
    "woner": "Bhaktapur Bsc CSIT Student"
}
print(dictionary)
print(dictionary["woner"])

#ranges of python to store the data
print(2**232)

#after deleting the variable and print the variable then it shows the variable isnot defined in the output
"""
counter = 100
print(counter)
del counter
print(counter)
"""
#multiple assignment is possible
a=b=c=100
print(a)
print(b)
print(c)

#python is the indent sensitive 
x=12
y=8
def sum(x,y):
    x=2
    sum=x+y
    print(x)
    return sum
print(sum(5,10))
print(x)


#Token
#complex number
value3 = 6+2.9j
print(value3)

#python hexadecimal literal
value4 = 0x12d
print(value4)

#Python octal literal 
value5= 0o021
print(value5)

#multiline literal
str2 = """Hello,
Its me manish shrestha
"""
print(str2)

#boolean literal 
a= (1== True)
b = (1 == False)
print(a)
print(b)

#Escape Sequence
txt = "We are the so-called \"Viking\" from the north."
print(txt)

#single quotes
txt = 'It\'s alright.'
print(txt)

#backslash
txt = "This will insert one \\."
print(txt)

txt = "Hello\n World!"
print(txt)

txt = "Hello\rWorld!"
print(txt)

x= -5
y=abs(x)
print(y)
z= 11
a= divmod(z,y)
print(a)

b=pow(y,y)
print(b)

b=pow(y,y,z)
print(b)

b=round(y,-4)
print(b)