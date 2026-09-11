class TimeMap:

    def __init__(self):
        self.d = {} # the key will be mapped to a list of lists where each list has a pair of values and timestamp
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append([value, timestamp])


# since were told that the timestamp values are in ascending order we can use binary search to reduce complexity from linear to log n. 
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.d.get(key, [])
        
        L = 0
        R = len(values) - 1

        while L <= R:
            mid = (L + R) // 2
            
            if values[mid][1] == timestamp:
                res = values[mid][0]
                return res
            
            if timestamp > values[mid][1]:
                res = values[mid][0]

                L = mid + 1
            else:
                R = mid - 1

        return res