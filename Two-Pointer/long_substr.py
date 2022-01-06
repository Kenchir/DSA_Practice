

from typing import List


def solution(arr:List[int]) ->int:
    sum =0
    for i in arr:
        sum += i
    return sum

print(solution([10,20,-30]))

