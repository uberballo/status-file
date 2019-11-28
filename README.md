# Reaktor-pre-assignment 

[Heroku](https://thawing-ravine-57333.herokuapp.com/)  

## How to use  
You can either choose the default status file by clicking `Default status` or you may upload your own status file, which can be found from `/var/lib/dpkg/status`.  
When file has been loaded and parsed, you may browse all packages found from the status.  
You can see more information by clicking the package name.  

## How to install
* Make sure to have the latest verison of Python 3, python3-venv, and pip.
* Download the program either trough `git clone <link>` or trough Github.
* Unzip the program folder if needed and make it your current working directory.
* Make virtual environment with  
`python3 -m venv venv`  
* Add the new environment as your source with  
`source venv/bin/activate`  
* Install required libraries with the command  
`pip install -r requirements.txt`  
* Run the application with  
`python3 run.py` 

## Tests
* Use the virtual environment.  
* Run tests with  
`pytest` 

