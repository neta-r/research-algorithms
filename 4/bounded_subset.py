class bounded_subset:
    def __init__(self, lst: list, C: int):
        self.c = C
        self.lst = lst
        self.appear = ""
        self.stop = "1"
        for _ in range(len(lst)):
            self.appear = self.appear + "0"
            self.stop = self.stop + "0"

    def __iter__(self):
        return self

    def __next__(self):
        con_to_next_iter = True
        while con_to_next_iter:
            con_to_next_iter = False
            self.appear = bin(int(self.appear, 2) + 1)[2:]
            bin_str = self.appear.zfill(len(self.lst))
            if bin_str == self.stop:
                raise StopIteration
            temp_sum = 0
            temp_lst = []
            for i in range(len(self.lst)):
                if bin_str[i] != "0":
                    temp_sum = temp_sum + self.lst[i]
                    temp_lst.append(self.lst[i])
                    if temp_sum > self.c:
                        con_to_next_iter = True
                        break
            if not con_to_next_iter:
                return temp_lst


for s in bounded_subset([1, 2, 3, 1], 4):
    print(s)


