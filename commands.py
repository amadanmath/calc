def command_sum(*args):
    return sum(args)

def command_taifu_shigoto_siro(*args):
    return "taifu shigoto siro !!"

def command_summod(*args):
    return sum(args[:-1])%args[-1]


def command_divide(a1, a2):
    if not a2:
        print "DAME!!!"
        return None
    else:
        return a1 / a2

def command_answer_to_life():
    return 42

def command_greg(*args):
    return sum(args) * 0
