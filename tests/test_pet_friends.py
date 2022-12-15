from tests.api import PetFriends
from tests.settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
#проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key

# Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

# Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result

# Проверяем что запрос всех питомцев возвращает не пустой список
def test_get_all_pets_with_valid_key(filter='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)# Получаем api-ключ и сохраняем в auth_key
    status, result = pf.get_list_of_pets(auth_key, filter)# Получаем список всех питомцев и проверяем что список не пустой

    assert status == 200
    assert len(result['pets']) > 0

# Проверяем что можно добавить изображение питомца и сохраняем в переменную pet_photo
def test_add_new_pet_with_valid_data(name='Акс', animal_type='аксолотль',
                                     age='4', pet_photo='images/axalotl.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученный ответ с ожидаемым
    assert status == 200
    assert result['name'] == name

# Проверяем возможжность удаления питомца
def test_successful_delete_self_pet():
    # Запрашиваем ключ api и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
# Если список пуст - добавляем нового питомцаи опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Акс", "аксолотль", "4", "images/axalotl.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
# запрашиваем список еще раз
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # проверяем статус 200
    assert status == 200
    assert pet_id not in my_pets.values()
# Проверяем возможность обновления инфо о питомце
def test_successful_update_self_pet_info(name='Шмурзик', animal_type='аксалотль', age=3):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")





