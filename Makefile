default: egg

.PHONY: default egg clean

egg:
	python setup.py bdist_egg

clean:
	@rm -rf build dist lights.egg-info
	@find . -type f -name '*.pyc' -delete
