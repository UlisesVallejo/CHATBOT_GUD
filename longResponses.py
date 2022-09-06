import random

R_COMER = "No me gusta comer nada porque soy un bot, ¡obvio!"
R_EDAD = "No tengo idea, soy solo un bot, pregunta a mis creadores"
R_HACER = 'Estoy conversando contigo justo ahora'
R_CHISTE = random.choice([
    '¿Que es una naranja con cuernos? UNA TOROnja',
    '¿Donde compra sus pantalones Goku? En Saya-Jeans XD',
    '¿Cuales son las cucarachas gays? Las que salen del closet',
    'Este era un pollito tan inteligente que en lugar de decir pi decia 3.1416'
])

def unknown():
    response = ["¿Podrias repetirlo? ",
                "¿Que significa eso?",
               'Si fuera tu, ¡iria a internet a escribir exactamente lo que escribiste aqui!'][
        random.randrange(3)]
    return response