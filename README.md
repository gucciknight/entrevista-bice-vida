# entrevista-bice-vida
Repositorio oficial de la opción 1 en las preguntas de desarrollo, creado por Agustín Rodríguez

### Stages de Jenkinsfile

1. **Build**
    - Construye la imagen Docker para la aplicación.
    - Comando: `docker.build("django-app")`.

2. **Test**
    - Ejecuta pruebas automatizadas dentro de un contenedor Docker.
    - Comando: `sh 'python app_project/manage.py test'`.

3. **Deploy**
    - Despliega la imagen Docker en Google Cloud.
    - Comandos:
        - `docker save django-app | bzip2 | ssh -o StrictHostKeyChecking=no ${GCLOUD_INSTANCE_NAME} "bunzip2 | docker load"`
        - `ssh -o StrictHostKeyChecking=no ${GCLOUD_INSTANCE_NAME} "docker run -d -p 8000:8000 django-app"`.
