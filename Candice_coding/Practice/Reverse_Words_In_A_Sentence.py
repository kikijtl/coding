# Enter your code here. Read input from STDIN. Print output to STDOUT
def reverseWords(sentence):
    sentenceList = sentence.split(' ')
    sentenceList.reverse()
    return ' '.join(sentenceList)



if __name__ == '__main__':
    sentence = raw_input()
    print reverseWords(sentence)