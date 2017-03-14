rm -rf .coverage
nosetests -sv --nocapture --nologcapture --with-coverage --cover-package=operation

rm -rf coverage.svg
coverage-badge -o coverage.svg
