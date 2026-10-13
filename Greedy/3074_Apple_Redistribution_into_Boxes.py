class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity.sort(reverse=True)
        apples = sum(apple)
        boxes = 0
        for size in capacity:
            apples -= size
            boxes += 1
            if apples <= 0:
                return boxes
        return boxes
