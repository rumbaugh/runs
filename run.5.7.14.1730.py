execfile('/mnt/data2/rumbaugh/EVLA/11A-138/scripts/utils_11A-138.py')
set_obs_arr()
for EorL in ['Early']:
    for groupnum in [2]:
        set_fields(EorL,groupnum)
        for SBnum in [9,10]:
            if SBnum != 'X': SBnum = int(SBnum)
            split_off_source(EorL,groupnum,SBnum,BPfield,'/mnt/data2/rumbaugh/EVLA/11A-138/data/%sSB%i/data/%sSB%i_%s.%s.11A-138.%s'%(EorL,groupnum,EorL,groupnum,str(SBnum),EVLA_date_dict[EorL][groupnum][SBnum],BPname))
            for field,fieldname in zip(CSOfields_arr,CSOnames):
                split_off_source(EorL,groupnum,SBnum,field,'/mnt/data2/rumbaugh/EVLA/11A-138/data/%sSB%i/data/%sSB%i_%s.%s.11A-138.%s'%(EorL,groupnum,EorL,groupnum,str(SBnum),EVLA_date_dict[EorL][groupnum][SBnum],fieldname))
            #for field,fieldname in zip(PCfields_arr,PCnames):
            #    split_off_source(EorL,groupnum,SBnum,field,'/mnt/data2/rumbaugh/EVLA/11A-138/data/%sSB%i/data/%sSB%i_%s.%s.11A-138.%s'%(EorL,groupnum,EorL,groupnum,str(SBnum),EVLA_date_dict[EorL][groupnum][SBnum],fieldname))
            for field,fieldname in zip(lensfields_arr,lensnames):
                split_off_source(EorL,groupnum,SBnum,field,'/mnt/data2/rumbaugh/EVLA/11A-138/data/%sSB%i/data/%sSB%i_%s.%s.11A-138.%s'%(EorL,groupnum,EorL,groupnum,str(SBnum),EVLA_date_dict[EorL][groupnum][SBnum],fieldname))
            FILE2 = open('/home/rumbaugh/progress.5.7.14.1730','a')
            FILE2.write('Finished splitting off %sSB%i_%s\n'%(EorL,groupnum,str(SBnum)))
            FILE2.close()
