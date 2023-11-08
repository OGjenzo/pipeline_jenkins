pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.10'
        VIRTUAL_ENV = "${WORKSPACE}/venv"
        DOCKER_REGISTRY = 'https://hub.docker.com/r/kbenalaya/'
        IMAGE_NAME = 'cocadminapp'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout ' ) {
            steps {
                script {
                    git credentialsId: 'khalil.benalaya@outlook.com', url: 'https://github.com/OGjenzo/pipeline_jenkins.git', branch: 'main'
                }
            }
        }
        
        stage('Optimize Assets') {
            steps {
                echo 'Optimisation des assets...'
                // Implement asset optimization tasks here if needed
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                script {
                    sh "docker login -u kbenalaya -p dckr_pat_i-2CAACDgCxHKNY-76m6usGLVX0 docker.io"
                    sh "docker build -t kbenalaya/cocadminapp:${BUILD_NUMBER} ."
                    sh "docker push kbenalaya/cocadminapp:${BUILD_NUMBER}"
                }
                echo 'Construction et Push de l\'image Docker...'
            }
        }     
        
        stage('Run Unit and Functional Tests') {
            steps {
                echo 'Run Unit and Functional Tests...'
                
                sh "docker-compose up -d"
                sh "${VIRTUAL_ENV}/bin/python -m pip install -r requirements.txt"
                sh "docker-compose down"
                //sh "${VIRTUAL_ENV}/bin/python -m pytest"   
                
            }
        }
        
        stage('Deploy to Production Server') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                echo 'Deploying to production server...'
                script {
                    sshagent(credentials: ['541a6150-d9f9-48fc-8239-eed84cfc9e8c']) {
                        sh """
                            ssh ogjenzo@4.178.97.244 'echo "Deployment command" && whoami && docker-compose down && pwd  '
                            
                        
                        """
                        // Pull the appropriate image based on the BUILD_NUMBER
                        sh """
                            ssh ogjenzo@4.178.97.244 'docker pull kbenalaya/cocadminapp:${BUILD_NUMBER}' 
                            
                        """
                        sh """
                            ssh ogjenzo@4.178.97.244 'cd /home/ogjenzo && git clone https://github.com/OGjenzo/pipeline_jenkins.git' 
                            
                        """
                                // Run Docker Compose with the specific image version
                        sh """
                            ssh ogjenzo@4.178.97.244 'cd /home/ogjenzo/pipeline_jenkins && docker-compose up -d'
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Build and test successful!'

            emailext(
                subject: "Build and Test Successful",
                body: "The build and test process was successful. Deployment to production is complete.",
                to: "khalil.benalaya@outlook.com", // Specify the recipient email address
                attachLog: true
            )
        }
        
        failure {
            echo 'Build or test failed!'

            emailext(
                subject: "Build and Test Failed",
                body: "The build and test process failed. Please check your code. Good luck :).",
                to: "khalil.benalaya@outlook.com", // Specify the recipient email address
                attachLog: true
            )
        }
    }
}
