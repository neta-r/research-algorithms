# in order to go over all permutation I uses binary addition
# for example if the list is [1,2,3]
# the string '010' will represent the sublist [2]
# the stop string in this case will be "1000"
class bounded_subset:
    def __init__(self, lst: list, C: int):
        self.c = C
        self.lst = lst
        self.rep = ""  # a string that represents the next permutation
        st = "1"  # a string that represents the first "illegal" permutation
        self.stop = st.ljust(len(lst)+1, '0')  # padding with 0's
        self.rep = st.ljust(len(lst)+1, '0')[1:]  # creating first representation 0000..0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.lst) == 0:
            raise StopIteration
        next_iter = True  # another iteration or found a solution in this one ?
        while next_iter:
            next_iter = False
            self.rep = bin(int(self.rep, 2) + 1)[2:]  # binary addition
            bin_str = self.rep.zfill(len(self.lst))  # creating current representation
            if bin_str == self.stop:
                raise StopIteration
            temp_sum = 0  # summing as we're going
            temp_lst = []  # creating list as we're going
            for i in range(len(self.lst)):
                if bin_str[i] != "0":  # is the current char in the current permutation ?
                    temp_sum = temp_sum + self.lst[i]
                    temp_lst.append(self.lst[i])
                    if temp_sum > self.c:  # break if current sum is too big !
                        next_iter = True
                        break
            if not next_iter:
                return temp_lst


# will print [3], [2], [1], [1, 3], [1, 2]
for s in bounded_subset([1, 2, 3], 4):
    print(s)

print("------------------")
# will print [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]
for s in bounded_subset([1, 2, 3], 8):
    print(s)

print("------------------")
# will print [1], [2], [1], [1, 1]
for s in bounded_subset([1, 2, 1], 2):
    print(s)

print("------------------")
# will print [32], [4], [1], [1, 32], [1, 4]
for s in bounded_subset([1, 100, 88, 4, 92, 32], 33):
    print(s)
