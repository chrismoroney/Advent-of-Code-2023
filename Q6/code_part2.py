def multiply_all_wins(num_ways_to_win):
    if len(num_ways_to_win) == 0:
        return 0
    
    ans = num_ways_to_win[0]
    for i in range(1, len(num_ways_to_win)):
        ans *= num_ways_to_win[i]
    return ans


def calculate_ways_to_win(map):
    ways_to_win = []
    for time in map:
        wins_for_time = 0
        winning_distance = int(map[time])
        for i in range(int(time)+1):
            distance = i * (int(time)-i)
            if distance > winning_distance:
                wins_for_time += 1
        ways_to_win.append(wins_for_time)
    return ways_to_win

def map_time_to_distance(times, distances):
    map = {}
    for i in range(len(times)):
        map[times[i]] = distances[i]

    return map

def parse_file(file_path):
    arr = []

    with open(file_path, 'r') as file:
        for line in file:
            content = line.strip().split()[1:]
            arr.append(content)

    times = arr[0]
    distances = arr[1]

    whole_time = ''
    whole_distance = ''

    for time in times:
        whole_time += time

    for distance in distances:
        whole_distance += distance 

    return_time = []
    return_dist = []
    return_time.append(whole_time)
    return_dist.append(whole_distance)

    return return_time, return_dist
            

if __name__ == '__main__':
    times, distances = parse_file('./input.txt')
    map = map_time_to_distance(times, distances)
    num_ways_to_win = calculate_ways_to_win(map)
    print(num_ways_to_win)
    