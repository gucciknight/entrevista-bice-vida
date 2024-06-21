#se utiliza python alpine por su ligereza y se instalarán las dependencias necesarias
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1
#se define directorio de trabajo en contenedor
WORKDIR /container_app

COPY requirements.txt requirements.txt
COPY app_bicevida app_bicevida

#se instalan las dependencias necesarias de python al estilo alpine
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del build-deps

#exponemos puerto por defecto que tiene django para el deploy
EXPOSE 8000


CMD ["python", "app_bicevida/manage.py", "runserver", "0.0.0.0:8000"]
