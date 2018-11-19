# Paranuara

> A code assignment for Hivery job interview https://github.com/joaosgreccia/hivery-backend-challenge

### Installation

This program requires Python 3.5 or above to run.

1. Some requirements:

    Install pip, if you don't already have:
    
    ```commandline
    easy_install pip
    ```
    
    Install virtualenv if you don't already have
    
    ```commandline
    pip3 install virtualenv
    ```
 
 2. Choose a folder to install Paranuara. Create and activate new virtualenv.
    
    On Unix:
    
    ```commandline
    virtualenv myenv
    source myenv/bin/activate
    ```
    
    On Windows:
    
    ```commandline
    virtualenv myenv
    myenv\scripts\activate
    ```
 3. Install Paranuara

    ```commandline
    pip install https://github.com/govorunov/paranuara/archive/master.zip
    ```

    This will add `paranuara` command to the console, which offers same syntax one 
    could expect from `python manage.py` script.

 4. Run these commands to instantiate new paranuara application:

    ```commandline
    paranuara migrate
    paranuara loaddata assignment
    paranuara runserver
    ```
Then navigate to http://localhost:8000 

### Usage

* To wipe database and import new JSON data use following commands:

    ```commandline
    paranuara flush
    paranuara load_companies companies.json
    paranuara load_people people.json
    ```

    Where `companies.json` and `people.json` are locations to JSON files containing new 
    data to import. JSON files should be in the format specified in the original 
    assignment.
    
* To run tests:

    ```commandline
    paranuara test paranuara
    ``` 

## Rest API endpoints:

1. http://localhost:8000/api/employees/1/
    
    Given a company (index), returns all its employees.
    Where `1` is index of the company as specified in source data.
    
2. http://localhost:8000/api/twopeople/1/2/
    
    Given 2 people, provides their information (Name, Age, Address, phone) and 
    the list of their friends in common which have brown eyes and are still alive.
    Where `1` and `2` are indexes of people as specified in source data.
    
3. http://localhost:8000/api/fruits_and_vegetables/1/
    
    Given 1 person, provides a list of fruits and vegetables they like. This endpoint
    respects this interface for the output:
    ```json
    {"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}
    ```