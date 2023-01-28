def generar_armadura():
    legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']
    stroomtroper=[]

    for i in range(2000):
        num= str(random.randint(100,999))
        batallon= random.choice(legiones)
        stroomtroper.append(soldado)
    
    soldado={}
    for trooper in stroomtroper:
        legion=stroomtroper[:2]
        if legion not in s.leg:
            s.leg[legion]=[]
        s.leg[legion].append(trooper)
