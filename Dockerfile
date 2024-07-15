FROM python:3.12-alpine
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# RUN chmod +x start.sh
CMD [ "sh", "start.sh" ]