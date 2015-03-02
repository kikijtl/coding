'''Given a number, return whether it is a happy number or not.'''

def happyNum(n):
    dic = {}
    while n != 1 and n not in dic:
        '''We found that unhappy num will end up with 4'''
        '''So the while condition can be n!=1 and n!=4'''
        sum = 0
        dic[n] = 0
        while n > 0:
            sum += (n%10)**2
            n /= 10
        n = sum
    if n == 1:
        return True
    else:
        return False
    

if __name__ == '__main__':
   for i in range(1, 30, 2):
       print (i, happyNum(i)),
       
'''       
def pureNum(n):
    dic = {}
    while n != 1 and n not in dic:
        sum = 0
        dic[n] = 0
        while n > 0:
            sum += n%10
            n /= 10
        n = sum**2
    if n == 1:
        return True
    else:
        return False
    
if __name__ == '__main__':
    for i in range(1, 30, 3):
        print (i, pureNum(i)),
        
'''