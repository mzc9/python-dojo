#to find out the datatype of a variable
print(type("Tonya Harding"))

#case changes
print("tonya".upper())

#find if a particular string terminates with a particular string value
print("entire string with multiple values".endswith("values"))

#to get help for strings
help(str)


#creating strings in python
"this entry will be considered a string"

#care about double and single quotes
'I'm using a single quote' # will lead to error

#correct format for the above
"Now I'm ready to use the single quotes inside a string!"

#strings in python are a sequence, so they can be accessed via index
#STRINGS ARE IMMUTABLE


#strings are a sequence, so can use index to find specific parts of the strings
s = "whatchamacallit"
s[0] # ->'w'
s[-1] # -> last letter
s[:: -1] #-> reverse string
s[::2] # grab all but go up in steps of 2
