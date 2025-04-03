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
    
}
}
