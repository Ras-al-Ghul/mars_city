import sys
import csv
import matplotlib.pyplot as plt

timestamp = []
thoracic = []
abdominal = []

with open("resp.txt", "r") as f:
	ip = list(csv.reader(f, delimiter='\t'))
	for i in xrange(len(ip)):
		timestamp.append(int(ip[i][0]))
		thoracic.append(int(ip[i][1]))
		abdominal.append(int(ip[i][2]))

inspirations = []
with open("inspiration.txt", "r") as f:
	ip = list(csv.reader(f, delimiter='\t'))
	for i in xrange(len(ip)):
		inspirations.append(int(ip[i][0]))

expirations = []
with open("expiration.txt", "r") as f:
	ip = list(csv.reader(f, delimiter='\t'))
	for i in xrange(len(ip)):
		expirations.append(int(ip[i][0]))

plt.plot(timestamp, thoracic)
plt.plot(timestamp, abdominal)
dicts = dict(zip(timestamp, thoracic))

percentchange = []
for i in xrange(1, len(expirations)):
	cur = dicts[expirations[i]]
	prev = dicts[expirations[i-1]]
	percent = 0.003 * prev
	if not ((prev - percent) < cur < (prev + percent)):
		percentchange.append(expirations[i])

for i in xrange(1, len(inspirations)):
	cur = dicts[inspirations[i]]
	prev = dicts[inspirations[i-1]]
	percent = 0.003 * prev
	if not ((prev - percent) < cur < (prev + percent)):
		percentchange.append(inspirations[i])

print percentchange

plt.plot(inspirations, [dicts[i] for i in inspirations], 'ro')
plt.plot(expirations, [dicts[i] for i in expirations], 'go')
plt.plot(percentchange, [dicts[i] for i in percentchange], 'bo')
plt.show()
		