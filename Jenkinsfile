pipeline {
    agent any
    environment {
        SSH_CREDENTIALS = credentials('ssh-bicevida') // Utiliza el ID de tu credencial SSH aquí
        GCLOUD_PROJECT = 'entrevista-bice-vida'
        GCLOUD_COMPUTE_ZONE = 'us-west1-b'
        GCLOUD_INSTANCE_NAME = 'bicevidamachine'
    }
    stages {
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build("django-app")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'python app_project/manage.py test'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                sshagent(['jenkins-ssh-key']) {
                    sh '''
                    gcloud config set project ${GCLOUD_PROJECT}
                    gcloud config set compute/zone ${GCLOUD_COMPUTE_ZONE}
                    docker save django-app | bzip2 | ssh -o StrictHostKeyChecking=no ${GCLOUD_INSTANCE_NAME} "bunzip2 | docker load"
                    ssh -o StrictHostKeyChecking=no ${GCLOUD_INSTANCE_NAME} "docker run -d -p 8000:8000 django-app"
                    '''
                }
            }
        }
    }
}
