execfile('/home/rumbaugh/git/CDCranking/CDCranking.py')

filebase='/home/rumbaugh/Downloads/WCDC4.20/view-source_www.hearthpwn.com_forums_hearthstone-general_fan-creations_178455-weekly-card-design-competition-4-20-submission'



numpage=6

filearr=np.zeros(numpage,dtype='|S200')
filearr[0]='%s.html'%filebase
for i in range(1,numpage): filearr[i]='%s_page=%i.html'%(filebase,i+1)

dcr=np.loadtxt('/home/rumbaugh/git/CDCranking/disqual_list_WCDC4.20.dat',dtype='i8')
#dcr[dcr>548]-=1
dqa=np.ones((numpage,20),dtype='bool')
dqf=dqa.flatten()
dqf[dcr-1]=0
dqa2=dqf.reshape((numpage,20))

CDCrank(filearr,disqual_flags=dqa2,top=30,outfile='/home/rumbaugh/Downloads/WCDC4.20/WCDC4.20_scores.dat',printavgs=True)
