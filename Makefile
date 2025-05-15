run-test:
	python -m pytest --alluredir allure-results

generate-report:
	allure generate --single-file --clean allure-results

requirement:
	pip install -r requirements.txt

flake8:
	flake8 .

