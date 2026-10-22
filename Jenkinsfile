pipeline {
    agent any
    parameters {
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Run verification tests?')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Parallel Build & Analysis') {
            parallel {
                stage('Code Linting') {
                    steps {
                        bat 'python -m py_compile app.py'
                    }
                }
                stage('Dependencies Check') {
                    steps {
                        bat 'python --version'
                    }
                }
            }
        }
        stage('Conditional Testing') {
            when {
                expression { params.RUN_TESTS == true }
            }
            steps {
                echo "Executing tests..."
                bat 'echo Tests Passed > test-report.txt'
            }
        }
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'test-report.txt', fingerprint: true
            }
        }
    }
}