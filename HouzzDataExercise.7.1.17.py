import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.cm as cm
import pickle

#load csvs
df=pd.read_csv('signups.csv',index_col=0)
vdf=pd.read_csv('visits.csv',index_col=0)

#count total unique visitors for later
tot_uids=len(df.uid.unique())

#set up matplotlib params
plt.figure(1)
plt.clf()
plt.close('all')
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)

#Plot bar graph of auth_type frequency
df.auth_type.value_counts(sort=False).plot(kind='barh')
vc=df.auth_type.value_counts()

fig=plt.gcf()
ax0=fig.get_axes()[0]
for iat,authtype in zip(np.arange(3),['A','B','C']): ax0.text(0.05,1./6+iat/3.,vc.loc[authtype],color='red',fontsize=24,horizontalalignment='left',verticalalignment='center',transform=ax0.transAxes)
plt.xticks(np.arange(0,45000,10000))
plt.savefig('/home/rumbaugh/Houzz/AuthTypeBarGraph.png',dpi=400)
plt.clf()
plt.close('all')


#Plot bar graph of device frequency
df.device.value_counts(sort=False).plot(kind='bar')
vc=df.device.value_counts()

fig=plt.gcf()
ax0=fig.get_axes()[0]
for iat,device in zip(np.arange(7),np.arange(1,8)): ax0.text(iat,vc.loc[device]+200,vc.loc[device],color='red',fontsize=14,horizontalalignment='center',verticalalignment='bottom')
plt.savefig('/home/rumbaugh/Houzz/DeviceBarGraph.png',dpi=400)
plt.clf()
plt.close('all')

#cros-tabulate device and auth_type then write to file
ct=pd.crosstab(df.device,df.auth_type)
ct.to_csv('/home/rumbaugh/Houzz/crosstab_auth_type_device.csv')

#plot histogram
ct.plot(kind = 'bar', colormap = cm.Accent, width = 1)
plt.savefig('/home/rumbaugh/Houzz/DeviceAuthtypeCrosstab.png',dpi=400)
plt.clf()
plt.close('all')

#make merged dataframe
mdf=pd.merge(df,vdf,on=['uid'])
#mdf.set_index('uid',inplace=True)
mdf['difference']=pd.to_datetime(mdf['dt']).sub(pd.to_datetime(mdf['signup_dt']))/np.timedelta64(1,'D')

try:
    heatmap_df=pickle.load(open('/home/rumbaugh/Houzz/heatmap_df1.pickle','rb'))
    signup_df=pickle.load(open('/home/rumbaugh/Houzz/signup_df1.pickle','rb'))
except IOError:
    heatmap_df=pd.DataFrame({x:0.0 for x in np.arange(1,25)},index=pd.date_range('2016-06-01','2016-10-30'))
    signup_df=pd.DataFrame({'signups':0},index=pd.date_range('2016-06-01','2016-10-30'))
    for signupdate in pd.date_range('2016-06-01','2016-10-30'):
        signupdate_str='{:4d}-{:02d}-{:02d}'.format(signupdate.year,signupdate.month,signupdate.day)
        mdf_tmp=mdf[mdf.signup_dt.values==signupdate_str]
        daily_signups=len(mdf_tmp.uid.unique())
        signup_df.loc[signupdate_str]['signups']=daily_signups
        #create categorical for week
        mdf_tmp['week']=pd.cut(mdf_tmp.difference,bins=np.arange(-1,24*7,7),labels=np.arange(1,25,dtype='i8'))
        mdf_tmp.set_index(['uid'],inplace=True)
        week_ct=pd.crosstab(mdf_tmp.index,mdf_tmp.week)
        #Remove signup visit from week 1
        week_ct[1]-=1
        #count visitors
        revisits=np.count_nonzero(week_ct,axis=0)
        heatmap_df.loc[signupdate_str]=revisits
    pickle.dump(heatmap_df,open('/home/rumbaugh/Houzz/heatmap_df1.pickle','wb'))
    pickle.dump(signup_df,open('/home/rumbaugh/Houzz/signup_df1.pickle','wb'))

fig, ax = plt.subplots(1,1)
ax.yaxis_date()

#plot heatmap
heatmap2=heatmap_df.multiply(100./signup_df.signups,axis='rows')
d=pd.date_range('2016-06-01','2016-10-30')
d=dates.date2num(d.to_pydatetime())
heatmap2.index=d
plt.pcolor(np.arange(0,25),d,heatmap2.values)
#format axes
plt.xlim(0,24)
plt.xlabel('Week')
plt.ylabel('Sign-up Date')
date_format = dates.DateFormatter('%m/%d')
ax.yaxis.set_major_formatter(date_format)
#reverse y-axis
ylim=plt.ylim()
plt.ylim(ylim[1],ylim[0])
#make colorbar
clb = plt.colorbar()
clb.set_label('Re-visit %', labelpad=-40, y=1.05, rotation=0)

plt.savefig('/home/rumbaugh/Houzz/VisitsHeatmap.png',dpi=400)
plt.clf()
plt.close('all')

#average revist percentage over signupdate
revist_perc=heatmap2.mean(axis=0)

