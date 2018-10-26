properties(
    [
        [$class: 'BuildDiscarderProperty', strategy: [$class: 'LogRotator', artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '10']]
    ]
);

node {
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
        cleanWs()
    }
}