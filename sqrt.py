

'''
 16-> 4
 17->4

 start from 0 to n
find mid btwn start and n

mid*mid=n
    return mid
if mid*mid>n:
    end=mid-1
else
    start=mid+1

start+(end-start)//2

10

3.1*3.1 =
'''



'''

'''
def sqrt(num):
    if num <= 1:
        return num

    start=0
    end=num

    while start < end:

        mid=start+(end-start)//2
        square=mid**2

        if square == num:
            return mid

        elif square < num:
            start=mid+1

        else:
            
            end=mid
            
    return start-1
'''
start 0  0  3  3 
end   10 5   5 4
mid    5  2  4  3
'''
    # return int(mid)

# print(sqrt(0))

'''
two string

s1 and s2

car and rac arc
 carr 
 arck

return true or false

'''

def anagram(s1,s2):

    if len(s1) != len(s2):
        return False
    
    myDict={}
    

    for elem in s1:
        if len(s2) > 0:
            position=s2.find(elem)
            if  position != -1:
                s2=s2[:position]+s2[position+1:]

            else:
                return False
        else:
            return False
    
    return len(s2)==0
        
    # s1=sorted(s1) #O(n)
    # s2=sorted(s2) 

    #O(nlogn)
    
def anagram1(s1,s2):

    if len(s1) != len(s2):
        return False
    
    myDict={}
    
    for elem in s1:
        if elem not in myDict:
            myDict[elem] = 1

        else:
            myDict[elem] += 1

    for char in s1:
        
        if char in myDict:

            if myDict[char] == 1:
                myDict.pop(char)

            else:
                myDict[char] -=1
                
        else:
       
            return False
    
    return True

print(anagram1("fairyll b taleso","rail safety boll"))
    

