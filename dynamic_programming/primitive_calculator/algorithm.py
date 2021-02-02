class Algorithm:
    """ 
    Defines algorithm object

    Attrs:
        name (string) - Name of algorithm
        algorithm (function) - agorithm passed in at construction, called when use method called
     """

    def __init__(self, name, implementation):
        self.name = name
        self.result = None
        self.algorithm = implementation

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def get_latest_result(self):
        return self.__result

    def set_latest_result(self, result):
        self.__result = result

    def use(self, *args, **kwargs):
        """
        Use the algorithm passed in at creation time

        Params:
            Any number of arguments used in the algorithm

        Returns:
            Value of the data returned by the algorithm

         """
        result = self.algorithm(self, *args, **kwargs)
        self.set_latest_result(result)

        return result

