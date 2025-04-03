pipeline{
    agent{
        label "Jenkins-Agent"
    }
    stages{
        stage("Clean Workspace"){
            steps {
                cleanws()
            }   
        }
        stage("Checkout Code"){
            steps {
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/IamAbii/DEVOPS_Complete.git'
            }   
        }
    
}
}
