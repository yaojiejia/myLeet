class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set()  # To keep track of visited rooms
        stack = [0]  # Start with room 0
        
        while stack:
            room = stack.pop()
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    if key not in visited:
                        stack.append(key)
        
        return len(visited) == len(rooms)

            
        

            


        

        