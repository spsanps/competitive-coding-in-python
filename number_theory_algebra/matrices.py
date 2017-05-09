class Mat:
    def __init__(self, value=None):
        self.value = value
        if value is not None:
            self.set_mn()
        else:
            self.m = 0
            self.n = 0

    def set_mn(self):
        self.m = len(self.value)
        self.n = len(self.value[0])

    def __str__(self):
        final_str = ''
        for i in xrange(self.m):
            for j in xrange(self.n):
                final_str += str(self.value[i][j]) + '\t'
            final_str += '\n'
        return final_str

    def __abs__(self):
        assert self.m == self.n
        if self.m == 1: return self.value[0][0]
        total = 0
        for i in xrange(self.m):  # Counting downwards
            new_mat_value = [self.value[j][1:] for j in xrange(0, i)] + [self.value[j][1:] for j in
                                                                         xrange(i + 1, self.m)]
            total += ((-1) ** i) * self.value[i][0] * abs(Mat(new_mat_value))

        return total

    def __add__(self, other):
        assert other.value
        assert other.m
        assert other.n

        assert self.m == other.m
        assert self.n == other.n

        new_value = [[0 for i in xrange(other.n)] for j in xrange(other.m)]

        for i in xrange(self.m):
            for j in xrange(self.n):
                new_value[i][j] = self.value[i][j] + other.value[i][j]
        return Mat(new_value)

    def __mul__(self, other):
        if type(other) is int:
            new_mat = Mat(self.value)
            new_mat.value = [[v * other for v in l] for l in new_mat.value]
            return new_mat
        else:
            new_value = [[0 for i in xrange(other.n)] for j in xrange(self.m)]
            assert self.n == other.m
            for i in xrange(self.m):
                for j in xrange(other.n):
                    new_value[i][j] = sum([self.value[i][k] * other.value[k][j] for k in xrange(self.n)])
            return Mat(new_value)

    def __sub__(self, other):
        """

        :type other: Mat
        """
        return self + other * -1

    def __pow__(self, power, modulo=None):
        assert power >= 0
        assert self.m == self.n
        m = [[0 for i in xrange(self.m)] for i in xrange(self.m)]
        for i in xrange(self.m):
            m[i][i] = 1
        new_mat = Mat(m)
        for i in xrange(power):
            new_mat = new_mat * self
        return new_mat


'''def shift_clock(matrix, point=(0, 0), depth = 0):
    n = len(matrix)
    if point == (depth, depth):
        next = (-1, depth)
    elif point == (depth, n - depth):


    m, n = point
    temp = matrix[m][n]
    matrix[m][n] = shift_clock(matrix, next)
    return temp
'''

if __name__ == "__main__":
    A = Mat([[1, 1], [1, 3], [5, 4]])
    B = Mat([[8, 29, 23], [39, 20, 4]])

    C = Mat([[1, 1], [0, 1]])

    print A - A * 2
    print A * B
    print abs(Mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

    C =  Mat([[1, 1, 3, 1], [0, 1, 4, 1], [2, 4, 3, 0], [5, 2, 7, 0]])

    from number_theory_algebra.exponents import fast_exp

    print fast_exp(C, 15)
