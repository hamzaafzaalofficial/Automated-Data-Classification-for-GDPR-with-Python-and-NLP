#Making python environment
mkdir test
cd test/
sudo apt update
sudo apt install python3 python3-pip python3-virtualenv
apt install python3.12-venv
source myenv/bin/activate
vi requirements.txt
# paste the content of requirements.txt
pip install -r requirements.txt
python3 -m spacy download en_core_web_sm
#Making dedicated gdpr directory 
mkdir gdpr_lab
cd gdpr_lab
nano generate_dataset.py  #use the content of the specified file
python3 generate_dataset.py # this will generate a .csv file as a dataset

#Analyzing the dataset
vi gdpr_classifier.py #use the content of the specified file
python3 gdpr_classifier.py
vi generate_reports.py #use the content of the specified file &:wq!
python3 generate_reports.py

#Scheduling the report 
#This is beneficial when your data is continously updating, otherwise this automation
#will result in same reports 
crontab -e
0 0 * * * /root/test/myenv/bin/python3 generate_reports.py 
#save :wq! or ctrl+o -> enter ->then ctrl+x

#Ideally the model was making errors that can be further fixed by tweaking.