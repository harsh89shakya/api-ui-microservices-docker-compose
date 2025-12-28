pipeline {
  agent any
  environment {
    DOCKER_CREDS = credentials('docker-hub-cred')
  }
  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/harsh89shakya/api-ui-microservices-docker-compose.git'
      }
    }
    stage('Build Images') {
      steps {
          bat 'docker compose build'
      }
    }
    stage('Tag') {
      steps {
            bat 'docker tag api-ui-microservices-docker-compose_api-services:latest harsh89shakya/api-services:latest'
            bat 'docker tag api-ui-microservices-docker-compose_ui-services:latest harsh89shakya/ui-services:latest'
            }
        }
    stage('Login to DockerHub') {
      steps {
          bat 'docker login -u %DOCKER_CREDS_USR% -p %DOCKER_CREDS_PSW%'
        }
      }
    stage('Push to Docker Hub') {
      steps {
          bat 'docker push harsh89shakya/api-services:latest'
          bat 'docker push harsh89shakya/ui-services:latest'
        }
      }
    stage('Deploy') {
      steps {
        script {
          bat 'docker compose up -d'
        }
      }
    }
  }
}