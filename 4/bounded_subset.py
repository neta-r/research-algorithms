class bounded_subset:
    def __init__(self, lst: list, C: int):
        self.c = C
        self.obj = lst
        self.start = 0
        self.end = 1
        self.group_size = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.group_size > len(self.obj):
            raise StopIteration
        while True:
            temp_sum = sum(self.obj[self.start: self.end])
            temp_group = self.obj[self.start: self.end]
            if self.start + self.group_size >= len(self.obj):
                self.group_size = self.group_size + 1
                self.start = 0
                self.end = self.group_size
            else:
                self.start = self.start + 1
                self.end = self.start + self.group_size
            # if temp_sum <= self.c:
            #     return temp_group
            return temp_group


for s in bounded_subset([1, 2, 3, 1], 4):
    print(s)


