# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel.
# The black pixels are connected, i.e., there is only one black region.
# Pixels are connected horizontally and vertically.
# Given the location (x, y) of one of the black pixels, 
# return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
# For example, given the following image:
# [
#   "0010",
#   "0110",
#   "0100"
# ]
# 
# 
# and x = 0, y = 2,
# Return 6.


class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        # Using Binary Search to find the top, bottom, left, right borders.
        top = self.findBoarder(0, x, image, lambda x: '1' in image[x])
        bottom = self.findBoarder(x, len(image)-1, image, lambda x: '1' not in image[x])
        left = self.findBoarder(0, y, image, lambda y: any(row[y]=='1' for row in image))
        right = self.findBoarder(y, len(image[0])-1, image, lambda y: all(row[y]=='0' for row in image))
        # any and all are built-in functions in python.
        return (bottom - top) * (right - left)

    def findBoarder(self, low, high, image, checkFunc):
        while low <= high:
            middle = (low + high) / 2
            if checkFunc(middle):
                high = middle - 1
            else:
                low = middle + 1
        return low


if __name__ == '__main__':
    image = ["0010", "0110", "0100"]
    x, y = 0, 2
    print Solution().minArea(image, x, y)