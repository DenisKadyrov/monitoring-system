FROM python:3.8-slim

# Установка зависимостей Flask
RUN pip install Flask gunicorn

# Копирование вашего приложения в образ
COPY app.py /app.py

# Установка рабочей директории
WORKDIR /

# Запуск Gunicorn для Flask
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

