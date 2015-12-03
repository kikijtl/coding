# The API: int read4(char *buf) reads 4 characters at a time from a file.
# 
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
# 
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
# 
# Note:
# The read function may be called multiple times.


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buffer_q = collections.deque([])
        # Used to store charaters that are read by read4 by not returned by readN
        self.ended = False
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if not n: return 0
        read_bytes = len(self.buffer_q)
        for i in xrange(min(read_bytes, n)):
            buf[i] = self.buffer_q.popleft()
        tmp_buffer = ['' for i in xrange(4)]
        while read_bytes < n and not self.ended:
            bytes = read4(tmp_buffer)
            if bytes < 4:
                self.ended = True
            buf_range = min(n, read_bytes+bytes)
            for i in xrange(read_bytes, buf_range):
                buf[i] = tmp_buffer[i-read_bytes]
            if read_bytes + bytes > n:
                for i in xrange(read_bytes+bytes-n, 0, -1):
                    self.buffer_q.append(tmp_buffer[bytes-i])
            read_bytes += bytes
        return min(read_bytes, n)
                
                