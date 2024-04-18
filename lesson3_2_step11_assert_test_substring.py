

# вариант с assert и , f в одну строку
def test_input_text(expected_result, actual_result):
    assert (expected_result == actual_result), f"expected {expected_result}, got {actual_result}"

# вариант с assert и , f в 2 строки
def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, \
        f"expected {expected_result}, got {actual_result}"

# вариант с .format()
def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, "expected {}, got {}".format(expected_result, actual_result)

# вариант без assert
def test_input_text(expected_result, actual_result):
    if expected_result!=actual_result:
        print("expected "+ expected_result+", got "+ actual_result)
    # ваша реализация, напишите assert и сообщение об ошибке

