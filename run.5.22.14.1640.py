execfile('/mnt/data2/rumbaugh/EVLA/11A-138/scripts/utils_11A-138.py')
set_obs_arr()

for lens in ['MG0414+0534','B0712+472','B1938+666']:
    if lens == 'B1938+666': EorL = 'Late'
    else: EorL = 'Early'
    for gnum in EVLA_obs_dict[EorL]:
        for SBnum in EVLA_obs_dict[EorL][gnum]:
            prefix = '/mnt/data2/rumbaugh/EVLA/11A-138/data/%sSB%i/data/%sSB%i_%s.'%(EorL,gnum,EorL,gnum,SBnum)
            prefix_len = len(prefix)
            if EVLA_obs_dict[EorL][gnum][SBnum][prefix_len+4:prefix_len+6] == '11': 
                odate = EVLA_obs_dict[EorL][gnum][SBnum][prefix_len:prefix_len+6]
            else: 
                odate = EVLA_obs_dict[EorL][gnum][SBnum][prefix_len:prefix_len+7]
            vis = '%s%s.11A-138.%s.ms'%(prefix,odate,lens)
            plotms(vis=vis,xaxis='time',yaxis='amp',selectdata=True,field='',spw='',timerange='',antenna='',correlation='RR',averagedata=True,avgchannel='64',avgtime='',avgspw=True)
            print 'Plotting %sSB%i_%s - %s - %s'%(EorL,gnum,SBnum,lens,odate)
            chk = raw_input('Continue?\n')
            while chk != 'y':
                print 'Invalid Input'
                chk = raw_input('Continue?\n')
            
