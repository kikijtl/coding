'''
find all the int coordinates of a circle without using sqrt, sin, cos, etc'''
'''hints: we can divide the circle into 8 pieces and we only need to focus
the 0~45 degree piece.'''

def drawCircle(r):
    m = [[' ' for i in range(r*2+1)] for j in range(r*2+1)]
    x = 0
    while x < 0.8*r:
        y = r
        while x <= y:
            if (x-r)**2 + (y-r)**2 == r**2:
                m[x][y] = '*'
                m[y][x] = '*'
                m[x][2*r-y] = '*'
                m[y][2*r-x] = '*'
                m[2*r-x][2*r-y] = '*'
                m[2*r-x][y] = '*'
                m[2*r-y][x] = '*'
                m[2*r-y][2*r-x] = '*'
                break
            y -= 1
        x += 1
    return m


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
    '''
    for r in test_case:
        print findDots(a, b, r)
    '''
    r = 7
    m = drawCircle(r)
    for row in m:
        for dot in row:
            print dot,
        print    
        
        