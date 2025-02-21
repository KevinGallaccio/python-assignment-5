
class CustomList:
    def __init__(self):
        self.list_size = 0
        self.custom_list = [None] * 10


    def add (self, item):
        if self.list_size == len(self.custom_list):
            self.__resize()
        self.custom_list[self.list_size] = item
        self.list_size += 1

    def size(self):
        return self.list_size

    def get(self, index):
        return self.custom_list[index]

    def __resize(self):
        resized_list = [None] * (len(self.custom_list) * 2)
        for i in range(len(self.custom_list)):
            resized_list[i] = self.custom_list[i]
        self.custom_list = resized_list

    def __repr__(self):
        return f'{self.custom_list[:self.list_size]}'