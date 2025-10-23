class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        changes = []
        for birth, death in logs:
            changes.extend([(birth, 1),(death, -1)])
        changes.sort()
        population = max_population = max_year = 0
        for date, chage in changes:
            population += chage
            if max_population < population:
                max_population = population
                max_year = date
        return max_year