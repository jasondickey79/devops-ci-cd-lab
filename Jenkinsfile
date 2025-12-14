pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/jasondickey79/devops-ci-cd-lab.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest flask'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t order-service:latest .'
            }
        }
        
        stage('Security Scan') {
            steps {
                sh 'trivy image order-service:latest || true'
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                docker rm -f order-service || true
                docker run -d -p 5000:5000 --name orderservice order-service:latest
                '''
            }
        }
    }
}

