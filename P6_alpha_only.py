str1 = input("Enter the string")
str2 = ""
for i in str1:
      if (ord(i)>= 65 and ord(i)<= 90) or (ord(i)>=97 and ord(i)<=122 ) :
           str2+=i
print("Alphabets in string are : " , str2)           
