test:
	nohup python test/get_html_file.py &
	pytest -v
req:
	pip install -r requirements.txt
