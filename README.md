# DomXSS_Detection
Static Dom XSS detector.

## Setup
### Setting up the environment

```shell
# Creating the virtual environment
python3 -m venv .env

# Activating the virtual environment
source .env/bin/activate
```

### Installing dependencies
pip3 install -r requirements.txt

### Download webdriver
- Firefox: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
- Google: https://chromedriver.chromium.org/downloads

Put in $project_dir/drivers
## Run
### scan by payload
```shell
# start a HTTP Server
python3 tests/get_html_file.py
# scan our local test HTML file by payload, 
python domxss_detect.py http://127.0.0.1:5000/LocationHashEval.html --rule payload
```
### scan by regular expression
```shell
python domxss_detect.py http://127.0.0.1:5000/LocationHashEval.html --rule reg --res_file scan_by_reg.txt
```

