import astropy.constants


print(dir(astropy.constants))
for k in dir(astropy.constants):
    print(k, k.__getitem__)