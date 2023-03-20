#allazoume orismata sti grammi 10.
import statistics

def squares(*argc) :
    mesos_oros = statistics.mean(argc)
    for x in argc :
        diff = abs(x - mesos_oros)
        yield diff**2

for i in squares(2,7,3,12) : 
    print(i)