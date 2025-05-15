run-test:
	python -m pytest --alluredir allure-results

generate-report:
	allure generate --single-file --clean allure-results

