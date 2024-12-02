import sender_stand_request
import data
def test_create_user_has_number_in_first_name_get_error_response():
    user_body = negative_assert_symbol("!@#$%")
    user_response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Имя пользователя введено некорректно. " \
                                         "Имя может содержать только русские или латинские буквы, " \
                                         "длина должна быть не менее 2 и не более 15 символов"