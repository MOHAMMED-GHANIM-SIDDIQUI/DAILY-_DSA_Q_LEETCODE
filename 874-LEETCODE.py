class Solution:
    def robotSim(self, commands, obstacles):
        # Store obstacles as a set of tuples for fast lookup
        obstacle_set = set(map(tuple, obstacles))

        # Directions: North, East, South, West
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        #    /\
        #  < || >
        #    \/
        x = y = 0
        direction = 0  # its the idx of the direction ===> start facing north
        max_dist = 0

        for cmd in commands:
            if cmd == -1:  # turn right
                direction = (direction + 1) % 4
            elif cmd == -2:  # turn left
                direction = (direction - 1) % 4
            else:
                dx, dy = directions[direction]

                for _ in range(cmd):
                    nx, ny = x + dx, y + dy

                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)

        return max_dist
