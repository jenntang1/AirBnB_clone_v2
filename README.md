# HBNB

This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON file, and retrieve objects from a database. The repository also contains script to setup a database with the required parameters for the interpreter to work.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

#### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, 
            or all objects of a given class

    * update - Updates existing attributes an object based 
               on class name and UUID

    * quit - Exits the program (EOF will as well)

To start, navigate to the project folder and enter `./console.py` in the shell.

### Command Examples:
##### Create
`create <class name>`
Ex:
`create BaseModel`

##### Show
`show <class name> <object id>`
Ex:
`show User my_id`

##### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

##### All
`all` or `all <class name>`
Ex:
`all` or `all State`

##### Quit
`quit` or `EOF`

##### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`
