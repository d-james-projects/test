pipeline {
  
  agent any
  
  stages {

    stage('Start') {
      steps {
        script {
          echo 'lets get started here ...'
        }
      }
    }
    stage('Test') {
      steps {
        script {
          sh 'ls -al && whoami'
        }
      }
    }
  }
}

