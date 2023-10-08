# Funktiot
def paljasta_lahja(arvoitus1, arvoitus2, arvoitus3):
    print(f'{arvoitus1} nimeltä {arvoitus2} la {arvoitus3} klo 19')
    print(f'Hyvää syntymäpäivää rakas!')

def mika_mina_olen():
    print('Olen Batman')
    print('Olen Teräsmies')
    print('Olen Jedi')

    return 'Dracula'

# Ensimmäinen arvoitus
mita = ''
first_list = ['bc', 'ba', 'abc', 'let', 'titi', 'ti']
listan_pituus = len(first_list)

for i in range(listan_pituus):
    if i % 2 == 1:
        mita += first_list[i]

# Toinen arvoitus
ihmetta = mika_mina_olen()

# Kolmas arvoitus

kirjasto = {'paiva': '2', 'kuukausi': '3', 'vuosi': '2024'}
tapahtuu = kirjasto['paiva']+'.'+kirjasto['kuukausi']+'.'+kirjasto['vuosi']

#Paljasta synttärilahja
paljasta_lahja(mita, ihmetta, tapahtuu)