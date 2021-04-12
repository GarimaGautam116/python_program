def ispalindrome(s) :
        return  s==s[ : : -1]
s = input ("Enter :")
ans = ispalindrome(s)
if ans:
        print("Palindrome")
else :
        print("Not Palindrome")
        
