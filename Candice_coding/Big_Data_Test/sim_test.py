#from mrjob.job import MRJob

def mapper(file):
    f = open(file, 'r')
    data = f.read()
    lines = data.splitlines()
    f.close()
    output = "D:\COEN242ProjectTest\small_sim_map.txt"
    sim_tb = {}
    for line in lines:
        if line != '':  #this might be replace by .strip() to remove whitespaces in head and tail
            k_v = line.split()
            uid = k_v[0]
            ratings = k_v[1].strip()
            ratings = ratings.split(',')    #A list of movie:rating items for one user
            rate_sum = 0
            for item_i in ratings:
                mv_i, rating_i = item_i.split(':')[0], item_i.split(':')[1]
                rate_sum += int(item_i[-1])
                for item_j in ratings:
                    mv_j, rating_j = item_j.split(':')[0], item_j.split(':')[1]
                    if (mv_i, mv_j) not in sim_tb:
                        sim_tb[(mv_i, mv_j)] = (int(rating_i), int(rating_j))
            rate_avg = rate_sum / float(len(ratings))
            for sim in sim_tb:
                #print '%s:%s' % (sim, (sim_tb[sim][0]-rate_avg, sim_tb[sim][1]-rate_avg))
                #This is the output of the mapper
                #key is (mv_i, mv_j), value is (rating_ui-rating_u, rating_uj-rating_u)
                with open(output, 'a') as out:
                    out.write('%s:%s\n' % (sim, (sim_tb[sim][0]-rate_avg, sim_tb[sim][1]-rate_avg)))
                out.close()
            sim_tb = {}
    return output
    
            

from math import sqrt

def reducer(file):
    f = open(file, 'r')
    data = f.read()
    data = data.strip()
    lines = data.splitlines()
    sim_tb = {}
    for line in lines:
        k_v = line.split(':')
        key = k_v[0]
        key = key.strip('()')
        key = tuple(key.split(', '))
        #Now we have the key of [mv_i, mv_j]
        value = k_v[1]
        value = value.strip('()')
        value = value.split(', ')
        #Now we have the value of [Rui-Ru, Ruj-Ru]
        if key not in sim_tb:
            sim_tb[key] = [float(value[0])*float(value[1]), 
                           float(value[0])*float(value[0]), float(value[1])*float(value[1])]
        else:
            sim_tb[key][0] += float(value[0])*float(value[1])   #Upper part
            sim_tb[key][1] += float(value[0])*float(value[0])   #First Lower part
            sim_tb[key][2] += float(value[1])*float(value[1])   #Second Lower part
    for key in sim_tb:
        if sim_tb[key][1] == float(0) or sim_tb[key][2] == float(0):
            continue
        sim = sim_tb[key][0] / sqrt(sim_tb[key][1]) /sqrt(sim_tb[key][2])
        #print "(%s,%s):%f" % (key[0], key[1], sim)
        with open('D:\COEN242ProjectTest\small_sim_reduce.txt', 'a') as out:
            out.write("(%s,%s):%s\n" % (key[0], key[1], sim))
        out.close()
    print 'Done!'
    


if __name__ == '__main__':
    
    map_input = 'D:\COEN242ProjectTest\small_input.txt'
    map_out = mapper(map_input)
    
    #reduce_input = "D:\COEN242ProjectTest\ExStep2Map.txt"
    reducer(map_out)
    
    