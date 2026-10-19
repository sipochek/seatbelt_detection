## Инструкция по запуску

Для запуска скрипта выполните следующие шаги в терминале из корневой папки проекта:

1. Создайте виртуальное окружение:
   python -m venv venv

2. Активируйте виртуальное окружение:
   - Для Windows (CMD/PowerShell):
     venv\Scripts\activate
   - Для macOS/Linux:
     source venv/bin/activate

3. При помощи скрипта скачайте baseml:
   python setup.py

4. Установите необходимые зависимости:
   pip install -r requirements.txt

5. Запустите основной скрипт:
   python main.py