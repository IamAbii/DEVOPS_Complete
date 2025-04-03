pipeline{
    agent{
        label "Jenkins-Agent"
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

        stage("Build Frontend"){
            steps {
                sh 'cd frontend && npm install && npm run build'
            }   
        }

        stage("Build Backend"){
            steps {
                sh 'cd backend && pip install -r requirements.txt'
            }   
        }
    
}
}
