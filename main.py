class finder:
    def find_pair(self,numbers, target):
        seen = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                return (seen[diff],i)
            seen[num] = i

numbers = (10,20,30,40,50,60,70,80)
target = int(input("Enter number:"))

result = finder().find_pair(numbers, target)

if result:
    print("the positions of pairs:", result[0],"and",result[1])
else:
    print("no pair found!")