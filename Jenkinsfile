pipeline {
    agent any

    environment {
        KUBECONFIG = '/var/lib/jenkins/.kube/config'
    }

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

        stage('Load Image into Minikube') {
            steps {
                sh '/usr/local/bin/minikube image load cloud-cicd-lab:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    /usr/bin/kubectl apply -f k8s/deployment.yaml
                    /usr/bin/kubectl apply -f k8s/service.yaml
                    /usr/bin/kubectl rollout status deployment/cloud-cicd-app --timeout=120s
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    /usr/bin/kubectl get deployment cloud-cicd-app
                    /usr/bin/kubectl get pods -l app=cloud-cicd-app
                    /usr/bin/kubectl get service cloud-cicd-service
                '''
            }
        }
    }
}
