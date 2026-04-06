class TimeMap:

    def __init__(self):
        self.dictionary = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.dictionary:
            vals = self.dictionary[key]
            vals = [[timestamp, value]] + vals
            self.dictionary[key] = vals
        else:
            self.dictionary[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dictionary:
            vals = self.dictionary[key]
            for v in vals:
                if timestamp == v[0]:
                    return v[1]
                elif timestamp >= v[0]:
                    return v[1]
            else:
                return ""
        else:
            return ""