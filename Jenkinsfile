pipeline {
    agent { label 'build-agent' }  // 指定要使用的 Jenkins 節點標籤

    environment {
        POETRY_HOME = "${HOME}/.poetry"  // Poetry 的安裝路徑
        PATH = "${POETRY_HOME}/bin:${PATH}"  // 將 Poetry 加入 PATH
    }

    stages {
        stage('Checkout') {
            steps {
                // 從 GitHub 拉取代碼
                git branch: 'main', 
                    url: 'https://github.com/CHTTCH/Practice_CI_CD.git'
            }
        }

        stage('Refresh .bashrc') {
            steps {
                // 使用 Poetry 安裝依賴
                sh '. ~/.bashrc'
            }
        }

        stage('Install Dependencies') {
            steps {
                // 使用 Poetry 安裝依賴
                sh 'poetry install'
            }
        }

        stage('Run Tests') {
            steps {
                // 使用 Poetry 運行 Python 的 unittest 測試
                sh 'poetry run python -m unittest discover'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // 如果有需要的清理步驟，可以在這裡添加
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'One or more tests failed.'
        }
    }
}
