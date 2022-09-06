import re, random
import longResponses as long
from datetime import datetime

ahora = datetime.now()

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    # añadir respuestas al diccionario
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # respuestas
    response(random.choice(['¡Hola!', '¿Que tal?', '¡Saludos!']), ['hola', 'hi'], single_response=True)
    response(random.choice(['¡Adios!', '¡Hasta luego!', 'Bye bye']), ['adios', 'nos', 'vemos', 'bye'], single_response=True)
    response('Estoy bien, ¿y tu?', ['como', 'estas'], required_words=['como', 'estas'])
    response('¡No hay de que!', ['gracias', 'chido'], single_response=True)
    response(random.choice(['¡Me halagas, supongo!', 'Gracias, no es reciproco', 'No se que es el amor']), ['te', 'amo'], required_words=['amo'])
    response(random.choice(['¿Que es querer?', '¿Lo dices en serio?']), ['te', 'quiero'], required_words=['quiero'])
    response(random.choice(['¡Me halagas!', 'Gracias, tu a mi no', 'Soy timido']), ['me', 'gustas'], required_words=['gustas'])
    response(random.choice(['¡Crees que me importa?', 'No voy a pelear contigo', 'Perdon']), ['te', 'odio'], required_words=['odio'])
    response('Puedes decirme GUDBot', ['cual', 'es', 'tu', 'nombre'], required_words=['cual', 'nombre'])
    response('Mis creadores me llaman GUDBot', ['como', 'te','llamas'], required_words=['como', 'llamas'])
    response('Mis creadores son Ulises, Gael y David', ['quien', 'es ','tu', 'creador'], required_words=['quien','creador'])
    response(f'Son las {str(ahora.strftime("%H:%M:%S"))}', ['que', 'hora', 'es'], required_words=['hora'])
    response(f'Hoy es {str(ahora.strftime("%d/%m/%y"))}', ['que', 'dia','es', 'hoy'], required_words=['dia'])
    response('Mi color favorito es el azul', ['cual', 'es ','tu', 'color', 'favorito'], required_words=['color'])
    response('No me gustan los deportes', ['cual', 'es ','tu', 'equipo', 'favorito'], required_words=['equipo'])
  
    # manejar respuestas largas a mensajes largos
    response(long.R_COMER, ['cual', 'comida'], required_words=['comida'])
    response(long.R_EDAD, ['cual', 'es', 'tu', 'edad'], required_words=['edad', 'tienes'])
    response(long.R_CHISTE, ['cuentame', 'un', 'chiste'], required_words=['chiste'])
    response(long.R_HACER, ['que', 'haces'], required_words=['que', 'haces'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    '''print(highest_prob_list)
    print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')'''

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# obtener una respuesta con base en el mensaje
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
    
# ciclo para enviar/obtener respuestas
while True:
    print('GUDBot: ' + get_response(input('Usuario: ')))