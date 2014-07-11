def command_sum(*args):
    return sum(args)

def command_summod(*args):
    return sum(args[:-1])%args[-1]
