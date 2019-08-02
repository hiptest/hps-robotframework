default: test
.PHONY: default

install_prerequisites:
	pip install robotframework
.PHONY: install_prerequisites

generate_tests:
	hiptest-publisher -c robotframework.conf -t "$(SECRET_TOKEN)" --without=actionwords
.PHONY: generate_tests

test: install_prerequisites
	robot -P src:tests --loglevel=DEBUG tests
.PHONY: test
