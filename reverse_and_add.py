#Reverse list and add up the individual integers to form a number
l1 = [2,4,3,9,9]
l2 = [5,6,4,9,9]

def reverselist(list):
          if len(list) == 1:
                    return list
          else:
                    reversedlist = reverselist(list[1:]) + [list[0]]
                    return reversedlist

l3 = reverselist(l1)
l4 = reverselist(l2)
sum = int(''.join(map(str,l3))) + int(''.join(map(str,l4)))
print(sum)