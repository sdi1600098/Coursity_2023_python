#python program to read 'inputdata.txt', calculate Mean Value and Standard Deviation of floats contained in txt file in str form. Then the program creates 'outputdata.txt'
#which contains the said values.

import statistics

count = 0
with open('inputdata.txt', 'r') as f:
    text = f.read()
    total_numbers = f.readlines()
    text_to_float = [float(number) for number in text.split()]
    MV = '%.3f' % statistics.mean(text_to_float)
    SD = '%.3f' % statistics.stdev(text_to_float)
with open('outputdata.txt', 'a+') as f2:
    line1 = ('Μέσος όρος = '+str(MV))
    f2.write(line1 + '\n')
    line2 = ('Τυπική απόκλιση = '+str(SD))
    f2.write(line2 + '\n')
    
