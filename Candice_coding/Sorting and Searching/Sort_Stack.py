''' Sort a stack in ascending order. Only one addional stack can be used'''

def sortStack(st1):
    st2 = []
    while st1:
        tmp = st1.pop()
        while st2 and st2[-1] < tmp:
            st1.append(st2.pop())
        st2.append(tmp)
    return st2


if __name__ == '__main__':
    st1 = [4,5,1,2,3,5,7,8,3,5,6,7,8,9,0,3,4,5]
    st2 = sortStack(st1)
    print st2