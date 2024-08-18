pipeline {
    agent { label 'build-agent' }  // 使用 build-agent 作為運行節點

    environment {
        POETRY_HOME = "${HOME}/.poetry"  // Poetry 的安裝路徑
        PATH = "${POETRY_HOME}/bin:${PATH}"  // 將 Poetry 加入 PATH
    }

    stages {
        stage('Checkout') {
            steps {
                // 拉取代碼
                git branch: 'main', 
                    url: 'https://github.com/CHTTCH/Practice_CI_CD.git'
            }
        }

        stage('Install Python 3') {
            steps {
                script {
                    // 更新包列表並安裝 Python 3 和 pip
                    sh 'docker exec -u root <container_name> apt-get update && apt-get install -y python3 python3-pip'
                }
                }
            }
        }

        stage('Install Poetry') {
            steps {
                // 安裝 Poetry（如果尚未安裝）
                sh 'curl -sSL https://install.python-poetry.org | python3 -'
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
            // 如果有其他清理步驟，可以在這裡添加
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'One or more tests failed.'
        }
    }
}
