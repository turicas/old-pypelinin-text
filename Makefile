test:
	nosetests --with-coverage --cover-package pypelinin tests/test_*.py

clean:
	find -regex '.*\.pyc' -exec rm {} \;

.PHONY: test clean
