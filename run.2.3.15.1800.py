import numpy as np

date = '2.3.15'

model_dict = {'MG0414+0534': 'rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod','B0712+472': 'rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod', 'B1938+666': 'shift -1.221864,-0.110719\naddcmp 0.0717458,true,-0.664,0.574,varpos\naddcmp 0.0307923,true,-0.053,0.869,varpos\naddcmp 0.0809120,true,-0.581,0.695,varpos\naddcmp 0.0112803,true,0.0,0,varpos\naddcmp 0.00985509,true,-0.310,0.973,varpos\naddcmp 0.00985509,true,-0.098,0.077,varpos'}

execfile('/home/rumbaugh/B1938+666_files/scripts/utils_11A-138.py')
set_obs_arr()

FILE=open('/home/rumbaugh/runs/run.%s.1800.sh'%date,'w')
FILE.write("#!/bin/bash\n")

opening_string = "difmap << EOF\ninteger mfitniter\nmfitniter = 7\nlogical varpos\nvarpos = false\n"
setup_string = "select I\nmapunits arcsec\nmapsize 256,0.05\n"
fit_string = "modelfit mfitniter\nselfcal false,false,60\nmodelfit mfitniter\nselfcal false,false, 60\nmodelfit mfitniter\nshift 0.1,-0.3\cmul = imstat(rms)\naddcmp cmul,false,0,0\n"
end_string = "quit\nEOF\n"

for EorL in ['Late']:
    for groupnum in np.sort(EVLA_obs_dict[EorL].keys()):
        set_fields(EorL,groupnum)
        for SBnum in np.sort(EVLA_obs_dict[EorL][groupnum].keys()):
            if SBnum != 'X': SBnum = int(SBnum)
            date = EVLA_date_dict[EorL][groupnum][SBnum]
            #for field,fieldname in zip(CSOfields_arr,CSOnames):
            #    source = fieldname
            #    FILE.write(opening_string)
            #    uvfile = '/mnt/data2/rumbaugh/EVLA/11A-138/data/%sSB%i/data/%sSB%i_%s.%s.11A-138.%s.uvfits'%(EorL,groupnum,EorL,groupnum,str(SBnum),EVLA_date_dict[EorL][groupnum][SBnum],fieldname)
            #    FILE.write('obs %s\n'%uvfile)
            #    FILE.write(setup_string)
            #    FILE.write('addcmp 0.1,true,0,0,varpos\n')
            #    FILE.write(fit_string)
            #    outfile = '/mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit_wrms.%s.%sSB%i_%s.fixpos.%s.mod'%(source,EorL,groupnum,str(SBnum),date)
            #    FILE.write('wmod %s\n'%outfile)
            #    FILE.write(end_string)
            for field,fieldname in zip(lensfields_arr,lensnames):
                source = fieldname
                FILE.write(opening_string)
                uvfile = '/home/rumbaugh/B1938+666_files/%sSB%i_%s.%s.11A-138.%s.uvfits'%(EorL,groupnum,str(SBnum),EVLA_date_dict[EorL][groupnum][SBnum],fieldname)
                FILE.write('obs %s\n'%uvfile)
                FILE.write(setup_string)
                FILE.write('%s\n'%model_dict[fieldname])
                #FILE.write(fit_string)
                if SBnum != 'X':FILE.write("modelfit mfitniter\nselfcal false,false,60\nmodelfit mfitniter\nselfcal false,false, 60\nmodelfit mfitniter\nshift 0.1,-0.3\nwdmap  /home/rumbaugh/B1938+666_files/residual_map.%s.%sSB%i_%s.fixpos.%s.fits\ncmul = imstat(rms)\naddcmp cmul,false,0,0\n"%(source,EorL,groupnum,str(SBnum),date))
                #outfile = '/mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit_wrms.%s.%sSB%i_%s.fixpos.%s.mod'%(source,EorL,groupnum,str(SBnum),date)
                #FILE.write('wmod %s\n'%outfile)
                FILE.write(end_string)
