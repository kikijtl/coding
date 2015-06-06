
def recommender(sim, orig_rt):
    sim_f = open(sim, 'r')
    sim_rc = sim_f.read()
    sim_lines = sim_rc.strip()  #remove whitespaces in head and tail
    sim_lines = sim_lines.splitlines()
    sim_f.close()
    #output = 'D:\COEN242ProjectTest\RecommendLs.txt'
    sim_tb = {}
    #Store all the similarity in sim_tb
    for line in sim_lines:
        #The input line format is: key_mv mv1:sim1,mv2:sim2,...
        k_v = line.split()  #Split line using whitespaces. Now k_v is a list: [key, value]
        mv_i = k_v[0]
        sim_ls = k_v[1]
        sim_ls = sim_ls.strip().split(',')
        for item in sim_ls:
            mv_j, sim = item.strip().split(':')[0], item.strip().split(':')[1]
            if (mv_i, mv_j) not in sim_tb and round(float(sim), 4) < 1.0:   #The condition may be changed
                sim_tb[(mv_i, mv_j)] = round(float(sim), 4)
                #print sim_tb[(mv_i,mv_j)]
    #Now we have the sim_tb
    orig_f = open(orig_rt, 'r')
    orig_rc = orig_f.read()
    orig_lines = orig_rc.strip()
    orig_lines = orig_lines.splitlines()
    orig_f.close()
    rt_tb = {}
    rec_ls = []
    for line in orig_lines:
        #The input line format is: uid mv1:rating1,mv2:rating2,...
        if line == '':
            continue
        k_v = line.split()
        uid = k_v[0]
        orig_ratings = k_v[1].strip()
        orig_ratings = orig_ratings.split(',')
        n = len(orig_ratings)
        for item_i in orig_ratings:
            mv_i, rating_i = item_i.split(':')[0], item_i.split(':')[1]
            
            mv_i = '000000' + mv_i
            mv_i = mv_i[-7:-1]+mv_i[-1]
            
            if (uid, mv_i) not in rt_tb:
                rt_tb[(uid, mv_i)] = int(rating_i)
        for j in range(1, 17771):
            mv_j = '000000' + str(j)
            mv_j = mv_j[-7:-1]+mv_j[-1]
            p_sum = 0
            p_count = 0
            p_rating_j = -10
            count = 0
            #count is the number of top similar movies that the user has watched
            if (uid, mv_j) in rt_tb:
                continue
            for rt_his in rt_tb:
                mv_i = rt_his[1]
                if (mv_j, mv_i) not in sim_tb:
                    continue
                p_sum += rt_tb[rt_his] * sim_tb[(mv_j, mv_i)]
                p_count += abs(sim_tb[(mv_j, mv_i)])
                count += 1
            if p_count != 0 and count > n/80:
                p_rating_j = round(p_sum / float(p_count), 4)
                #Get the predicted rating through average
            #Adjust the predicted rating range
            if p_rating_j < 1 and p_rating_j > -10:
                p_rating_j = 1
            
            elif p_rating_j > 5:
                p_rating_j = 5
            
            k = 10  #The number of recommended movies!!!
            if len(rec_ls) < k:
                rec_ls.append((p_rating_j, mv_j))
            else:
                rec_ls.sort(reverse=True)
                if p_rating_j > rec_ls[-1][0]:
                    rec_ls[-1] = (p_rating_j, mv_j)
        rec_ls.sort(reverse=True)
        print 'Recommendation For User %s:' % uid
        for item in rec_ls:
            print item  #Don't forget the ,
            #print item[1],
        print
        '''
        with open(output, 'a') as out:
            out.write('%s:    ' % uid)
            for item in rec_ls:
                out.write('%s ' % item)
            out.write('\n')
            out.close()
        '''
    #return output



if __name__ == '__main__':
    '''
    sim = 'D:\COEN242ProjectTest\small_sim_reduce_topk.txt'
    orig_rt = 'D:\COEN242ProjectTest\small_input.txt'
    '''
    sim = 'D:\COEN242ProjectTest\Step3_TopKOutput.txt'
    orig_rt = 'D:\COEN242ProjectTest\UID864.txt'
    
    recommender(sim, orig_rt)
    

    
    