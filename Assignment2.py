# To print the numbers which are divisible by 7 when the starting and ending numbers are given
a=int(input("Enter the starting number : "))
b=int(input("Enter the ending number : "))
for i in range(a, b+1) :
    if (i%7 == 0) :  # if the remainder is zero then the number is divisible by 7
        print (i)


# To check the prime numbers in a list
# c=int(input("Enter the starting number : "))
# d=int(input("Enter the ending number : "))
list4=[1,2,4,13,30,19,70,80,100]
a=[]
for i in list4:
    count=0
   # if (i>1) :
    for j in range(1, i) :
        if (i%j)==0 :
            count=count+1
    else :
        if (count==1) :
            a.append(i)
            print(a)


# To print all the prime numbers when starting and ending numbers are given
c=int(input("Enter the starting number : "))
d=int(input("Enter the ending number : "))
for count in range(c, d+1) :
    if (count>1) :
        for i in range(2,count) :
            if (count%i)==0 :
                break
        else :
            print(count)


# To convert even characters to uppercase and odd characters to lower case
String = "jktechtraining"
print("The original string is :", String)
result = " "
for i in range(len(String)) :
    if (i%2):   # if not (i%2) - it converts even characters to lower case and odd characters to upper case
        result = result + String[i].upper()
    else :
        result = result + String[i].lower()
print("The updated string is :", result)


# Counts the total number of words in the given sentence
sentence = "Begin your day with beautiful smile "
words = len(sentence.split())
print("Total number of words in the given sentence is : ", words)

