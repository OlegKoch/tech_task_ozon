# Tech task Ozon Банк

# Создать виртуальное окружение:.
    python -m venv venv

# Активировать виртуальное окружение:
    source venv/Scripts/activate

# Установить модули из файла requirementst.txt: 
    pip install -r requirements.txt

# Из корня проекта (где находится api.py и папка tests/) запустите команду:
    pytest -v

# Пример успешной работы тестов:
    tests/test_hero.py::test_high_male_with_work PASSED                                                                                                                                                                            [ 16%] 
    tests/test_hero.py::test_high_female_with_work PASSED                                                                                                                                                                          [ 33%] 
    tests/test_hero.py::test_high_male_without_work PASSED                                                                                                                                                                         [ 50%] 
    tests/test_hero.py::test_high_female_without_work PASSED                                                                                                                                                                       [ 66%] 
    tests/test_hero.py::test_empty_list PASSED                                                                                                                                                                                     [ 83%] 
     
