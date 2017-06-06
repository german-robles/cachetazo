build:
	docker-compose build --pull

testing:
	docker run -ti -v ${PWD}:/usr/src/app cachetazo_cachetazo python -m pytest -vv --cov-report html:report_html --cov-report term-missing --cov=app test
