# To convert epoch modified datetime to normal time
import os
import datetime

file_name = 'File2.txt'
if os.path.exists(file_name):
    print('file exists')
    m_time = os.path.getmtime(file_name)
    dt_m = datetime.datetime.fromtimestamp(m_time)
    print('modifiled time is {}'.format(m_time))
    c_time = os.path.getctime(file_name)
    dt_c = datetime.datetime.fromtimestamp(c_time)
    print('created time is {}'.format(dt_c))
else:
    print('no file with that name')


# To print all data from the file
file_name1 = open('File2.txt','r')
content = file_name1.read()
print("The data in the file are : ", content)
file_name1.close()


# To print the total number of lines in the file
with open("File2.txt",'r') as fp :
    lines = len(fp.readlines())
    print("The total number of lines in the file is :", lines)


# To print the total number of characters in a file
with open("File2.txt", 'r') as fp :
    characters = len(fp.read())
    print("The total number of characters in the file is :", characters)


# To print the most recent modification time of the file
with open("File2.txt", 'r') as fp :
    m_time = os.path.getmtime(file_name)
    dt_m = datetime.datetime.fromtimestamp(m_time)
    print("The most recent modifiled time is {}".format(m_time))


# To print the file size
file_size = os.path.getsize("File2.txt")
print("File size is :", file_size, "KiloBytes")


# To print the file name
import os
file_path = 'C:/Users/Rachana.Giliyal/PycharmProjects/pythonProject1/File1.txt'
file_name = os.path.basename(file_path)
print("File name is:", file_name)
