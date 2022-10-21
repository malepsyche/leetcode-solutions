# Get indices of 2 values that add up to target
nums = [2,7,11,15]
target = 18

dictionary = dict(enumerate(nums))

def getindices():
          for a in nums:
                    for b in nums:
                              if a+b == target:
                                        indice = [key for key in dictionary if dictionary[key] == a]
                                        indice1 = [key for key in dictionary if dictionary[key] == b]
          return indice+indice1
          
print(getindices())