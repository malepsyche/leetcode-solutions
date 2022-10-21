#https://leetcode.com/problems/valid-parentheses/
                
s = ['(',')',')',')']
stack = []

a = {')':'(', ']':'[', '}':'{'}
def returnboolean():
          for b in s:
                    if b not in a:
                              stack.append(b)
                    elif stack and a[b] == stack[-1]:
                              stack.pop()
                    else:
                              return False

          return stack == []

print(returnboolean())