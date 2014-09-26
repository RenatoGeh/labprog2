class Host:
	def __init__(self, domain, header):
		self.domain = domain[1:]
		self.entries = {}
		self.header = header
	def add_entry(self, name, ip):
		self.entries[int(ip.split('.')[-1])] = name
	
hosts = []
ignored = False
current = -1

while True:
	try:
		s = input()
		s_ = s
		s = s.strip()
		spl = s.split()
		spl_ = s.split(' ')

		if not ignored and (spl_[0] == "NS"):
			ignored = True
		elif not ignored:
			print(s_)
		if ignored:
			if spl_[0] == "NS":
				hosts.append(Host(s.split()[1].split('.'), s_))
				current = current + 1
			if len(spl) > 2:
				h = hosts[current]
				h.add_entry(spl[0], spl[2])

	except(EOFError):
		break

for k in hosts:
	sorted_list = sorted(k.entries)
	print(k.header)
	for i in sorted_list:
		entry = k.entries[i]
		print(i, "PTR", end=' ')
		print(entry, *k.domain, sep='.', end=".\n")

		

