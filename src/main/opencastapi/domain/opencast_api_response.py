class OpencastApiResponseDescriptor():
    """Directly manipulates the instance __dict__.
    """
    def __init__(self, name=None):
        """
            Input: name is the label of the thing you are storing
        """
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        #del instance.__dict__[self.name] = value
        raise AttributeError(f"Deletion of attribute {name} from {repr(instance)} not possible.")

class OpencastApiResponse():
    """Format-agnostic response object, where data can be accessed using
        object-oriented programming. In a style consistent with dict access.
        (dot notation).
    """
    def __init__(self, *args, **kwargs):
        jj
