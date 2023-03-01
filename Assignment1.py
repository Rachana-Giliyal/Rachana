# To print the largest and smallest numbers from the given three numbers
a=int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number : "))
c=int(input("Enter the 3rd number : "))
if(a>b) :
    print("The largest of three numbers is the 1st number :", a)
elif(b>c) :
    print("The largest of three numbers is the 2nd number : ",b)
else :
    print("The largest of three numbers is the 3rd number : ",c)
if(a<b):
    print("The smallest of three numbers is the 1st number :", a)
elif(b<c):
    print("The smallest of three numbers is the 2nd number :", b)
else :
    print("The smallest of three numbers is the 3rd number :", c)


#To print the largest, smallest and second-largest numbers from the given list
list5 = [12,34,65,87,98,23,124,6]
print("The given list is : ", list5)
list5.sort()
print("The largest number in the given list is : ", max(list5)) # To find the largest number in the list
print("The smallest number in the given l;ist is : ",min(list5)) # To find the smallest number in the list
print("The second largest number in the given list is : ",list5[-2]) # To find the second-largest number in the list


# To remove the 2nd index from the list ( List starts from index zero)
List1=[1,2,1,1,4,5]
removed_element=List1.pop(2)
print("List1 : ",List1)
print("Removed Element : ", removed_element)
print("Updated List : ", List1)


# To delete the second occurrence of 1 from the list
a=[1,2,1,1,4,5]
remove_element=1
count=0
for i in range(0,len(a)-1) :
    if (remove_element==a[i]) :
        count=count+1
        if(count==2):
            del a[i]
            break
print(a)


# To delete the 3rd, 6th and 4th index from the list
List2 = [1,4,10,30,60,70,80,100]
print("list2 : ", List2)
Deleted_index_list=List2.pop(3)  # deletes the 3rd index ie, 30
print("Deleted List : ", Deleted_index_list)
print("Updated List : ", List2)
Deleted_index_list=List2.pop(6)  # deletes the 6th index ie, 100
print("Deleted List : ", Deleted_index_list)
print("Updated List : ", List2)
Deleted_index_list=List2.pop(4)  # deletes the 4th index ie, 70
print("Deleted List : ", Deleted_index_list)
print("Updated List : ", List2)


# To delete 3rd, 7th and 4th index from the list
List2 = [1,4,10,30,60,70,80,100]
b=[3,7,4]
for i in sorted(b, reverse=True) :    # sort the given list
    del List2[i]
print(List2)


# To reverse a string
string = "JKTech"
print(string[::-1])


# Checks whether the string has 2 or more vowels and if so then, prints true
String = "thought"
def rev_string(string):
    rev_string = String[::-1]   # To reverse a string
    return rev_string
rev_string_var = rev_string(String)
print(rev_string_var)

def is_two_vowels_present(rev_string_var):
    list1=['a','e','i','o','u']  # vowels list
    #list1.count(2)
    count=0
    for each_character in rev_string_var :   # checks each character in the reversed string
        if each_character in list1 :
            count = count + 1

    if (count>=2) :     # if the count is greater than or equal to 2 then returns true else false
        print("Contains 2 vowels")
        return True
    else :
        print("Does not contain vowels")
        return False

two_vowels_present = is_two_vowels_present(rev_string_var)
print(two_vowels_present)
