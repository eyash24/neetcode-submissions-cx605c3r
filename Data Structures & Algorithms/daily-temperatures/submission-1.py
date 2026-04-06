class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        hot_day = [0]*len(temperatures)

        for day, curr_temp in enumerate(temperatures):
            day_count = 0
            for next_temp in temperatures[day+1:]:
                day_count += 1
                if next_temp > curr_temp:
                    hot_day[day] = day_count
                    break
        
        return hot_day



                    

