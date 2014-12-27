#可怕的詩

subjects=["晏晏女神", "魚", "老政錩", "Chris","灌籃一姊","蘇停小粉絲"]
verbs=["抓住", "挑眉", "毆打", "凝視", "爬", "搬", "call"]
adv=["曖昧地", "美送地", "輕浮地", "真摯地", "輕鬆地", "飄飄然地", "瀟灑地"]
nouns=["JJ", "為停", "泰瑞","來貘", "閃光"]
a=0

while a < 5 :
    import random
    x = random.choice(subjects)
    y = random.choice(adv)
    z = random.choice(verbs)
    w = random.choice(nouns)

    b = x+" "+y+" "+z+" "+w
    c = x+" "+z+" "+w
    d = [b,c]

    print(random.choice(d))

    a+=1
