@Library('local-shared-library') _
loadLocalLibrary scm, "library-folder"

pipeline {
  
  agent any
  
  stages {

    stage('Start') {
      steps {
        script {
          echo 'lets get started here ...'
        
	  def externalMethod = load('localFunc.groovy')
	  def x = externalMethod.methodA()
	  echo x.toString()
	  externalMethod.methodB("say something there")
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
    stage('Library') {
      steps {
	aUsefulFunc "i would like to send you thing"
      }
    }
  }
}

