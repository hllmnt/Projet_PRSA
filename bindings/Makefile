all: install

build:
	python3 setup.py build

install: build
	python3 setup.py install --user

.PHONY: all clean

clean:
	rm -rf build package_*