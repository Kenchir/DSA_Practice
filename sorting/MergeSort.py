

'''
Worst-case performance	 O(nlogn)
space : O(n)
'''
def MergeSort(arr):
    
    if len(arr)<=1: 
        return arr

    middle = len(arr) // 2
    left = MergeSort(arr[:middle])
    right = MergeSort(arr[middle:])
    
    return merge(left,right)


def merge(left,right):
    result=[]
  
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left.pop(0))

        else:
            result.append(right.pop(0))
          
    for item in right:
        result.append(item)

    for item in left:
        result.append(item)
  
    # print(result)
    return result

# print("result:  ",MergeSort([8,1,2,3,4,6,5,12,7]))
assert [1,2,3,4,5,6,7,8,45]==MergeSort([1,45,2,3,4,6,8,5,7])
assert [2,31,90,119,125,234,685]==MergeSort([685,119,90,234,2,125,31])
assert [1,2,3]==MergeSort([3,1,2])

'''
def mergeSort(arr : List[int]) -> List[int]:

  n = len(arr)
  if n  == 1:
    return arr
  
  mid = n // 2
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])

  return merge(left, right)

def merge(left : List[int], right : List[int]) -> List[int]:

  i, j, a , b, result = 0,0, len(left), len(right),[]

  while i < a  and  j < b :

    if left[i] < right[j]:
      result.append(left[i])
      i += 1

    else :
      result.append(right[j])
      j += 1
 
  while j < b:
    result.append(right[j])
    j += 1
  
  while i < a:        
    result.append(left[i])
    i += 1

  return result

'''