class TimeMap:

    def __init__(self):
        self.time_dict = dict()
        # dict format = {key: [time_stamp, value @ time_stamp]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # have to set the value in increasing order of timestamp
        if key not in self.time_dict.keys():
            time_value = [[timestamp, value]]

        else:
            time_value = self.time_dict[key]
            low, high = 0, len(time_value)-1

            while low <= high:
                mid = low + (high-low) // 2

                if time_value[mid][0] > timestamp:
                    high = mid -1
                else:
                    low = mid + 1
                
                target_pos = mid

            if timestamp > time_value[mid][0]:
                target_pos = mid + 1
            else:
                target_pos = mid - 1

            time_value.insert(target_pos,[timestamp, value])

        self.time_dict[key] = time_value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict.keys():
            return ""

        time_value = self.time_dict[key]

        low, high = 0, len(time_value) - 1

        while low <= high:
            mid = low + (high-low) // 2
            if time_value[mid][0] == timestamp:
                return time_value[mid][1]
            elif time_value[mid][0] > timestamp:
                high = mid - 1
            else:
                low = mid + 1

        mid = low + (high-low) // 2
        if time_value[mid][0] < timestamp:
            return time_value[mid][1]
        else:
            return ""
                
        
