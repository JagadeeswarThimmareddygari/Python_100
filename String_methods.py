#string methods 
s1='hello, world!'

#calculate the length
print("Length of the string: ",len(s1))

#capitalized copy of the first letter of the string
print(s1.capitalize())

#to obtain the string of each world capitalized copy
print(s1.title())

#To obtain the copy of the string variable capital
print(s1.upper())

#To find the position of the substring in
print(s1.find('or'))
print(s1.find('jd')) #return -1 if not found
#similar to find but the exception is raised when substring is not found
print(s1.index('or'))
# print(s1.index('jd'))

#check if the string starts with specified string
print(s1.startswith('He')) #false
print(s1.startswith('he'))

#check if the string end with the specified string
print(s1.endswith('!'))

#center the string with the specified width and fill the specified color on both the sides
print(s1.center(50,'*'))

#put the string to the right of the specified width and fill the specified color on the left
print(s1.rjust(50,'*'))

#put the string to the left of the specified width and fill the specified color on the right
print(s1.ljust(50,'*'))

s2='abc13563'

#check whether the string is of numbers
print(s2.isdigit())

#check whether the string of of characters
print(s2.isalpha())

#check if the string is of numbers and letters constituting
print(s2.isalnum())

s3='jackfrued123@gmail.com'
print(s3)
#get the copy after trimming the left and right spaces of the string
print(s3.strip())
