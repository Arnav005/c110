#mean

import csv
with open('height-weight.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
    #print(file_data)
    file_data.pop(0)
    print(file_data)
    new_data=[]
    for i in range(len(file_data)):
        n_num=file_data[i][1]
        new_data.append(float(n_num))
        
        #getting the mean
n=len(new_data)
total=0
for x in new_data:
    total+=x

mean=total/n
print( "mean " +str(mean))


#median

import csv
with open('height-weight.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
    #print(file_data)
    file_data.pop(0)
    print(file_data)
    new_data=[]
    for i in range(len(file_data)):
        n_num=file_data[i][1]
        new_data.append(float(n_num))
        
        #getting the median
n=len(new_data)
new_data.sort()

#using floor division to get the nearest number whole number

if n % 2 == 0 :
    #getting the first number
    median1 = float(new_data[n//2])
    #getting the second number
    median2 = (new_data[n//2])
    #getting the maean of these number
    median = (median1+median2) / 2
else:
    median=new_data[n//2]
    print(n)

print("Median is -> " + str(median))
    




