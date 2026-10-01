pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Student Registration Web Application...'

                bat '''
                    if not exist index.html exit /b 1
                    if not exist style.css exit /b 1
                    if not exist script.js exit /b 1
                '''

                echo 'HTML, CSS and JavaScript files found.'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'

                bat 'python test.py'
            }
        }
    }

    post {
        success {
            echo 'Build and Test completed successfully!'
        }

        failure {
            echo 'Build or Test failed!'
        }
    }
}