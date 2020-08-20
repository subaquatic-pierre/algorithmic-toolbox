class AlgorithmTestStress(AlgorithmTestStressBase):
    """ Stress test to run against algorithms
    Params:
        algorithms (list) : list of algorithms to run against test data
        data_size (integer) : maximum size of data set to use for test
        max_value (integer) : maximum value to be used in a data point within the data set
     """

    random.seed(1)

    def build_data(self, **kwargs):
        data = {"awesome": True}

        return data
