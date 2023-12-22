def find_possibilities(spring, num):
    if spring == '':
        return 1 if not num else 0
    if not num:
        return 0 if '#' in spring else 1

    num_possibilities = 0

    #logic in this section was visualized and inspired by HyperNeutrino: https://www.youtube.com/watch?v=g3Ms5e7Jdqo&t=449s
    if spring[0] in '?.':
        num_possibilities += find_possibilities(spring[1:], num)

    if spring[0] in '?#':
        if num[0] <= len(spring) and '.' not in spring[:num[0]] and (num[0] == len(spring) or spring[num[0]] != '#'):
            num_possibilities += find_possibilities(spring[num[0] + 1:], num[1:])

    return num_possibilities

def parse_file(file_path):
    springs = []
    arrangements = []
    with open(file_path, 'r') as file:
        for line in file:
            content = line.split(' ')
            springs.append(content[0])
            arrangements.append(content[1].replace('\n', '').split(','))
    return springs, arrangements

if __name__ == '__main__':
    springs, arrangements = parse_file('./input.txt')
    nums = []
    for arr in arrangements:
        nums.append([int(num) for num in arr])
    total = 0
    for spring, num in zip(springs, nums):
        num_possibilities = find_possibilities(spring, num)
        total += num_possibilities
    print(total)