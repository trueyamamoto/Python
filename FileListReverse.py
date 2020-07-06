# reverse all lines in text file
with open('./read.txt') as f:
 line=f.readlines()

line.reverse()

with open('./write.txt', mode='w') as f:
 f.writelines(line)
