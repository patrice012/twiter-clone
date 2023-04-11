

def _output(arr:list) -> str:
    if len(arr) >= 4 and len(arr) <= 6:
        rad = [arr.pop(len(arr) - 1) for i in range(0, 3)]
        suf = 'K'
    if len(arr) >= 7:
        suf = 'M'
        rad = [arr.pop(len(arr) - 1) for i in range(0, 6)] 
    return "{0}{1}".format(''.join(arr), suf)

def to_array(num:int) -> list:
    return [a for a in str(num)]

def format_output(number:int) -> str:
    num_list = list()
    if number <= 999:
        return str(number)
    num_array = to_array(number)
    output = _output(num_array)
    return output