FROM python:3.9.15-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py makemigrations
RUN python manage.py makemigrations links
RUN python manage.py migrate
EXPOSE 8000  
# CMD [ "python", "manage.py", "runserver"]