

def tourWin1(arr, target):
    table = {}
    teamWin = ''
    for i in range(len(arr)):
        if target[i] == 0:
            if arr[i][1] in table:
                table[arr[i][1]] += 1
                teamWin = arr[i][1]
            else:
                table[arr[i][1]] = 1
        else:
            if arr[i][0] in table:
                table[arr[i][0]] += 1
                teamWin = arr[i][0]
            else:
                table[arr[i][0]] = 1

    return teamWin


def tourWin2(arr, target):
    pass


if __name__ == '__main__':
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]
    result = [0, 0, 1]
    print(f'Solution 1: {tourWin1(competitions, result)}')
    print(f'Solution 2: {tourWin2(competitions, result)}')
