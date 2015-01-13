'''Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB '''
    
def convertToTitle(num):
    ch = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    convertAux(num, ch, result)
    return ''.join(result)
        
def convertAux(num, ch, result):
    if num <= 26:
        result.append(ch[num])
        return
    if num % 26:
        convertAux(num/26, ch, result)
        result.append(ch[num%26])
    else:
        convertAux((num-1)/26, ch, result)
        result.append('Z')
        
if __name__ == '__main__':
    num = 52
    print convertToTitle(num)