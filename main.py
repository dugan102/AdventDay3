with open("engineMap.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

print(lines[0])

digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
symbols = {'@', '*', '%', '$', '=', '#', '+', '-', '&', '/'}
checked = set()

def search(i, j, arr):


    coordinates = [[1, -1], [0, -1], [-1, -1], [1, 0], [-1, 0], [1, 1], [0, 1], [-1, 1]]

    rMax = len(arr)
    cMax = len(arr[0])

    total = 0

    for r, c in coordinates:
        it = i-r
        jt = j-c
        num = ''

        if 0 <= it < rMax and 0 <= jt < cMax:
            if arr[it][jt] in digits:

                #checked.add([i, j])
                while (0 <= jt-1 < cMax and arr[it][jt-1] in digits):
                    jt -=1
                while (0 <= jt+1 < cMax and arr[it][jt] in digits):
                    if (it, jt) in checked:
                        num = ''
                        break
                    num += arr[it][jt]
                    checked.add((it, jt))
                    jt += 1
        if num != '':
            total += int(num)

    #print(total)
    return total




answer = 0
for i in range(len(lines[1])):
    if lines[1][i] in symbols:
        answer = answer + search(1, i, lines)
        print(lines[1][i], search(1, i, lines))


print(answer)