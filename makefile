file = script_mine
make:
	python main.py $(file)
clean:
	rm *.pyc
	rm *.ppm
