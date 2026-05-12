from collections import Counter
from typing import List

def isDuplicate(nums: List[int]):
    frequency = Counter(nums)

    isDuplicate = False

    for num in nums:
        if frequency[num] > 1:
            isDuplicate = True
            break
    return isDuplicate

# print(isDuplicate([1, 2, 3, 4,3]))




# def valid(s: str, t: str):


