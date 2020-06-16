PRIORITIES = []

def get_priorities():
    return ['safety', 'perceived_safety', '', 'efficiency']

def set_priorities_from_file(fileName):
    """
    Read a file line by line with the prioriites
    """
    f = open(fileName, "r")
    for x in f:
        PRIORITIES.append(x)
    return PRIORITIES
