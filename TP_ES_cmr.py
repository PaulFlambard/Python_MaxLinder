import random as rd
N_pop = rd.randint(700, 54000)

min_capt1 = int(0.02*N_pop)
max_capt1 = int(0.04*N_pop)
n_capt1 = rd.randint(min_capt1, max_capt1)
p_marq = n_capt1/N_pop

print('Lors de la première capture, on a attrapé & marqué '
      , n_capt1, ' individus')

n_capt2 = rd.randint(min_capt1, max_capt1)

n_marq = 0

for ind in range(n_capt2):
    if rd.random() <= p_marq:
        n_marq = n_marq + 1
        
if n_marq < 2:
    while n_marq < 2 or n_capt2 <= N_pop:
        n_capt2 = n_capt2 + 1        
        if rd.random() <= p_marq:
            n_marq = n_marq + 1

print('Lors de la recapture, on a attrapé ', n_capt2,
      'individus dont ', n_marq, 'été marqués')

p = int(input("Combien d'individus dans la population ? "))

print('La population totale était de ', N_pop, 'individus')
print("L'écart absolu a été de ", p - N_pop,
      "et l'écart relatif a été de ",
      100*round((p - N_pop)/N_pop, 4), '%')