class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int],
                           waterStartTime: list[int], waterDuration: list[int]) -> int:
        answer = float("inf")
        for i in range(len(landStartTime)):
            land_end = landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                water_end = max(land_end, waterStartTime[j]) + waterDuration[j]
                answer = min(answer, water_end)

                water_first_end = waterStartTime[j] + waterDuration[j]
                land_end_after = max(water_first_end, landStartTime[i]) + landDuration[i]
                answer = min(answer, land_end_after)
        return answer
