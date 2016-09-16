import numpy as np
import os
execfile("/home/rumbaugh/LRIS_files_dict_master.py")
execfile("/home/rumbaugh/slit_name_dict_master.py")
files_dict['0435m2']['red']['exp_times'][127] = 0

def run_swarp(outdir,mask,color,side,combine_type='MEDIAN',resample='Y',slitnames=None,skipimgs=None):
    if slitnames == None:
        FILE = open('swarpinputlist_tmp.lst','w')
        FILE2 = open('swarpinweights_tmp.lst','w')
        images = []
        try:
            for night in files_dict[mask]['night']:
                images = np.append(images,files_dict[mask]['night'][night][color]['images'])
        except KeyError:
            images = files_dict[mask][color]['images']
        for img in images:
            if not ((mask == '0435m2') & (side == 'top') & (color == 'red') & (img == 127)):
                flag = True
                try:
                    if img in skipimgs:
                        flag = False
                except TypeError:
                    pass
                if flag:
                    FILE.write('%s%s_%s_%s_%i_bgsub.fits\n'%(outdir,mask,color,side,img))
                    FILE2.write('%s%s_%s_%s_%i_var.fits\n'%(outdir,mask,color,side,img))
        FILE.close()
        FILE2.close()
        os.system("swarp @swarpinputlist_tmp.lst -IMAGEOUT_NAME '%s%s_%s_%s_coadd_bgsub.fits' -WEIGHTOUT_NAME '%s%s_%s_%s_coadd_bgsub.weight.fits' -WEIGHT_IMAGE @swarpinweights_tmp.lst -WEIGHT_TYPE MAP_VARIANCE -BLANK_BADPIXELS Y -RESCALE_WEIGHTS N -BACK_TYPE MANUAL -SUBTRACT_BACK N -COMBINE_TYPE %s -RESAMPLE %s"%(outdir,mask,color,side,outdir,mask,color,side,combine_type,resample))
        os.system("rm swarpinputlist_tmp.lst")
        os.system("rm swarpinweights_tmp.lst")
    else:
        for slit in slitnames:
            FILE = open('swarpinputlist_tmp.lst','w')
            FILE2 = open('swarpinweights_tmp.lst','w')
            images = []
            try:
                for night in files_dict[mask]['night']:
                    images = np.append(images,files_dict[mask]['night'][night][color]['images'])
            except KeyError:
                images = files_dict[mask][color]['images']
            for img in images:
                flag = True
                try:
                    if img in skipimgs:
                        flag = False
                except TypeError:
                    pass
                if flag:
                    FILE.write('%s%s_%s_%s_%s_%i_bgsub.fits\n'%(outdir,mask,slit,color,side,img))
                    FILE2.write('%s%s_%s_%s_%s_%i_var.fits\n'%(outdir,mask,slit,color,side,img))
            FILE.close()
            FILE2.close()
            os.system("swarp @swarpinputlist_tmp.lst -IMAGEOUT_NAME '%s%s_%s_%s_%s_coadd_bgsub.fits' -WEIGHTOUT_NAME '%s%s_%s_%s_%s_coadd_bgsub.weight.fits' -WEIGHT_IMAGE @swarpinweights_tmp.lst -WEIGHT_TYPE MAP_VARIANCE -BLANK_BADPIXELS Y -RESCALE_WEIGHTS N -BACK_TYPE MANUAL -SUBTRACT_BACK N -COMBINE_TYPE %s -RESAMPLE %s"%(outdir,mask,slit,color,side,outdir,mask,slit,color,side,combine_type,resample))
            os.system("rm swarpinputlist_tmp.lst")
            os.system("rm swarpinweights_tmp.lst")

outdir = '/mnt/data2/rumbaugh/LRIS/2011_01/reduced/'
for mask in ['1131m3','1131m4']:
    sides, colors = ['bottom'],['red']
    for color in colors:
        for side in sides:  
            if ((mask not in ['0435m3_v2','1131m1_v2']) | (color != 'blue') | (side != 'top')): 
                if ((mask == '0435m2') & (color == 'red')):
                    run_swarp(outdir,mask,color,side,skipimgs=[127]) 
                else:
                    run_swarp(outdir,mask,color,side)
                f = raw_input('\n\nDid it work?\n\n')
                if f == 'n':
                    try:
                        run_swarp(outdir,mask,color,side,resample='N',skipimgs=files_dict[mask][color]['exp_times'].keys())
                    except KeyError:
                        if ((mask == '0435m2') & (color == 'red')):
                            run_swarp(outdir,mask,color,side,resample='N',skipimgs=[127])
                        else:
                            run_swarp(outdir,mask,color,side,resample='N')

slit_dict = {'1131m1_v2': {'blue': {'top': ['1','54','80','261','490','484','564','663','678','948'], 'bottom': ['176','77']}}, '1131m2_v2': {'blue': {'top': ['1','91','121','197','227','517','600','679','786'], 'bottom': ['98','426']}}, '0435m3_v2': {'blue': {'top': ['132','450','668','604','885','849','865']}}}
