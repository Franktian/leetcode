def isHappy(n):
   ht = {}
   while n != 1 and not ht.get(n):
      ht[n] = 1
      n = getSumSquare(n)
   return n == 1

def getSumSquare(n):
   res = 0
   while n > 0:
      digit = n % 10
      res += digit ** 2
      n /= 10
   return res