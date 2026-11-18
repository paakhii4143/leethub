
class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1

        def multiply(A, B):
            C = [[0] * m for _ in range(m)]

            for i in range(m):
                for k in range(m):
                    if A[i][k]:
                        for j in range(m):
                            C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD

            return C

        def mat_vec(A, v):
            return [
                sum(A[i][j] * v[j] for j in range(m)) % MOD
                for i in range(m)
            ]

        def power_vec(A, v, p):
            while p > 0:
                if p % 2:
                    v = mat_vec(A, v)

                A = multiply(A, A)
                p //= 2

            return v

        # Transition matrices
        L = [[0] * m for _ in range(m)]
        U = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                if j < i:
                    L[i][j] = 1
                elif j > i:
                    U[i][j] = 1

        # Initial DP for length 2
        up = list(range(m))
        down = [m - 1 - i for i in range(m)]

        # Combine two transitions
        A = multiply(L, U)
        B = multiply(U, L)

        # Number of pairs of transitions
        p = (n - 2) // 2

        up = power_vec(A, up, p)
        down = power_vec(B, down, p)

        # Apply one extra transition if needed
        if (n - 2) % 2:
            new_up = mat_vec(L, down)
            new_down = mat_vec(U, up)

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD
