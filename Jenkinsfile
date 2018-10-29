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
        /*
        stage('Install') {
            dir('./vdist') {
                sh "rpm -Uvh thebideo-comments-1.$BUILD_NUMBER-1.x86_64.rpm"
            }
        }
        */
        stage('Archive') {
            archiveArtifacts artifacts: 'vdist/*', onlyIfSuccessful: true
        }
    } catch(Exception e) {
    
    } finally {
        stage('Notify') {
            slackNotifier(currentBuild.currentResult)
            cleanWs()
        }
    }
}