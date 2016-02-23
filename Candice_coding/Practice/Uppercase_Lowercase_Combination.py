# Given a string with only numbers and lowercase characters, return all the possible combinations lowercase, uppercase and number.
# e.g. input: 'ab3d2'; output: ['ab3d2', 'Ab3d2', 'aB3d2', 'ab3D2', 'AB3d2', 'Ab3D2', 'aB3D2', 'AB3D2']

def upperLowerCombination(s):
    results = set([])
    upperLowerCombinationHelper(s, [], results)
    return list(results)

def upperLowerCombinationHelper(s, tmpResult, results):
    if not s:
        word = ''.join(tmpResult)
        if word not in results:
            results.add(word)
        return
    tmpResult.append(s[0])
    upperLowerCombinationHelper(s[1:], tmpResult, results)
    tmpResult.pop()
    tmpResult.append(s[0].upper())
    upperLowerCombinationHelper(s[1:], tmpResult, results)
    tmpResult.pop()
    return


if __name__ == '__main__':
    s = 'ab3d2'
    print upperLowerCombination(s)
    s = '3b2'
    print upperLowerCombination(s)
    s = 'abb'
    print upperLowerCombination(s)
    s = 'abba'
    print upperLowerCombination(s)