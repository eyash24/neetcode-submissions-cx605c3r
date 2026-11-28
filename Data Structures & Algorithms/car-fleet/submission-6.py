class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_speed = [(pos, sp) for pos, sp in zip(position, speed)]
        car_speed = sorted(car_speed, reverse=True)
        
        time_stack = []
        fleets = 0

        for pos, sp in car_speed:
            t = (target - pos) / sp
            if not time_stack:
                time_stack.append(t)
                fleets += 1

            elif t > time_stack[-1]:
                    fleets += 1
                    time_stack.append(t)
        return fleets
            



            


        