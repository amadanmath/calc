def command_sum(*args):
    return sum(args)

def command_divide(a1, a2):
    if not a2:
        print "DAME!!!"
        return None
    else:
        return a1 / a2

def command_answer_to_life():
    return 42
