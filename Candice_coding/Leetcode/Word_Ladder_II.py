# Given two words (beginWord and endWord), and a dictionary's word list, 
# find all shortest transformation sequence(s) from beginWord to endWord, such that:
# 
# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,
# 
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.

import collections

class Solution(object):
    def findLadders(self, start, end, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        if start==end:
            return []
        d = set(wordlist)
        q = collections.deque()
        visited = set()
        q.append(start)
        visited.add(start)
        min_len = float('inf')
        # string <=> [prev strings]
        path_map = {}
        path_map[start], path_map[end] = [[start]], []
        while q:
            s=q.popleft()
            # i is each position in s
            for i in xrange(len(s)):
                # try to replace the curr_pos with chr(97+j)
                for j in xrange(26):
                    tmp = list(s)
                    tmp[i] = chr(97+j)
                    tmp = ''.join(tmp)
                    if tmp == end:
                        for previous_path in path_map[s]:
                            if len(previous_path)+1 > min_len:
                                return path_map[end]
                            min_len = len(previous_path) + 1
                            path_map[end].append(previous_path+[end])
                    elif tmp in d and tmp not in visited:
                        q.append(tmp)
                        visited.add(tmp)
                        if tmp not in path_map:
                            path_map[tmp] = []
                        for previous_path in path_map[s]:
                            path_map[tmp].append(previous_path+[tmp])
        return path_map[end]

if __name__ == '__main__':
    start = "nape"
    end = "mild"
    wordlist = ["dose","ends","dine","jars","prow","soap","guns","hops","cray",
                "hove","ella","hour","lens","jive","wiry","earl","mara","part",
                "flue","putt","rory","bull","york","ruts","lily","vamp","bask",
                "peer","boat","dens","lyre","jets","wide","rile","boos","down",
                "path","onyx","mows","toke","soto","dork","nape","mans","loin",
                "jots","male","sits","minn","sale","pets","hugo","woke","suds",
                "rugs","vole","warp","mite","pews","lips","pals","nigh","sulk",
                "vice","clod","iowa","gibe","shad","carl","huns","coot","sera",
                "mils","rose","orly","ford","void","time","eloy","risk","veep",
                "reps","dolt","hens","tray","melt","rung","rich","saga","lust",
                "yews","rode","many","cods","rape","last","tile","nosy","take",
                "nope","toni","bank","jock","jody","diss","nips","bake","lima",
                "wore","kins","cult","hart","wuss","tale","sing","lake","bogy",
                "wigs","kari","magi","bass","pent","tost","fops","bags","duns",
                "will","tart","drug","gale","mold","disk","spay","hows","naps",
                "puss","gina","kara","zorn","boll","cams","boas","rave","sets",
                "lego","hays","judy","chap","live","bahs","ohio","nibs","cuts",
                "pups","data","kate","rump","hews","mary","stow","fang","bolt",
                "rues","mesh","mice","rise","rant","dune","jell","laws","jove",
                "bode","sung","nils","vila","mode","hued","cell","fies","swat",
                "wags","nate","wist","honk","goth","told","oise","wail","tels",
                "sore","hunk","mate","luke","tore","bond","bast","vows","ripe",
                "fond","benz","firs","zeds","wary","baas","wins","pair","tags",
                "cost","woes","buns","lend","bops","code","eddy","siva","oops",
                "toed","bale","hutu","jolt","rife","darn","tape","bold","cope",
                "cake","wisp","vats","wave","hems","bill","cord","pert","type",
                "kroc","ucla","albs","yoko","silt","pock","drub","puny","fads",
                "mull","pray","mole","talc","east","slay","jamb","mill","dung",
                "jack","lynx","nome","leos","lade","sana","tike","cali","toge",
                "pled","mile","mass","leon","sloe","lube","kans","cory","burs",
                "race","toss","mild","tops","maze","city","sadr","bays","poet",
                "volt","laze","gold","zuni","shea","gags","fist","ping","pope",
                "cora","yaks","cosy","foci","plan","colo","hume","yowl","craw",
                "pied","toga","lobs","love","lode","duds","bled","juts","gabs",
                "fink","rock","pant","wipe","pele","suez","nina","ring","okra",
                "warm","lyle","gape","bead","lead","jane","oink","ware","zibo",
                "inns","mope","hang","made","fobs","gamy","fort","peak","gill",
                "dino","dina","tier"]
    print Solution().findLadders(start, end, wordlist)