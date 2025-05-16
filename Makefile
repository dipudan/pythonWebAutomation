run-test:
	python -m pytest --alluredir allure-results

generate-report:
	allure generate --single-file --clean allure-results -o allure-report

requirement:
	pip install -r requirements.txt

flake8:
	flake8 .

install-allure:
	sudo apt-get update
	sudo apt-get install -y openjdk-11-jdk
	wget https://github.com/allure-framework/allure2/releases/download/2.24.1/allure-2.24.1.tgz
	tar -zxvf allure-2.24.1.tgz
	sudo mv allure-2.24.1 /opt/allure
	sudo ln -s /opt/allure/bin/allure /usr/bin/allure
	echo "/opt/allure/bin" >> $GITHUB_PATH

