class Car:
    def __init__(self, maker, model, **kwargs):
        """
        To make a car, accept maker, model and an arbitrary number of keyword arguments.
        Store information in a dictionary.
        """
        self.info = {"maker": maker, "model": model}

        for key in kwargs.keys():
            self.info[key] = kwargs[key]

    def show(self):
        """Print the dictionary with the car information"""
        print(self.info)
