import uuid
from datetime import datetime
import sys

sys.path.append('/home/richie/My_AirBnB/models')

class BaseModel():
    """ defines all attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4()) 
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs)!=0:
                del kwargs['__class__']
                for key, value in kwargs.items():
                    if key == 'created_at'  or 'updated_at':
                          timeobject = datetime.strftime(value, '%Y-%m-%dT%H%M%S%f')
                          setattr(self, key, timeobject)
                    else:
                         setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4()) 
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            
    
       

    def save(self):
        """ updates the public instance attribute updated_
        at with the current datetime
        """
        updated_at = datetime.now()
      
      
    def to_dict(self):
        """  returns a dictionary containing all attributes keys/values of __dict__ of the instance:
        """
        rdict = self.__dict__

        rdict['created_at'] = self.created_at.isoformat()
        rdict['updated_at'] = self.updated_at.isoformat()
        rdict['id']         = self.id
        rdict["__class__"] = self.__class__.__name__

        return rdict

    def __str__(self):
        """Returns the print/str representation of the BaseModel instance."""
        id = self.id
        class_name = self.__class__.__name__
        dict = self.__dict__

        return f'[{class_name}] ({id}) {dict}'

        