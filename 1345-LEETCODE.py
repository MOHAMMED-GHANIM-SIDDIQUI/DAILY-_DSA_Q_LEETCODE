class Solution:
    def minJumps(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        # value -> all indices having that value
        graph = defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)

        q = deque([0])
        visited = {0}
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                # all possible next jumps
                neighbors = graph[arr[i]] + [i - 1, i + 1]

                for nxt in neighbors:
                    if 0 <= nxt < n and nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

                # Important optimization:
                # don't process same value again
                graph[arr[i]].clear()

            steps += 1

        return -1
