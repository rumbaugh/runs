import math as m
import sys

try:
    cRA,cDec,r,PA
except NameError:
    sys.exit("Parameters not set")

rt = r/60.0/60.0*m.pi/180.0
PAt = PA*m.pi/180.0
RAout = m.atan((m.cos(cDec)*m.cos(rt)*m.sin(cRA)+m.sin(rt)*(m.cos(cRA)*m.sin(PAt)-m.cos(PAt)*m.sin(cDec)*m.sin(cRA)))/(m.cos(cDec)*m.cos(cRA)*m.cos(rt)-m.sin(rt)*(m.cos(cRA)*m.cos(PAt)*m.sin(cDec)+m.sin(cRA)*m.sin(PAt))))
Decout = m.asin(m.cos(rt)*m.sin(cDec)+m.cos(cDec)*m.cos(PAt)*m.sin(rt))
if RAout < 0: RAout += 2*m.pi
RAdif = (cRA-RAout)*(180/m.pi)*3600.0*m.cos(cDec)
Decdif = (cDec-Decout)*(180.0/m.pi)*3600.0
print RAdif
print Decdif
RAdifalt = m.cos(cRA)*m.cos(cRA)*(-m.tan(cRA)+(m.cos(cDec)*m.cos(rt)*m.sin(cRA)+m.sin(rt)*(m.cos(cRA)*m.sin(PAt)-m.cos(PAt)*m.sin(cDec)*m.sin(cRA)))/((m.cos(cDec)*m.cos(cRA)*m.cos(rt)-m.sin(rt)*(m.cos(cRA)*m.cos(PAt)*m.sin(cDec)+m.sin(cRA)*m.sin(PAt)))))
Decdifalt = (1.0/m.sqrt(1-m.cos(cDec)*m.cos(cDec)))*((1-m.cos(rt))*m.cos(cDec)-m.cos(PAt)*m.sin(rt)*m.sin(cDec))
print RAdifalt*(180/m.pi)*3600.0*m.cos(cDec)
print Decdifalt*(180.0/m.pi)*3600.0

