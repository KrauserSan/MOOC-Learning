#find sum of all the numbers from the txt file 
import re
handle = open("ActualDataWeek2.txt",'r')
total = 0
for line in handle:
    nums = re.findall('[0-9]+',line)
    if len(nums)>=1:
        for x in nums:
            total = total + int(x)
print(total)
