
def mapper(sim, orig_rt):
    sim_f = open(sim, 'r')
    sim_rc = sim_f.read()
    sim_lines = sim_rc.strip()  #remove whitespaces in head and tail
    sim_lines = sim_lines.splitlines()
    sim_f.close()
    output = 'D:\COEN242ProjectTest\Step3SimPre.txt'
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
            if (mv_i, mv_j) not in sim_tb:
                sim_tb[(mv_i, mv_j)] = round(float(sim), 4)
                #print (mv_i,mv_j)
    #Now we have the sim_tb
    orig_f = open(orig_rt, 'r')
    orig_rc = orig_f.read()
    orig_lines = orig_rc.strip()
    orig_lines = orig_lines.splitlines()
    orig_f.close()
    for line in orig_lines:
        #The input line format is: uid    rt_count,rt_avg,mv1:rating1,mv2:rating2,...
        if line == '':
            continue
        k_v = line.split()
        uid = k_v[0]
        orig_ratings = k_v[1].strip()
        orig_ratings = orig_ratings.split(',')[2:]
        for item_i in orig_ratings:
            mv_i, rating_i = item_i.split(':')[0], item_i.split(':')[1]
            p_sum = 0
            p_count = 0
            p_rating_i = -1
            for item_j in orig_ratings:
                mv_j, rating_j = item_j.split(':')[0], item_j.split(':')[1]
                if (mv_i, mv_j) not in sim_tb or mv_i == mv_j:
                    #print (mv_i,mv_j)
                    continue
                p_sum += int(rating_j) * sim_tb[(mv_i, mv_j)]
                p_count += abs(sim_tb[(mv_i, mv_j)])
            if p_count == 0:
                #print rating_i
                p_rating_i = 0
            else:
                p_rating_i = round(p_sum / float(p_count), 4)
                #Get the predicted rating through average
            #Adjust the predicted rating range
            if p_rating_i < 1 and p_rating_i != 0:
                p_rating_i = 1
            elif p_rating_i > 5:
                p_rating_i = 5
            err = abs(p_rating_i - float(rating_i))
            #The mapper output is: uid:mv_i    predict_rating,absolute_error
            with open(output, 'a') as out:
                out.write('%s:%s    %s,%s\n' % (uid, mv_i, p_rating_i, err))
                out.close()
    return output


def reducer(file):
    f = open(file, 'r')
    data = f.read()
    data = data.strip()
    lines = data.splitlines()
    err_sum = 0
    err_count = 0
    for line in lines:
        k_v = line.split()
        key = k_v[0]
        value = k_v[1]
        value = value.strip()
        value = value.split(',')
        p_rating = value[0]
        err = float(value[1])
        err_sum += err
        err_count += 1
    print err_sum / float(err_count)
    

if __name__ == '__main__':
    
    sim = 'D:\COEN242ProjectTest\small_sim_reduce_topk.txt'
    orig_rt = 'D:\COEN242ProjectTest\small_input.txt'
    '''
    sim = 'D:\COEN242ProjectTest\Step3_TopKOutput.txt'
    orig_rt = 'D:\COEN242ProjectTest\ExStep1Output.txt'
    '''
    m_out = mapper(sim, orig_rt)
    
    #m_out = 'D:\COEN242ProjectTest\SlopeOneMap.txt'
    reducer(m_out)
    
    '''
    The MAE for small_input.txt is 0.2679
    '''
    
                
            
        
    
    