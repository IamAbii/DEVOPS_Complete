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
	  stage("Trivy Scan") {
             steps {
                 script {
                     def images = ["${FRONTEND_IMAGE}:${IMAGE_TAG}", "${BACKEND_IMAGE}:${IMAGE_TAG}"]
                     def trivyVersion = "aquasec/trivy:0.49.1"

                     images.each { image ->
                        def imageName = image.replaceAll("[/:]", "_")
                        def reportFile = "${imageName}_trivy_report.txt"

                        echo "🔍 Scanning Image: ${image}"
                
                        sh """
                            docker run --rm \
                            -v /var/run/docker.sock:/var/run/docker.sock \
                            -v \$(pwd):/root/reports \
                            ${trivyVersion} image ${image} \
                            --no-progress \
                            --scanners vuln \
                            --exit-code 0 \
                            -severity HIGH,CRITICAL \
                            --format table > /root/reports/${reportFile}
                        """

                        echo "📄 Trivy report saved: ${reportFile}"
                 }

            // Archive all Trivy reports for Jenkins UI
            archiveArtifacts artifacts: '*_trivy_report.txt', allowEmptyArchive: true
            }   
    }
}


    
}
}
