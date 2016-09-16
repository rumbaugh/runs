names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])
names2 = names
for i in range(0,len(names)):
    cr = read_file('/home/rumbaugh/temp/idl_vels.' + names2[i] + '.4.10.12.dat')
    isblu = copy_colvals(cr,'col3')
    g = np.where(isblu == 1)
    g = g[0]
    print names[i],len(isblu),len(g),len(isblu)-len(g)


