dailyhoursworked = [5, 10, 10]
productiondata = [[10, 20, 9], [11, 16, 11], [10, 24, 13], [14, 20, 17]]
workertotal = [0]*3

for workernum in range(3):
    workertotal[workernum] = 0
# next

for workernum in range(3):
    for daynum in range(4):
        workertotal[workernum] = workertotal[workernum] + productiondata[daynum][workernum]
    # next
# next

for workernum in range(3):
    workeravg = float(workertotal[workernum] / (4 * dailyhoursworked[workernum]))
    if workeravg < 2:
        print("Investigate", workernum)
    # endif
# next
