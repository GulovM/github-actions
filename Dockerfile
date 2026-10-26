# Базовый образ Python (slim для уменьшения размера и ускорения сборки)
FROM python:3.11-slim

# Отключаем буферизацию вывода и генерацию .pyc файлов
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Сначала копируем только зависимости для эффективного кэширования слоев Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь исходный код
COPY . .

# Команда запуска контейнера
CMD ["python", "app.py"]

