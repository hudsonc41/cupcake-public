def rotate(cycle):
    sort_values = sorted(cycle)
    lowest_value = sort_values[0]
    rotation = cycle.index(lowest_value)
    rotated_cycle = cycle[rotation:] + cycle[:rotation]
    return rotated_cycle


def rat_algorithm(num):
    nums = [num]
    while int(num) < 100000000000:
        digits = list(str(num))
        reversed_digits = digits[::-1]
        reversed_num = int("".join(reversed_digits))
        sum_nums = num + reversed_num
        num = int("".join(sorted(str(sum_nums))))
        if num in nums:
            index = nums.index(num)
            cycle = tuple(nums[index:])
            cycle = rotate(cycle)
            cycle_period = len(cycle)
            return (cycle_period, cycle)
        else:
            nums.append(num)


cycles = {}
for i in range(1, 10000):
    cycle = rat_algorithm(i)
    if cycle:
        cycles[cycle] = cycles.get(cycle, 0) + 1

for cycle_info, occurences in cycles.items():
    cycle_info = cycle_info
    print(
        f"Period: {cycle_info[0]}, occurs {occurences} times, cycle: {' '.join(map(str, cycle_info[1]))}"
    )
