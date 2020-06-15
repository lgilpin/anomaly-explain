import portion as interval

def isError(data, stats):
    label = data['category_name']
    size = data['size']

    true_size = stats[label]['average']
    true_std = stats[label]['std']

    return checkSizes(size, true_size, true_std)

def checkSizes(size, average, std):
    flag = 0
    for i in range(0,2):
        reasonable = interval.closed(average[i]-std[i], average[i]+std[i])
        if size[i] not in reasonable:
            flag += 1 # NOt an error
    if flag >= 2: return 1
    else: return 0
