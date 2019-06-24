pipeline{
    agent {
        docker { 
            image 'python:3.7.3'
        }  
    }
    stages{
        stage('build'){
            echo "building..."
            sh "pip3 install requests"
        }
        stage("Unit Test"){
            steps{
                echo "Unit test unit"
                sh "python3 ./test.py"
                echo "Unit test finish"  
            }
        }
    }
}