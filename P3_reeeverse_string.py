def reverse(str):
                    if len(str)==0 :
                        return str
                    else :
                        return reverse(str[1: ]) + str[0]

string=input("enter the string")
print("The given string is : " , string)
print("The reversed string is : " , reverse(string))
