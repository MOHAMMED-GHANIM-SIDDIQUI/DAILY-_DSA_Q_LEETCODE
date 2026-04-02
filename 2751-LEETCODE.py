class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        indices = sorted(range(n), key=lambda i: positions[i])
        stack = []

        for curr in indices:
            if directions[curr] == 'R':
                stack.append(curr)
            else:
                while stack and healths[curr] > 0:
                    top = stack.pop()

                    if healths[top] > healths[curr]:
                        healths[top] -= 1
                        healths[curr] = 0
                        stack.append(top)

                    elif healths[top] < healths[curr]:
                        healths[curr] -= 1
                        healths[top] = 0

                    else:
                        healths[curr] = 0
                        healths[top] = 0

        return [h for h in healths if h > 0]
