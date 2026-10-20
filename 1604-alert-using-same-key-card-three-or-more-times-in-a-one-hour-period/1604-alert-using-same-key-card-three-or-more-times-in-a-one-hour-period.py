class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:

        n = len(keyName)
        res = []
        timestamps = defaultdict(list)

        for i in range(n):
            name = keyName[i]
            time = keyTime[i]

            hours, minutes = map(int, time.split(":"))
            total_minutes = hours * 60 + minutes

            timestamps[name].append(total_minutes)

        for name, times in timestamps.items():
            times.sort()

            left = 0
            for right in range(len(times)):
                while times[right] - times[left] > 60:
                    left += 1

                if right - left + 1 >= 3:
                    res.append(name)
                    break
        return sorted(res)
                
