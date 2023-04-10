


def to_array(num, lt):
    remainder = num % 10
    num = int((((num - remainder) * 10) / 10 ))
    print(num, 'number')
    lt.append(remainder)
    print(lt, 'number list')
    if num != 0:
        return to_array(num,lt)
    return

def format_output(number:int) -> int:
    num_list = list()
    if number <= 999:
        return number
    num_array = to_array(number, num_list)
    return num_array
