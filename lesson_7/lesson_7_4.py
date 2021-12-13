text = '''Стоишь на берегу и чувствуешь соленый запах ветра, что веет с моря, и 
веришь,что свободен ты и жизнь лишь началась, и губы жжет подруги поцелуй, 
пропитанный слезой! '''
d = {}
for i in text.split('\n'):
    for j in i.split():
        d[j] = d.get(j, 0) + 1
slovo_max = d[max(d, key=lambda x: d[x])]
print("Чаще всего используется слово:", *sorted([x for x in d if d[x] ==
                                                 slovo_max]), sep='\n')
