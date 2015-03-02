'''
find all the int coordinates of a circle without using sqrt, sin, cos, etc'''
'''hints: we can divide the circle into 8 pieces and we only need to focus
the 0~45 degree piece.'''

def findDots(a, b, r):
    result = [(a,r+b), (r+a,b), (a,b-r), (a-r,b)]
    x = 1+a
    while x-a < 0.8*r:
        y = r+b
        while y-b >= x-a:
            if (x-a)**2+(y-b)**2 == r*r:
                result.append((x, y))
                result.append((x, -y))
                result.append((-x, y))
                result.append((-x, -y))
                result.append((y, x))
                result.append((y, -x))
                result.append((-y, x))
                result.append((-y, -x))
                break
            y -= 1
        x += 1
    return result

if __name__ == '__main__':
    test_case = [1,2,3,4,5]
    a = 1
    b = 2
    for r in test_case:
        print findDots(a, b, r)
        
        
        