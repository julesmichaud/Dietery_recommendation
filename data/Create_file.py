meats=['Abats','Charcuterie','Crustaces et mollusques','poissons','Viandes (hors volailles)','Volailles']
desserts=['Compotes et fruits au sirop','Confiserie et chocolat','Entremets et cremes desserts','Fromages','Fruits frais et secs','Glaces, desserts glaces et sorbets','Viennoiseries, patisseries, gateaux et biscuits sucres','Yaourts et fromages blancs']
accompaniments=['Legumes','Legumineus','Noix,graines et fruits oleagineux','Pates, riz, ble et autres cereales completes et semi-completes','Pates, riz, ble et autres cereales raffinees','Pommes de terre et autres tubercules','Substituts de produits animaux a base de soja et autres vegetaux']
starters=['Oeufs et plats a base doeufs','Plats a base de legumes']


repas=['meats','desserts','accompaniments','starters']

for plat in repas:
    new_file=open('/home/dardare/eclipse-workspace/PAF/Dietery_recommendation/data/sorted_by_caterogies/'+plat+'.csv','a')
    for ingre in plat:
        file=open("/home/dardare/eclipse-workspace/PAF/Dietery_recommendation/data/sorted_by_type/"+ingre+".csv","r")
        lines=file.read_lines()
        file.close()
        for line in lines:
            new_file.write(line+'\n')
    new_file.close()