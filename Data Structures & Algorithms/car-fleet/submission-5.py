class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetcount = 0
        fleet = []
        final_t = []
        for i in range(len(position)):
            final_t.append((target - position[i]) / speed[i])
        print(final_t)
        for i in range(len(position)):
            fleet.append([position[i], final_t[i]])
        
        fleet = sorted(fleet, key = lambda x: x[0])
        fleet.reverse()
        print(fleet)
        # i = 1
        goon = fleet[0]
        i = 1
        for x in fleet:
            if x[1] <= goon[1]:
                # fleet.pop()
                i = i
            else:
                goon = x 
                i += 1    
        return i

# [3,4,2,1] [15, 12, 2, 10]
# [[4, 12], [3, 15], [2,2], [1, 10]]