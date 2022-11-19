# Инструкция по запуску для ОС - Ubuntu 22.04.1 LTS.

1. Клонируем проект в нужную папку: 
  $ git clone https://github.com/Fischer0007/system_technik_tests.git <Имя папки>
  
2. Переходим в директорию с тестом: 
  $ cd system_technik_tests
  
3. Установим инструмент для управления пакетами pip: 
  $ sudo apt install -y python3-pip 
  
3. Устанавливаем необходимые библиотеки Python:
  $ pip3 install -r req.txt
  
4. Запускаем тест с отчетом в консоли: 
  $ python3 -m pytest -rqpP script.py
