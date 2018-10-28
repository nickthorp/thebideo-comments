properties(
    [
        [$class: 'BuildDiscarderProperty', strategy: [$class: 'LogRotator', artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '10']]
    ]
);

node {
    try {
        stage('checkout') {
            checkout scm
        }

        stage('build') {
            sh 'chmod 755 *.sh'
            sh './make.sh init'
            sh './make.sh build'
        }
        
        stage('Cleanup') {
            archiveArtifacts artifacts: 'vdist/*', onlyIfSuccessful: true
            slackNotifier(currentBuild.currentResult)
            cleanWs()
        }
    } catch {
        stage('Notify') {
            slackNotifier(currentBuild.currentResult)
            cleanWs()
        }
    }
}