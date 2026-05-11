from itertools import accumulate
from typing import List


def runningSum(nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
        

# print(runningSum([1, 2, 3, 4]))

# print(list(accumulate([1, 2, 3, 4])))  one line solution



def getConcatenation(nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
            print("nums[i]",nums[i])
        return nums
      
# print(getConcatenation([1, 2, 3,1]))

# 1 2 3 1 1 2 3 1



#   For Single Element  
def singleNumber(nums: List[int]) -> int:
        countArr = []

        for i in range(len(nums)):
            indexCount = 0
            for j in range(len(nums)):
                if(nums[i] == nums[j]):
                    indexCount +=1
            countArr.append(indexCount)

        
        print(countArr)

        for i in range(len(countArr)):
          if countArr[i] == 1:
            return nums[i]

#   For Single Element  
# def singleNumber(nums: List[int]) -> int:
#         result = 0

#         for i in range(len(nums)):
#             result ^= nums[i]
#         return result

# def singleNumber(self, nums: List[int]) -> List[int]:
#         from collections import Counter
#         freq = Counter(nums)
#         return [num for num in nums if freq[num] == 1][0]
            
# print(singleNumber([2, 2, 1,3,1]))


# Forst returning array of ellemt whose elements has  1 frequency
def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        return [num for num in nums if freq[num] == 1]

print(singleNumber([2, 2, 1,3,1]))