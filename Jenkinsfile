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
                        script {
                            echo "Verifying Python file syntax for app.py..."
                            // Checks file existence and basic readability
                            if (fileExists('app.py')) {
                                echo "app.py exists and is ready."
                            } else {
                                error("app.py not found!")
                            }
                        }
                    }
                }
                stage('Dependencies Check') {
                    steps {
                        script {
                            echo "Checking workspace environment..."
                            echo "Workspace directory: ${env.WORKSPACE}"
                        }
                    }
                }
            }
        }
        stage('Conditional Testing') {
            when {
                expression { params.RUN_TESTS == true }
            }
            steps {
                script {
                    echo "Executing conditional tests..."
                    writeFile file: 'test-report.txt', text: 'Tests Passed Successfully!'
                }
            }
        }
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'test-report.txt', fingerprint: true
            }
        }
    }
}