# Status-file 

[Heroku](https://thawing-ravine-57333.herokuapp.com/)  

## What, Why and How?  
The program parses status file, that contains information about your systems software packages and shows them on the website.  
This is the pre-assignment for junior dev at Reaktor.  
As the users inputs their chosen status file, we pass it to the `PackageHandler`, which produces a list of objects, that contain all required information. Name, description, dependencies, dependants and required href links. I use Flask to run the front-backend and Jinja to produce required .HTML files. Some JavaScript is used on the package.html, but it is for the sake of folding the description.  

The program starts by first going trough the given status file and produces all packages with their dependencies. After we've gone trough the file, we trim the dependency names and produce required DependencyLink-objects. This is done later, because we can't be sure if the dependency will actually exist in the status. After that we go trough the dependants. If the dependant is in the list, we add a href, otherwise we just add the name to the link. 


  
For the packages That I used:
* Flask, it is easy and fast to use and makes the routing easy and easy to unterstand.  
* Jinja, because this is made with only Python (except that one script) we can easily produce list elements with it and show info when it is present.  
* Pytest, testing is a lot easier with it. 
* Other packages are required by the previously mentioned.

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

