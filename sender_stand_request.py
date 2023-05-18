import configuration
import requests

# Функция создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

# Функция получения заказа по треку
def get_track_order(track):
   return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track))






