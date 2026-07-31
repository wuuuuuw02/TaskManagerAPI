# Task Manager API

RESTful API для управления личными задачами, построенный на **Django REST Framework**.  
Позволяет создавать, просматривать и обновлять задачи с полной изоляцией данных между пользователями.

![CI](https://github.com/wuuuuuw02/TaskManagerAPI/actions/workflows/ci.yml/badge.svg)

## ✨ Основные возможности

- 🔐 **JWT-аутентификация** (через `djangorestframework-simplejwt`)
- 🛡️ **Безопасность**: пользователь видит и редактирует только свои задачи
- 📝 **Валидация данных**: заголовок ≥5 символов, описание ≥10 символов
- 🧪 **Тестирование**: покрытие ключевых сценариев (аноним, чужие задачи, валидация)
- 📚 **Автоматическая документация**: Swagger UI с поддержкой авторизации
- 🔄 **CI/CD**: автоматические тесты при каждом коммите (GitHub Actions)

## 🚀 Быстрый запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/ваш-логин/taskmanager-api.git
cd taskmanager-api

# 2. Установить зависимости
pip install -r requirements.txt

# 3. Выполнить миграции
python manage.py migrate

# 4. Запустить сервер
python manage.py runserver