class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet_count = 0

        car_pos_speed_dict = {}
        for pos, speed in zip(position, speed):
            car_pos_speed_dict[pos] = speed
        
        position.sort()
        position = position[::-1]

        prev_car_fleet_time = None
        for car_pos in position:
            d = target - car_pos
            s = car_pos_speed_dict[car_pos]
            if s == 0:
                time = -float('inf')
            else:
                time = float(d / s)
            
            if prev_car_fleet_time is None:
                prev_car_fleet_time = time
                car_fleet_count += 1 
            else:
                if time <= prev_car_fleet_time:
                    continue
                else:
                    prev_car_fleet_time = time
                    car_fleet_count += 1

        return car_fleet_count

            
            


        
