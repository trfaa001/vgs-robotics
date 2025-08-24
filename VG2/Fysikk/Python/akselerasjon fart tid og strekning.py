# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:46:38 2023

@author: trfaa001
"""
import time
print("Alle Variabler blir rundet ned til 1 desimal")
print("Hvilkene variabler har du (skriv ja eller nei)?")
time.sleep(1)

harvest_v0 =round(input("Har du start fart?"), 1)
harvest_v = round(input("Har du fart?"), 1)
harvest_a = round(input("Har du akselerasjon?"), 1)
harvest_t = round(input("Har du tid?"), 1)
harvest_s = round(input("Har du strekning?"), 1)

if harvest_v0 == "ja":
    v0 = float(input("Skriv startfart"))
if harvest_v == "ja":
    v = float(input("Skriv fart"))
if harvest_a == "ja":
    a = float(input("Skriv akselerasjon"))
if harvest_t == "ja":
    t = float(input("Skriv tid"))
if harvest_s == "ja":
    s = float(input("Skriv strekning"))    


if havest_t == "nei":
    if harvest_v == "ja" and harvest_v0 and harvest_a:
        t = (v-v0)/a
    if harvest_s and harvest_v0 and harvest_t and harvest_a:
        t = ((2*s)/t-(2*(v0*v-vo**2))/(a**2))**1/2
    