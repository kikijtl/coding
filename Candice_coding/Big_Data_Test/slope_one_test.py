#from math import abs

def mapper(diff, orig_rt):
    diff_f = open(diff, 'r')
    diff_rc = diff_f.read()
    diff_lines = diff_rc.strip()
    diff_lines = diff_lines.splitlines()
    diff_f.close()
    output = 'D:\COEN242ProjectTest\ExSlopeOne.txt'
    diff_tb = {}
    #Store all the difference in diff_tb
    for line in diff_lines:
        k_v = line.split(':')
        key_ls = k_v[0]
        key_ls = key_ls.strip('()').split(',')
        key0 = key_ls[0].strip('""').strip("''")
        key1 = key_ls[1].strip('""').strip("''")
        key = (key0, key1)
        #print key
        if key not in diff_tb:
            diff_tb[key] = round(float(k_v[1]), 3)
    #Now we have the diff_tb
    orig_f = open(orig_rt, 'r')
    orig_rc = orig_f.read()
    orig_lines = orig_rc.strip()
    orig_lines = orig_lines.splitlines()
    orig_f.close()
    for line in orig_lines:
        if line == '':
            continue
        k_v = line.split()
        uid = k_v[0]
        orig_ratings = k_v[1].strip()
        orig_ratings = orig_ratings.split(',')
        for item_i in orig_ratings:
            mv_i, rating_i = item_i.split(':')[0], item_i.split(':')[1]
            p_sum = 0
            p_count = 0
            p_rating_i = -1
            for item_j in orig_ratings:
                mv_j, rating_j = item_j.split(':')[0], item_j.split(':')[1]
                if (mv_i, mv_j) not in diff_tb:
                    continue
                p_sum += int(rating_j) + diff_tb[(mv_i, mv_j)]
                p_count += 1
            if p_count == 0:
                #print rating_i
                p_rating_i = int(rating_i)
            else:
                p_rating_i = round(p_sum / float(p_count), 2)
                #Get the predicted rating through average
            #Adjust the predicted rating range
            if p_rating_i < 1:
                p_rating_i = 1
            elif p_rating_i > 5:
                p_rating_i = 5
            err = abs(p_rating_i - float(rating_i))
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
    
    diff = 'D:\COEN242ProjectTest\ExDiffReduce.txt'
    orig_rt = 'D:\COEN242ProjectTest\ExStep1Output.txt'
    '''
    diff = 'D:\COEN242ProjectTest\small_diff_reduce.txt'
    orig_rating = 'D:\COEN242ProjectTest\small_input.txt'
    '''
    m_out = mapper(diff, orig_rt)
    
    #m_out = 'D:\COEN242ProjectTest\SlopeOneMap.txt'
    reducer(m_out)
    
    '''
    The MAE for small_input.txt is 0.65
    '''
    
                
            
        
    
    