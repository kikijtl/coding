# Google Engineering Residency Program
# Find all the abbreviations for a word.
# Extension of the abbreviation method of Leetcode 288
# The abbreviation can happen at any part of the word.
# Hint: A letter can itself or 1.
# Combine all the consecutive 1s together to be a number.


def allAbbr(word):
    results = []
    dfs(word, [], results)
    return results

def dfs(word, tmpResult, results):
    if not word:
        results.append(combine(tmpResult))
        return
    for letter in [word[0], '1']:
        tmpResult.append(letter)
        dfs(word[1:], tmpResult, results)
        tmpResult.pop()

def combine(tmpResult):
    abbr = ''
    count = 0
    for i in xrange(len(tmpResult)):
        if i == 0 and tmpResult[i] != '1':
            abbr += tmpResult[i]
        elif i == 0:
            count += 1
            continue
        else:
            if tmpResult[i] == tmpResult[i-1] == '1':
                count += 1
            elif tmpResult[i] == '1':
                count += 1
            elif count != 0:
                abbr += str(count)
                count = 0
                abbr += tmpResult[i]
            else:
                abbr += tmpResult[i]
    if count != 0:
        abbr += str(count)
    return abbr

if __name__ == '__main__':
    word = 'home'
    print allAbbr(word)