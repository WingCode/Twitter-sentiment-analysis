import sys

for line in sys.stdin:
	line = line.strip()
	words = line.split(' ')
	i=0
	for word in words:
			print '%s\t%s' % (i,word)
			i=i+1


#cat /home/wing/113CS0147/senti/proj/input | python /home/wing/113CS0147/senti/proj/mapper_senti.py | python /home/wing/113CS0147/senti/proj/reducer_senti.py

#hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -file /home/wing/113CS0147/senti/proj/mapper_senti.py   -mapper "python /home/wing/113CS0147/senti/proj/mapper_senti.py" -file /home/wing/113CS0147/senti/proj/reducer_senti.py   -reducer "python /home/wing/113CS0147/senti/proj/reducer_senti.py" -input /senti/input -output /senti/output