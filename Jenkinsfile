pipeline {
    agent any

    stages {
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
                sh '''
                trivy image order-service:latest || true
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                echo "Stopping exisiting container if it exists...."
                docker stop orderservice || true
                docker rm orderservice || true
                
                docker rm -f order-service || true
                docker run -d -p 5000:5000 --name orderservice order-service:latest
                '''
            }
        }
    }
}