color_arr,ls_arr=['red','blue'],['solid','dashed','dotted']
datestr_arr,auth_arr=['7/24','8/18'],['A','B','C']
#2-day heatmap, segmented by auth_type
heatmap_df_auth=pd.DataFrame({x:0.0 for x in np.arange(1,25)},index=np.arange(6))
for signupdate, i in zip([datetime(2016,7,24),datetime(2016,8,18)],[0,1]):
    signupdate_str='{:4d}-{:02d}-{:02d}'.format(signupdate.year,signupdate.month,signupdate.day)
    mdf_tmp=mdf[mdf.signup_dt.values==signupdate_str]
    for auth,j in zip(auth_arr,np.arange(3)):
        mdf_tmp_auth=mdf_tmp[mdf_tmp.auth_type.values==auth]
        mdf_tmp['dt0']=pd.to_datetime(mdf_tmp_auth.dt)
        daily_signups=len(mdf_tmp_auth.uid.unique())
        for w in np.arange(1,25):
            w_st,w_end=signupdate+timedelta(days=7*(w-1)),signupdate+timedelta(days=7*w-1)
            mdf_tmp_auth=mdf_tmp.set_index('dt0')
            mdf_tmp_auth=mdf_tmp_auth.loc['{:4d}-{:02d}-{:02d}'.format(w_st.year,w_st.month,w_st.day):'{:4d}-{:02d}-{:02d}'.format(w_end.year,w_end.month,w_end.day)]
            revisits=len(mdf_tmp_auth.uid.unique())
            #Remove signup visit from week 1
            if w==1:revisits-=np.sum(mdf_tmp_auth.uid.value_counts()==1)
            heatmap_df_auth.loc[3*i+j][w]=revisits*100./daily_signups
        plt.plot(np.arange(1,25),heatmap_df_auth.loc[3*i+j],color=color_arr[i],ls=ls_arr[j],lw=2,label='{}-{}'.format(datestr_arr[i],auth_arr[j]))
plt.legend()
plt.xlabel('Week')
plt.ylabel('Re-visit %')
plt.xlim(0.5,24.5)
plt.savefig('/home/rumbaugh/Houzz/VisitsSeg.png',dpi=400)

    
plt.clf()
plt.close('all')
try:
    heatmap_df=pickle.load(open('/home/rumbaugh/Houzz/heatmap_df2.pickle','rb'))
    nonvisit_df=pickle.load(open('/home/rumbaugh/Houzz/nonvisit_df2.pickle','rb'))
except IOError:
    heatmap_df=pd.DataFrame({x:0.0 for x in np.arange(1,25)},index=pd.date_range('2016-06-01','2016-10-30'))
    nonvisit_df=pd.DataFrame({'nonvisits':0.0},index=pd.date_range('2016-06-01','2016-10-30'))
    for signupdate in pd.date_range('2016-06-01','2016-10-30'):
        signupdate_str='{:4d}-{:02d}-{:02d}'.format(signupdate.year,signupdate.month,signupdate.day)
        mdf_tmp=mdf[mdf.signup_dt.values==signupdate_str]
        #creat categorical for week
        mdf_tmp['week']=pd.cut(mdf_tmp.difference,bins=np.arange(-1,24*7,7),labels=np.arange(1,25,dtype='i8'))
        mdf_srt=mdf_tmp.sort_values(['uid','week'])
        mdf_srt.set_index(['uid'],inplace=True)
        week_ct=pd.crosstab(mdf_srt.index,mdf_srt.week)
        #Remove signup visit from week 1
        week_ct[1]-=1
        #find first visit
        first_nonzero=(week_ct>0).idxmax(axis=1)
        #find entries that didn't visit in 24 weeks
        week_ct_sum=np.sum(week_ct,axis=1)
        first_nonzero[week_ct_sum==0]=-1
        #count it up
        heatmap_df.loc[signupdate_str]=np.array([np.sum(first_nonzero==w) for w in np.arange(1,25)])#*100./daily_signups
        nonvisit_df.loc[signupdate_str]=np.sum(first_nonzero==-1)#*100./daily_signups
    pickle.dump(heatmap_df,open('/home/rumbaugh/Houzz/heatmap_df2.pickle','wb'))
    pickle.dump(nonvisit_df,open('/home/rumbaugh/Houzz/nonvisit_df2.pickle','wb'))


fig=plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.7]) 
ax.yaxis_date()

#plot heatmap
heatmap2=heatmap_df.multiply(100./signup_df.signups,axis='rows')
d=pd.date_range('2016-06-01','2016-10-30')
d=dates.date2num(d.to_pydatetime())
heatmap2.index=d

pc=ax.pcolor(np.arange(0,25),d,heatmap2.values)
#format axes
ax.set_xlim(0,24)
ax.set_xlabel('Week')
ax.set_ylabel('Sign-up Date')
date_format = dates.DateFormatter('%m/%d')
ax.yaxis.set_major_formatter(date_format)
#reverse y-axis
ylim=ax.get_ylim()
ax.set_ylim(ylim[1],ylim[0])
#make colorbar
clb = plt.colorbar(pc)
clb.set_label('First Visit %', labelpad=-18, y=1.05, rotation=0)

#Make cumulative percentage plot
axX = fig.add_axes([0.1, 0.8, 0.8*0.8, 0.125], sharex=ax) 
visits_perday=heatmap_df.sum(axis=0)
cumvisits=visits_perday.cumsum()
cumperc=cumvisits*(100./tot_uids)
axX.plot(np.arange(1,25),cumperc)
axX.set_ylabel('Cum. 1st Visit %')
axX.set_ylim(60,85)
axX.set_yticks(np.arange(60,85,10))
ax.set_xlim(0,24)
axX.set_xlim(0,24)
plt.setp(axX.get_xticklabels(), visible=False)

plt.savefig('/home/rumbaugh/Houzz/FirstVisitsHeatmap.png',dpi=400)
plt.clf()
plt.close('all')
