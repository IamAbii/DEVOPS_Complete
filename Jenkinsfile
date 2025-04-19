pipeline {
    agent {
        label "Jenkins-Agent"
    }
    environment {
        RELEASE = "1.0.0"
        IMAGE_TAG = "${RELEASE}-${BUILD_NUMBER}"
        DOCKER_USER = "abhilash2"
        DOCKER_PASS = "dockerhub"
        FRONTEND_IMAGE = "${DOCKER_USER}/frontend-app"
        BACKEND_IMAGE = "${DOCKER_USER}/backend-app"
        JENKINS_API_TOKEN = credentials("JENKINS_API_TOKEN")
    }

    stages {

        stage("Clean Workspace") {
            steps {
                cleanWs()
            }
        }

        stage("Checkout Code") {
            steps {
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/IamAbii/DEVOPS_Complete.git'
            }
        }

        stage('Build & Push Docker Images') {
            steps {
                script {
                    docker.withRegistry('', DOCKER_PASS) {
                        def frontend_image = docker.build("${FRONTEND_IMAGE}:${IMAGE_TAG}", "frontend")
                        def backend_image = docker.build("${BACKEND_IMAGE}:${IMAGE_TAG}", "backend")

                        frontend_image.push("${IMAGE_TAG}")
                        backend_image.push("${IMAGE_TAG}")
                    }
                }
            }
        }

        stage("Trigger CD Pipeline") {
            steps {
                script {
                    withCredentials([string(credentialsId: 'JENKINS_API_TOKEN', variable: 'API_TOKEN')]) {
                        sh """
                            CRUMB_JSON=\$(curl -s -u abhilash2:\$API_TOKEN http://ec2-3-110-46-176.ap-south-1.compute.amazonaws.com:8080/crumbIssuer/api/json)
                            CRUMB=\$(echo \$CRUMB_JSON | jq -r '.crumb')
                            CRUMB_FIELD=\$(echo \$CRUMB_JSON | jq -r '.crumbRequestField')

                            curl -v -X POST -u abhilash2:\$API_TOKEN \\
                                -H "\$CRUMB_FIELD: \$CRUMB" \\
                                "http://ec2-3-110-46-176.ap-south-1.compute.amazonaws.com:8080/job/gitops-CD/buildWithParameters?token=gitops-token&IMAGE_TAG=${IMAGE_TAG}"
                        """
                    }
                }
            }
        }
    }
}
