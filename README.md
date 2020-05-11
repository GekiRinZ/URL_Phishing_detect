
###Step1
pip install -r requirements.txt

###Step2
Modify "WORKING_PATH" variable in file feature_extraction.py to your current working directory (go to your current working dir, use "pwd" command)

###Step3
python train.py -> best optimal score (no need, already trained to the maximum score)

###Step4
Enable Chromium Extension Developer Mode, Load Unpack -> Extension folder

###Step5
python app.py (run the backend server)


Test the endpoint with postman

body data(JSON)
{"url":"https://github.com/mathiznogoud/"}


### 403 ERROR BACKEND
Solution: Restart Chromium web browser, delete the extension and add it again
GL&HF
