2 == 1 + 1

14 < 13

12 <= 6 + 6

9 == 3**2 and 12 - 3 != 9

9 == 3**2 or 12 - 3 != 9

if True:
    print('bidibix')
	
if 2 == 4:
    print('problème') #ne sera pas affiché car le test est faux#

if 4 < 5:
    print('zêta')

k = int(input('Rentrer une valeur :')) #permet à l'utilisateur de choisir la valeur de k#

if k <= 0:
    print('k est négatif')
elif k <= 10:
    print('k est plus petit que 10')
else:
    print('k est strictement plus grand que 10')

def styl_vt(n): #n nb de stylos#
    if n < 20:
        return 0.7*n
    if n < 250: #on met un if à la place du elif#
        return 0.9 * (0.7*n)
    return 0.85 * (0.7*n) 
    #pas de else & on aligne ce dernier return avec les if#

liste = [2, 4, 7.8 , 'plop'] #exemple de liste#

cpt = 1
for k in range(5):
    cpt = 3*cpt #à chaque passage de boucle, cpt est multiplié par 3#
    print(cpt)

def livret(n):
    s = 600 #somme à l'ouverture#
    for t in range(n): #sert à décompter les années#
        s = 1.0115*s - 4.2
    return round(s, 2) #arrondit au centime s#

print(livret(5), livret(10), livret(20))
