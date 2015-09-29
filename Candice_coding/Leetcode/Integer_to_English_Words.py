class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        words = []
        unit = ["", "Thousand", "Million", "Billion"]
        for i in range(len(unit)-1, -1, -1):
            divider = 1000 ** i
            if num / divider:
                subword = self._numberToWordsHelper(num / divider)
                words.append('{} {}'.format(subword, unit[i]))
                num = num % divider
        return ' '.join(words)
    
    def _numberToWordsHelper(self, num):
        subwords = []
        dict = {0: "Zero", 1:"One", 2: "Two", 3: "Three", 4: "Four", \
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", \
                  10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
                  15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", \
                  20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", \
                  70: "Seventy", 80: "Eighty", 90: "Ninety"}
        if num / 100:
            subwords.append('{} Hundred'.format(dict[num/100]))
            num = num % 100
            if num == 0: return ' '.join(subwords)
        if num / 10 <= 1:
            subwords.append('{}'.format(dict[num]))
            return ' '.join(subwords)
        subwords.append('{}'.format(dict[num / 10 * 10]))
        num = num % 10
        if num == 0: return ' '.join(subwords)
        subwords.append('{}'.format(dict[num]))
        return ' '.join(subwords)


if __name__ == '__main__':
    print Solution()._numberToWordsHelper(2)