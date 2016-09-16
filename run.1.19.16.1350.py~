execfile('/home/rumbaugh/git/CDCranking/CDCranking.py')

filebase='/home/rumbaugh/Downloads/WCDC3.01/view-source_www.hearthpwn.com_forums_hearthstone-general_fan-creations_94398-class-creation-competition-worlds-beyond-warcraft'

filearr=np.zeros(11,dtype='|S200')
filearr[0]='%s.html'%filebase
for i in range(1,11): filearr[i]='%s_page=%i.html'%(filebase,i+1)

dcr=np.loadtxt('/home/rumbaugh/git/CDCranking/disqual_list_WCDC3.01.dat',dtype='i8')
#dcr[dcr>548]-=1
dqa=np.ones((11,20),dtype='bool')
dqf=dqa.flatten()
dqf[dcr-1]=0
dqa2=dqf.reshape((11,20))

CDCrank(filearr,disqual_flags=dqa2,top=30,outfile='/home/rumbaugh/Downloads/WCDC3.01/WCDC_scores_1.12.16.1125.dat',printavgs=True)
