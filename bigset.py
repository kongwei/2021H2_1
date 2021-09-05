class BigSet(set):
    def to_string(self):
        data_list = list(self)
        data_list.sort()

        ret = []
        start = -1
        end = -1
        for i in data_list:
            if i == end + 1:
                end = i
            else:
                ret.append(range2string(start, end))
                start, end = i, i
        ret.append(range2string(start, end))

        return ",".join(ret[1:])

    def __or__(self, other):
        return BigSet(super().__or__(other))

    def __and__(self, other):
        return BigSet(super().__and__(other))

    def __xor__(self, other):
        return BigSet(super().__xor__(other))

    def __sub__(self, other):
        return BigSet(super().__sub__(other))


def range2string(start, end):
    if start == end:
        return str(start)
    else:
        return "%s-%s" % (start, end)
