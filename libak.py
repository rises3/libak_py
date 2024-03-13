# LIBÁK

# A róka libát lop a faluból. A libák súlyát – pontosabban tömegét – listában adjuk meg. A farkas a dűlőútnál várja a rókát, és a három kilónál nagyobb libákat elveszi – a piciket nagylel�kűen otthagyja a rókának.
# libak = [1,5,2,3,4]

# a. Hány kiló libát ehet meg a róka?
# b. Átlagosan hány kilósak a rókának maradt libák?
# c1. Előfordult-e olyan, hogy a róka legalább háromkilós libát lopott?
# c2. Előfordult-e olyan, hogy a róka kisebb libát hozott, mint az előző napon?
# d. Hányadik napon sikerült a rókának először legalább háromkilós libát lopnia?
# e. Melyik a róka első legalább háromkilós libája?
# f. Hány libát tarthat meg a róka?
# g. Mekkora a legkisebb liba, amit a farkas elvesz a rókától?

def beolvasas():
    l=[]
    with open("libak.txt", "r", encoding="UTF-8") as fm:
        for sor in fm:
            l.append(int(sor.strip()))
    return l

def kiir(l, r_m_kg, r_a, r_l3s, r_lklen):
    print(f"A libák súlyai: {l}")
    print(f"{r_m_kg} kg libát ehet meg a róka")
    print(f"Átlagosan {r_a} kilósak a rókának maradt libák")
    print(f"{r_l3s} olyan, hogy a róka legalább 3 kg-s libát lopott.")
    print(f"{r_lklen} olyan, hogy a róka kisebb libát hozott, mint az előző napon.")
    
def osszegzes(l):
    osszeg=0
    for elem in l:
        if elem<=3:
            osszeg+=elem
    return osszeg

def megszamolas(l):
    db=0
    for suly in l:
        if db<=3:
            db+=1
    return db
            
def eldontes1(l):
    van=False
    i=0
    while i<len(l) and not l[i]>=3:   
        i+=1
    if i<len(l):
        van=True
    return van         
            
def eldontes2(l):
    i=len(l)-1            
    while i>0 and not (l[i]>l[i-1]):
        i-=1
    if i<len(l):
        van=True
    else:
        van=False
    return van
            
            
            

libak=beolvasas()
r_megehet_ossz_kg=osszegzes(libak)
r_megehet_db=megszamolas(libak)
r_atlag=r_megehet_ossz_kg/r_megehet_db
r_legalabb_harom_e=eldontes1(libak)
if r_legalabb_harom_e:
    r_legalabb_harom_e_string="Előfordult"
else:
    r_legalabb_harom_e_string="Nem fordult elő"
    
r_lopott_kisebb_libat_elozo_nap=eldontes2(libak)
if r_lopott_kisebb_libat_elozo_nap:
    r_lopott_kisebb_libat_elozo_nap_string="Előfordult"
else:
    r_lopott_kisebb_libat_elozo_nap_string="Nem fordult elő"


kiir(libak, r_megehet_ossz_kg, r_atlag, r_legalabb_harom_e_string, r_lopott_kisebb_libat_elozo_nap_string)