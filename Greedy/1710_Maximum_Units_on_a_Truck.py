class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        units = 0
        for boxes, per_box in boxTypes:
            take = min(boxes, truckSize)
            units += take * per_box
            truckSize -= take
            if truckSize == 0:
                break
        return units
