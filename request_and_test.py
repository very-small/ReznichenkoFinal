import configuration
import requests
import data

# Функция создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

# Функция получения трека созданного заказа в числовом виде из ответа
def track_order(track_str):
   temp1 = str(track_str)
   temp = ""
   for c in temp1:
      if c.isdigit():
          temp = temp + c
   track = int(temp)
   return track

# Функция получения заказа по треку
def get_track_order(track):
   return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track))


# Тест.
def test_order_track():
    # Создаем новый заказ
    order_new_track = post_new_order(data.order_new).json()
    print (order_new_track)
    # Получаем его трек
    new_track  = track_order(order_new_track)
    print (new_track)
    # По треку получаем заказ и ответ
    return_order = get_track_order(new_track)
    print (return_order)
    # Сам тест на успех
    assert return_order.status_code == 200

test_order_track()



