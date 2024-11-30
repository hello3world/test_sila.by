После клонирования проекта выполните следующие шаги для настройки виртуального окружения и установки зависимостей.

1. Активируйте виртуальное окружение:
#### На Windows:
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

#### На Linux и macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Либо: В PyCharm

    Откройте настройки проекта:
        Перейдите в File > Settings (или Ctrl+Alt+S).
        Перейдите в Project: <ваш проект> > Python Interpreter.
        Нажмите на кнопку Add Interpreter.
        Потом Add local interpreter.
        Выбираем нужную версию питона и нажимаем OK.
        Нажимаем Apply и OK.
Если в терминале перед вашим проектом не стоит (.venv), то запустите его командой:
#### На Windows:
```bash
.\.venv\Scripts\activate
```

#### На Linux и macOS:
```bash
source .venv/bin/activate
```


2. Установите зависимости:
```bash
pip install -r requirements.txt
```
