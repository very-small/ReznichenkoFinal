import data
import sender_stand_request

# Тест.
def test_order_track():
    # Создаем новый заказ и получаем его трек
    track_number = sender_stand_request.post_new_order(data.order_new).json()["track"]
    # По треку получаем заказ и ответ
    resp_get_track_order = sender_stand_request.get_track_order(track_number)
    # Сам тест на успех
    assert resp_get_track_order.status_code == 200

test_order_track()



