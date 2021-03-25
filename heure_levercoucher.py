#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 13:38:20 2019

@author: jeandavid
"""
import numpy as np

def deg2rad(a):
    return a/180*np.pi

def rad2deg(a):
    return a/np.pi*180

def hsexag2hdec(h):   #heure sexagecimal sous forme decimal en heure decimal
    heure=int(h)
    dec=h-heure
    mn=(dec*100/60)
    return heure+mn

def hdec2hsexag(h):   #heure decimal en heure sexagecimal
    heure=int(h)
    dec=h-heure
    mn=int(dec*60)
    s=int((dec-mn/60)*3600)
    return (heure+fuseau+dst,mn,s)

def fprint(list):
    if list[1]<=9:
        pattern='{}:0{}:{}'
    else:
        pattern='{}:{}:{}'
    return pattern.format(list[0],list[1],list[2])

def hauteur(lat,decl):
    return 90-(lat-decl) if (lat-decl)>0 else 90+lat-decl

def heurelever(lat,decl):
    d=deg2rad(decl)
    l=deg2rad(lat)
    hl=np.arccos(np.tan(l)*np.tan(d))/deg2rad(15)
    hc=24-hl
    return hl,hc

decl=23.2                     #format deg.mn
decl=hsexag2hdec(decl)
lat=48.9
fuseau=1
dst=0

if (dst==0 and decl>4):dst=1 
elif (dst==1 and decl<-12):dst=0


lever, coucher=heurelever(lat,decl)
print('Latitude:',lat)
print('Declinaison:',decl)
print('GMT+',fuseau+dst,'DST' if dst==1 else '')
print('Lever :',fprint(hdec2hsexag(lever)))
print('Coucher :',fprint(hdec2hsexag(coucher)))
print('Hauteur soleil a midi:',hauteur(lat,decl))