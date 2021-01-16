#1 Examples of string
# String is a set of character -> "kush"

print("Hello, world")

name = "kush"
print(name)

name2 ="Hi my name is # kush"
print(name2)
-------------------------------------------------------------------

# How to print "Quotes" inside a Quotes

#1 -> using backlash(\). This is also known as escape

name3 = "How to print \"Quotes\" inside a Quote"
print(name3)

#2 -> change double quotes to single or vica versa

name3 = 'How to print "Quotes" inside a Quot'
print(name3)
--------------------------------------------------------------------

# 2 How to check a data type

# type() function for checking data type

name = "sam"
print(type(name))           # <class 'str'>

print(type("kush"))         # <class 'str'>

number = 9
print(type(number))         # <class 'int'>
----------------------------------------------------------------------

# 3 how to check length of a Strings

# len() is use for checking length of a string

name_length = len("kushagra")
print(name_length)              # ->8

name = "kushagra"
print(len(name))
-----------------------------------------------------------------------

#4 how to print string in a new line

#1 ->use \n
print("My name is \nkush\n")

#2 ->Uing triple quotes (""" or ''')
print ("""my name
is
kushagra""")
----------------------------------------------------------------------

#5 String Concatenation

string1="abra"
string2="cadabra"
magic_string= string1 + string2
print(magic_string)

# inbetween spaces
string1="abra"
string2="cadabra"
magic_string= string1 + " " + string2
print(magic_string)
----------------------------------------------------------------------

#6 String Indexing

    #  k u s h a g r a    -> len =8
    #  0 1 2 3 4 5 6 7

name = "kushagra"
print(name[1])      # -> u

#print(namee[9]) -> IndexError: string index out of range

#negative indexing
    #  k  u  s  h  a  g  r  a
    # -8 -7 -6 -5 -4 -3 -2 -1

print(name[-1])     #-> a

# print(namee[-10]) -> IndexError: string index out of range

# Checking total index of any String variable
total_index = len(name) -1
--------------------------------------------------------------------

# 7 String slicing

name = "kushagra"
name3 = name[1] + name[2] + name[3]

#best way
print(name[0:3])      #->kus

print(name[ :3])      #->kus

print(name[3:])       #->hagra

print(name[:])        #->kushagra
--------------------------------------------------------------------

#8 Empty string

empty_string = ""
non_empty_string1 = " "


# 9 cannot assign character at particular index

pen = "blue"
# pen[0] ="g"->TypeError:'str'object does not support item assignment

pen = "g" + pen[ 1 :]     #>glue
print(pen)
---------------------------------------------------------------------

# 10 Manipulating String with Method
    #1 lowercase

print("KuSh".lower())    #->kush

name = "KuSh".lower()    #->kush
print(name)

name1 ="kush"
name2 =name1.lower()   #-> saving it to a variable because this will return a copy which we are saving in variable
print(name2)             #->kush

    #2 uppercase
print("kush".upper())    #->KUSH

namee = "KuSh".upper()    #->KUSH
print(namee)

name4 ="kush"
name5 = name4.upper()
print(name5)             #->KUSH

#3  To remove whitespace
name = "kush    "
print(name.rstrip())      #->kush


name = "    kush"
print(name.lstrip())       #->kush

name = "    kush     "
print(name.strip())        #->kush


#4 startswith()   endswith()

name ="kush"
new_name =name.startswith("k")  #->true  will be store in new_variable
print(new_name)

new_name =name.endswith("d")       #->false
print(new_name)

-------------------------------------------------------------------
