
class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Step 1: Build original tree
        adj = [[] for _ in range(n)]

        for i in range(1, n):
            adj[parent[i]].append(i)

        # Step 2: Find new parents
        new_parent = parent[:]
        last = {}

        def dfs(node):
            ch = s[node]

            # Store previous closest ancestor with same character
            old = last.get(ch, -1)

            if node != 0 and old != -1:
                new_parent[node] = old

            # Update closest ancestor
            last[ch] = node

            for child in adj[node]:
                dfs(child)

            # Restore previous ancestor after returning
            if old == -1:
                del last[ch]
            else:
                last[ch] = old

        dfs(0)

        # Step 3: Build modified tree
        new_adj = [[] for _ in range(n)]

        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        # Step 4: Calculate subtree sizes
        ans = [1] * n

        def calculate(node):
            for child in new_adj[node]:
                calculate(child)
                ans[node] += ans[child]

        calculate(0)

        return ans
