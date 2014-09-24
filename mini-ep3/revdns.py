class Host:
	def __init__(self, domain):
		self.domain = domain[1:]
		self.entries = {}
	def add_entry(self, name, ip):
		self.entries[int(ip.split('.')[-1])] = name
	
hosts = []
ignored = False
current = -1

while True:
	try:
		s = input()
		if not ignored:
			print(s)		
		s = s.strip()
		
		if not ignored and (s.split(' ')[0] == "NS"):
			ignored = True
			hosts.append(Host(s.split()[1].split('.')))
			current = current + 1
		elif ignored:
			pieces = s.split()
			if len(pieces) > 2:
				h = hosts[current]
				h.add_entry(pieces[0], pieces[2])

	except(EOFError):
		break

for k in hosts:

	sorted_list = sorted(k.entries)
	for i in sorted_list:
		entry = k.entries[i]
		print(i, "PTR", end=' ')
		print(entry, *k.domain, sep='.', end=".\n")

		

