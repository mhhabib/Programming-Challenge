import random
import string
import enum

class ObjectTypes(enum.Enum):
    IntegerNumber=0
    RealNumber=1
    Alphanumeric=2
    Alphabetic=3

class RandomObject:
    def __init__(self):
        self.integernumber = 0
        self.realnumber = 0
        self.alphanumeric = 0
        self.alphabetic = 0
    
    def objectsCount(self, ObjectTypes):
        self.integernumber+=1 if ObjectTypes == ObjectTypes.IntegerNumber else 0
        self.realnumber+=1 if ObjectTypes == ObjectTypes.RealNumber else 0
        self.alphanumeric+=1 if ObjectTypes == ObjectTypes.Alphanumeric else 0
        self.alphabetic+=1 if ObjectTypes == ObjectTypes.Alphabetic else 0

    def __dict__(self) -> dict:
        return {'integernumber': self.integernumber, 'realnumber': self.realnumber, 'alphanumeric': self.alphanumeric, 'alphabetic': self.alphabetic}

class RandomObjectGenerator:
    def __init__(self):
        self.randomObjectsList = []
        self.randomObject = RandomObject()

    def get_random_objects(self):
        self.randomObjectsList = get_random_objects()[0]
        return self.randomObjectsList

    def get_random_object_count(self):
        self.randomObject=get_random_objects()[1]
        return self.randomObject.__dict__()



def get_random_objects():

    # The size of a list of random objects
    total_file_size = 2*1024*1024
    get_RandomObjects=""
    addNewline = False

    # count the number of objects 
    randomObject = RandomObject()
    current_file_size = 0
    
    while current_file_size < total_file_size:

        index = random.randint(4,17)
        if index % 4 == ObjectTypes.IntegerNumber.value:
            generateObject=random.randint(99,9999999).__str__()
            randomObject.objectsCount(ObjectTypes.IntegerNumber)

        elif index % 4 == ObjectTypes.RealNumber.value:
            generateObject=random.uniform(99,9999999).__str__()
            randomObject.objectsCount(ObjectTypes.RealNumber)

        elif index %4  == ObjectTypes.Alphanumeric.value:
            generateObject=''.join(random.choice(string.ascii_letters+string.digits) for i in range(7))
            randomObject.objectsCount(ObjectTypes.Alphanumeric)

        elif index %4  == ObjectTypes.Alphabetic.value:
            generateObject=''.join(random.choice(string.ascii_letters) for i in range(7))
            randomObject.objectsCount(ObjectTypes.Alphabetic)

        current_file_size +=len(generateObject)+1
        if current_file_size > total_file_size:
            break
        
        if(addNewline):
             generateObject = "," + generateObject

        addNewline = True
        get_RandomObjects +=generateObject

    return get_RandomObjects, randomObject

