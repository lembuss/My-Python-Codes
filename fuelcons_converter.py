# fuel consumption converter

def l100kmtompg(liters):
    lpkm = liters/100
    gpm = lpkm * 0.4248
    mpg = 1/gpm
    
    return mpg
    
def mpgtol100km(miles):
    gpm = 1/miles
    lpkm = gpm * 2.351
    l100km = lpkm * 100
    
    return l100km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
