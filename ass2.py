
# Q Reverse words of a string
#Example
#Input: "Python Means Programming"
#Output: "Programming Means Python"  
#Explaination:

s="Python Means Programming"

print(' '.join(s.split(' ')[::-1]))


#Q Check if two strings are anagrams or not?
#Example
#Input: "aaba" & "aaab"
#Output: Yes

#Input: "abcd" & "deba"
#Output: No

str1 =input("Input: ")
str2 =input()
flag=0
if len(str1)==len(str2):
    for ch in str1:
        if ch in str2:
            continue
        else:
            flag=1
            break
else:
    flag=1

if(flag==1):
    print("No")
else:
    print("Yes")


#Q check if a string is palindrome
#Example
#Input: hello-> olleh
#Output:  Not a palindrome

#Input: madam-> madam
#Output:  palindrome

#Explaination: Yes, if reversed string is same as original string
#Note: Try to use your own logic to find palindrome


str=input("Enter string")
if str==str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



#Q Input a string and find out duplicates alphabets

#Example
#Input: python at zenrays
#Output:  a,n
#Explaination: a & n both are repeating in the string

str= input("Enter string")
dup =set([i for i in str if str.count(i)>1])
print(dup)


#Q Count occurrences of a specific character in a String

str=input("Enter a string")
ch=input("Enter the character")
print(ch," : ",str.count(ch))



#Q Count occurrence of specific word in a String

str=input("Enter string")
wrd= input("Enter word")
print(str.count(wrd))



#Q Find out no of alphabets, lowercase, uppercase, vowels, consonants,
 #digits, spaces in a string


str=input("Enter string : ")
vowel ="aeiouAEIOU"
a=l=u=v=c=s=d=spch=0
for ch in str:
    if ch.isalpha():
        a+=1
        if ch.islower(): l+=1
        else:u+=1
        if ch in vowel:v+=1
        else:c+=1
    elif ch.isdigit():d+=1
    elif ch.isspace():s+=1
    else:spch+=1

print("alpha: ",a," lower: ",l," upper :",u," digit : ",d," space : ",s,
      "special : ",spch)


#Q Check if a string is a double string
#Example
#Input: "1221"
#Output: No

#Input: "abab"
#Output: Yes

#Input: "aaaaa"
#Output: No

#Input: "bbaabb"
#Output: No

#Explaination: 
#We call a string a "double string" if it has an even length and 
#the first half of this string is equal to the second half of this string

str=input("Enter string: ")
flag=0
if len(str)%2==0:
    n=len(str)//2
    if str[:n]==str[n:]:
        flag=1
if flag==0:
    print("No")
elif flag==1:
    print("Yes")
    





