import models
from datetime import datetime
from uuid import uuid4

class BaseModel():
    """
    Class base model defines all common attributes for other classes

    """

    def __init__(self, *args, **kwargs):

        """
        *args passes non-key arguments
        **kwargs passes key/value arguments

        """
        tform = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid4())
        self.creted_at = datetime.today()
        self.added_at = datetime.today()

        if len(kwargs) !=0:

            for key, value in kwargs.items():
                if key == "created_at" or value == " added_at":
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = value
        else:
            models.storge.new(self)

    def save(self):
        """
        updates added_at to current datetime
        """
        self.added_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
    
    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)