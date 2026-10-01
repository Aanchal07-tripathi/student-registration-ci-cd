pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Student Registration Project...'

                bat '''
                    if not exist index.html exit /b 1
                '''

                echo 'HTML file found successfully.'
            }
        }

        stage('Test') {
            steps {
                echo 'Running HTML tests...'

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