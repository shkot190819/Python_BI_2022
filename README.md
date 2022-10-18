# HW3. Modules and virtual environments
Kubuntu 22.04.1 LTS
python 3.10

**User guide for running file:**
1. update local apt package index and then download and install packages\
`sudo apt update`
2. installing pip and python header files\
`sudo apt install python3-pip python3-dev`
3. python virtual environment setup\
`sudo -H pip3 install --upgrade pip`\
`sudo -H pip3 install virtualenv`
4. create a Python virtual environment in the project directory and activate it\
`virtualenv pyth2`\
`source pyth2/bin/activate`
5. i tested the program through jupiter, so I installed it in a virtual environment (but you need to run the program itself in the terminal, so this is not necessary)\
`pip install jupyter`
6. installing packages via requirement.txt or manual installation\
a. via requirement.txt file (attached):\
`pip install -r requirements.txt`\
b. manual installation:\
`pip install -Iv biopython==1.77`\
`pip install google-api-python-client`\
`pip install python-math`\
`pip install typing`\
`pip install kiwy`\
`pip install bs4`\
`pip install aiohttp`\
`pip install pandas`\
`pip install scipy`\
`pip install scanpy`\
`pip install parser-libraries`\
`pip install lxml`\
`pip install opencv-python`
7. copy the file pain.py to the working directory with the active virtual environment
8. make the file executable\
`chmod +x pain.py`
9. run file\
`python3 pain.py`
