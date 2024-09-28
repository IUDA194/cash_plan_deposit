FROM python:3.11

# Устанавливаем переменную среды для запуска в режиме неинтерактивного режима
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект в контейнер
COPY . /app/

# Запускаем команду для запуска сервера Django
CMD python main.py