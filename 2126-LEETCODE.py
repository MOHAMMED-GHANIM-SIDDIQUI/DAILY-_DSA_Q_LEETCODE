class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for threat in asteroids:
            if threat>mass:
                return False
            mass+=threat
        return True
        
