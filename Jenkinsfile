
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cloud-cicd-lab:latest .'
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    docker run --rm cloud-cicd-lab:latest python -c "from app import app; response = app.test_client().get('/'); assert response.status_code == 200; print('Application test passed')"
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker rm -f cloud-cicd-app 2>/dev/null || true
                    docker run -d \
                        --name cloud-cicd-app \
                        --restart unless-stopped \
                        -p 5000:5000 \
                        cloud-cicd-lab:latest
                '''
            }
        }
    }
}
