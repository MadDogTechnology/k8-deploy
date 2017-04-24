from subprocess import check_output, STDOUT
from log import log

@log()
def execute(args): 
    return exc(args)


def exc(args): 
    return check_output(args, stderr=STDOUT, universal_newlines=True)
