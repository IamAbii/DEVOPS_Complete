pipeline{
    agent{
        label "Jenkins-Agent"
    }
    environment {
        RELEASE = "1.0.0"
        IMAGE_TAG = "${RELEASE}-${BUILD_NUMBER}"
        DOCKER_USER = "abhilash2"
        DOCKER_PASS = "dockerhub"
        FRONTEND_IMAGE = "${DOCKER_USER}" + "/" + "frontend-app"
        BACKEND_IMAGE = "${DOCKER_USER}" + "/" + "backend-app"
    }

    
    stages{
        
        stage("Clean Workspace"){
            steps {
                cleanWs()
            }   
        }
        
        
        stage("Checkout Code"){
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
	  stage('Trivy Scan') {
		steps {
			script {
					// Define image names
				def images = [
				"abhilash2/frontend-app:1.0.0-7",
				"abhilash2/backend-app:1.0.0-7"
				]

					// Create a local reports directory
					sh 'mkdir -p reports'

					// Loop through each image and scan
					images.each { image ->
					def safeName = image.replaceAll(/[:\/]/, "_")  // for filename safety
					echo "🔍 Scanning Image: ${image}"
					sh """
						trivy image --format table \
						--output reports/${safeName}_trivy_report.txt \
						${image}
               				 """
            }
        }
    }
}



    
}
}
