# First Python Lesson 

# Lets write first code :) 

print('Hello World') # 'print' function writes the input of the function on terminal 

# We use "#" to open a comment line, this line will be ignored by program 
# Determining a variable is very simple on Python, Python can understand the type of variable.
# Lets determine a variable in type of integer named "a" equal to 2 
# Integer variable type is named "Tam sayi" in Turkish, decimal part of integers is "0" 
a = 2 # int 
# We can print the variable we determined 
print(a) 

# In Python we can check the type of variables with a simple "type" function 
# This function takes variables as input and returns the type of variable 
# When we print this function, we can see the returned value of this function 
print(type(a))

# Another variable type is "float" which includes decimal parts after point 
# We should consider about that every integer number is also a float number but not every float number is an integer
# For example 20 is an integer number but also has decimal part 20 = 20.000000 as we can imagine 
b= 2.2 #float 
print(type(b))



# Another variable type is "string" 
# The type of variable that contains the fonts is called a string.
# We use "" symbol to write characthers as string 
c = "UBN-Jr Python Class" #string 
print(type(c))
print(c) 


# One of the most important varibale type is Boolean type
# Boolean type is a logical varibale type that can keep just two different values "TRUE" or "FALSE"
# This type mostly used for conditionals 
# TRUE means condition happend and FALSE means condition does not happend 
# We can just see this is a simple approach for now but latter we will see this data type much more detailed 
d = True #boolean 
print(type(d)) 
# 1-0 ifadesidir 
print(d) 

e = False #boolean
print(type(e))
print(e)

# Mathematical Operators 
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y



# Now lets look at the usage of print function 
ubn = int = 45 
print(ubn) 

print(c, "Merhaba UBN - Jr ", a, b, d, e, ubn)

deger1 = 2
deger2 = 3
print(deger1 + deger2) 

a = input("Lutfen bir sayi giriniz: ") 

print(a) 



cumle = str
cumle = input("Lutfen bir cumle giriniz: ") 

print(cumle) 



# Python average 

vize = input("Lutfen vize notunuzu giriniz: ")
final = input("Lutfen final notunuzu giriniz: ")



finalortalama = float(final) * 0.6
vizeortalama = float(vize) * 0.4


ortalama = finalortalama + vizeortalama 
print(ortalama) 


# Sartli ifadeler ve donguler 



