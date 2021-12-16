test:
	nohup python tests/get_html_file.py &
	pytest -v
	ps aux|tests/get_html_file.py|awk '{print $2}'|xargs kill -9
req:
	pip install -r requirements.txt
