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
    }
   // post {
     //   success {
       //     build job: 'gitops-CD', parameters: [
         //       string(name: 'IMAGE_TAG', value: env.IMAGE_TAG)
           // ]
      //  }
  //  }
}
