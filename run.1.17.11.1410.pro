set_dirs
set_plot,'PS'
device,file='/home/rumbaugh/COSMOS/test.spat.error.plot.ps'

for i=0,2 do begin &$
   for j=0,2 do begin &$
   dists = [] &$
   for k=1,10 do begin &$
      file = "/home/rumbaugh/COSMOS/analysis/test.spat.error.1.17.11.1400_" + STRCOMPRESS(string(i*30 + j*10 + k),/REMOVE_ALL) + ".dat" &$
      readcol,file,tra,tdec,tdist,format="I,I,D",SILENT=1 &$
      dists = [dists,tdist] &$
   endfor &$
   Histoplot,dists,MININPUT=0,MAXINPUT=40,BINSIZE=5,PROBABILITY=cprob,LOCATIONS=loc &$
   Histoplot,dists,MININPUT=0,MAXINPUT=40,BINSIZE=1,PROBABILITY=cprob,LOCATIONS=loc &$
   plot,[0-1],[0-1],/nodata,XRANGE=[0,40],yrange=[0,1.1],xstyle=1,ystyle=1 &$
   oplot,loc,cprob &$
   g = sort(dists) &$
   co = dists[g[UINT(0.68*n_elements(dists))]] &$
   print, co &$
endfor &$
endfor
end
