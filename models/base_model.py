
from datetime import datetime
from uuid import uuid4

class BaseModel():
    """
    Class base model defines all common attributes for other classes

    """

    def __init__(self, *args, **kwargs):
        """constructor"""

        for key, value in kwargs.item():
            if key == "__class__":
                continue

            if(key == "created_at"):
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M%S.%f")

            setattr(self,key,value)

        if "id" not in kwargs.keys():
            self.id = str(uuid4())

        if"created_at" not in kwargs.keys():
            self.create_at = datetime.now()

        if "update_at" not in kwargs.keys():
            self.updated_at = datetime.now()

        if len(kwargs) == 0:
            storage.new(self)

    def __Str__(self):
    
    
        """defines what should be printed for each instances of the class"""
        st = "[{:S}] ({:S}) {:S}"
    
    def save(self):
        """
        Updateds the public instances attr updated_at with current datetime

        """
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of instance
        """
        dcopy =self.__dict__.copy()
        dcopy['__class__'] = self.__class__.__name__
        dcopy['created_at'] = self.created_at.isoformat()
        dcopy['updated_at'] = self.updated_at.iosformat()

        return dcopy
