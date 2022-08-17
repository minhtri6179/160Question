# Algoexpert
def runLengthEncoding(string):
    # Write your code here.
    pre = string[0]
    result = ""
    count = 0
    for ch in string:
        if ch == pre:
            count += 1
        else:
            if count > 9:
                while count > 9:
                    offset = count % 9
                    result += str(9) + pre
                    count -= 9
                result += str(count) + pre
            else:
                result += str(count) + pre
            count = 1
        pre = ch

    offset = count % 9
    while count > 9:
        result += str(9) + pre
        count -= 9
    result += str(offset) + pre
    return result
