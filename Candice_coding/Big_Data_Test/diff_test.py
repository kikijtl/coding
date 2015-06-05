#from mrjob.job import MRJob

def mapper(file):
    f = open(file, 'r')
    data = f.read()
    lines = data.splitlines()
    f.close()
    output = "D:\COEN242ProjectTest\small_diff_map.txt"
    diff_tb = {}
    for line in lines:
        if line != '':  #this might be replace by .strip() to remove whitespaces in head and tail
            k_v = line.split()
            uid = k_v[0]
            ratings = k_v[1].strip()
            ratings = ratings.split(',')    #A list of movie:rating items for one user
            for item_i in ratings:
                mv_i, rating_i = item_i.split(':')[0], item_i.split(':')[1]
                for item_j in ratings:
                    mv_j, rating_j = item_j.split(':')[0], item_j.split(':')[1]
                    if (mv_i, mv_j) not in diff_tb:
                        diff_tb[(mv_i, mv_j)] = int(rating_i)-int(rating_j)
            for diff in diff_tb:
                #print '%s:%s' % (diff, diff_tb[diff])
                #This is the output of the mapper
                #key is (mv_i, mv_j), value is rating_ui-rating_uj
                with open(output, 'a') as out:
                    out.write('%s:%s\n' % (diff, diff_tb[diff]))
                    out.close()
            diff_tb = {}
    return output
    
            

from math import sqrt

def reducer(file):
    f = open(file, 'r')
    data = f.read()
    data = data.strip()
    lines = data.splitlines()
    diff_tb = {}
    for line in lines:
        k_v = line.split(':')
        key = k_v[0]
        key = key.strip('()')
        key = tuple(key.split(', '))
        #Now we have the key of [mv_i, mv_j]
        value = k_v[1]
        #value = value.strip('()')
        #value = value.split(', ')
        #Now we have the value of Rui-Ruj
        if key not in diff_tb:
            diff_tb[key] = [int(value), 1]
        else:
            diff_tb[key][0] += int(value)   #Diff sum
            diff_tb[key][1] += 1   #Diff count
            #sim_tb[key][2] += float(value[1])*float(value[1])   #Second Lower part
    for key in diff_tb:
        diff = diff_tb[key][0] / float(diff_tb[key][1])
        #print "(%s,%s):%s" % (key[0], key[1], diff)
        with open('D:\COEN242ProjectTest\small_diff_reduce.txt', 'a') as out:
            out.write("(%s,%s):%s\n" % (key[0], key[1], diff))
        out.close()
    print 'Done!'
    


if __name__ == '__main__':
    map_input = 'D:\COEN242ProjectTest\small_input.txt'
    '''
    map_input = 'D:\COEN242ProjectTest\ExStep1Output.txt'
    '''
    map_out = mapper(map_input)
    
    #map_out = 'D:\COEN242ProjectTest\small_diff_map.txt'
    reduce_input = map_out
    reducer(reduce_input)
    
    