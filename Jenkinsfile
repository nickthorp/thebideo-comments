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
        sh 'make build'
    }
}