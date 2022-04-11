class BricksAndWaterPython:

    def how_much_water(bricks_array: list) -> int:
        water = 0
        for i in range(len(bricks_array)):
            for j in range(i, len(bricks_array)):
                for k in range(i, j):
                    print(i, j, k)
                    if bricks_array[i] > bricks_array[k] and bricks_array[j] > bricks_array[k]:
                        water += min(bricks_array[i], bricks_array[j]) - bricks_array[k]
                        bricks_array[k] = min(bricks_array[i], bricks_array[j])
        return water