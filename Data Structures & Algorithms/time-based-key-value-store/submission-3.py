class TimeMap:

    def __init__(self):
        self.jon = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.jon:
            self.jon[key] = [[value], [timestamp]]
        else:
            self.jon[key][0].append(value)
            self.jon[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.jon:
            return ""
        if timestamp in self.jon[key][1]:
            return self.jon[key][0][self.jon[key][1].index(timestamp)]
        if self.jon[key][1] == []:
            return ""
        print(self.jon[key][0][-1])
        x = 1
        while x <= len(self.jon[key][1]):
            if self.jon[key][1][-x] <= timestamp:
                return self.jon[key][0][-x]
            x += 1
        return ""
