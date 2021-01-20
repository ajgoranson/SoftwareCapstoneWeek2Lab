# create a student dataclass with student objects 

#import the dataclass
from dataclasses import dataclass


# Initialize the data class (This will produce its own __init__ and __str__ methods using the given data)
# This may be useful when creating a more simple class like this one, where you may not care about the formatting as much
# This is also used in more simple classes because it does not initalize empty lists automatically if you want that done you will have todo it yourself
@dataclass
class Students:
   
    name: str
    school_id: str
    gpa: float

#createing a main method with student data
def main():
    #adding an example student to the students class
    alex = Students('Alex', 'aksdef', 4.0)

    #this will just print his name
    print(alex.name)

    # this will just print his school id
    print(alex.school_id)

    #this will print both using the dataclasses premade __str__ method
    print(alex)

    # another example student to show it works with different data
    aj = Students('AJ', 'sjdf83', 3.4)
    print(aj)

#call the main method    
main()