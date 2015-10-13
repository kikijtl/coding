def sim_recommender(mid):
    title_f = open("D:\KIKI\Study\SCU\Big Data\Project\\nf_prize_dataset\movie_titles.txt", 'rb')
    title_rc = title_f.read()
    title_lines = title_rc.strip()  #remove whitespaces in head and tail
    title_lines = title_lines.splitlines()
    title_f.close()
    #output = 'D:\COEN242ProjectTest\RecommendLs.txt'
    title_tb = {}
    #Store all the similarity in sim_tb
    for line in title_lines:
        #The input line format is: key_mv mv1:sim1,mv2:sim2,...
        k_v = line.split(',')  #Split line using whitespaces. Now k_v is a list: [key, value]
        mv_i = k_v[0]
        mv_i = '000000' + mv_i
        mv_i = mv_i[-7:-1]+mv_i[-1]
        title = k_v[2]
        title_tb[mv_i] = title
    #Now we have the sim_tb
    corr_f = open('D:\COEN242ProjectTest\Step3_Top10_Correlation.txt', 'r')
    corr_rc = corr_f.read()
    corr_lines = corr_rc.strip()  #remove whitespaces in head and tail
    corr_lines = corr_lines.splitlines()
    corr_f.close()
    for line in corr_lines:
        #The input line format is: key_mv mv1:sim1,mv2:sim2,...
        k_v = line.split()  #Split line using whitespaces. Now k_v is a list: [key, value]
        mv_i = k_v[0]
        if mv_i == mid:
            corr_ls = k_v[1]
            corr_ls = corr_ls.strip().split(',')
            print '(Correlation)Movies similar to %s(%s) is:' % (title_tb[mid], mid)
            for item in corr_ls:
                mv_j, corr = item.strip().split(':')[0], item.strip().split(':')[1]
                print '%s(%s), %s' % (title_tb[mv_j], mv_j, corr)
    print
    
    cos_f = open('D:\COEN242ProjectTest\Step3_Top10_Cosine.txt', 'r')
    cos_rc = cos_f.read()
    cos_lines = cos_rc.strip()  #remove whitespaces in head and tail
    cos_lines = cos_lines.splitlines()
    cos_f.close()
    for line in cos_lines:
        #The input line format is: key_mv mv1:sim1,mv2:sim2,...
        k_v = line.split()  #Split line using whitespaces. Now k_v is a list: [key, value]
        mv_i = k_v[0]
        if mv_i == mid:
            cos_ls = k_v[1]
            cos_ls = cos_ls.strip().split(',')
            print '(Cosine)Movies similar to %s(%s) is:' % (title_tb[mid], mid)
            for item in cos_ls:
                mv_j, cos = item.strip().split(':')[0], item.strip().split(':')[1]
                print '%s(%s), %s' % (title_tb[mv_j], mv_j, cos)
    print            
    
    adjcos_f = open('D:\COEN242ProjectTest\Step3_Top10_AdjCosine.txt', 'r')
    adjcos_rc = adjcos_f.read()
    adjcos_lines = adjcos_rc.strip()  #remove whitespaces in head and tail
    adjcos_lines = adjcos_lines.splitlines()
    adjcos_f.close()
    for line in adjcos_lines:
        #The input line format is: key_mv mv1:sim1,mv2:sim2,...
        k_v = line.split()  #Split line using whitespaces. Now k_v is a list: [key, value]
        mv_i = k_v[0]
        if mv_i == mid:
            adjcos_ls = k_v[1]
            adjcos_ls = adjcos_ls.strip().split(',')
            print '(Adjusted Cosine)Movies similar to %s(%s) is:' % (title_tb[mid], mid)
            for item in adjcos_ls:
                mv_j, adjcos = item.strip().split(':')[0], item.strip().split(':')[1]
                print '%s(%s), %s' % (title_tb[mv_j], mv_j, adjcos)
                
if __name__ == '__main__':
    mid = '0014240'
    title_source = 'D:\KIKI\Study\SCU\Big Data\Project\nf_prize_dataset\movie_titles.txt'
    
    sim_recommender(mid)
    
        