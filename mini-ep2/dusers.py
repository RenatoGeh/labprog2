import sys

class User:
    def __init__(self, _properties):
        self.properties = []
        self.properties.extend(_properties)
        #print(self.properties)
        id = self.properties[2]
        try:
            uids[id].append(self.properties[0])
            #print(id, uids[id])
        except (KeyError):
            uids[id] = [self.properties[0]]
        name = self.properties[4].split(' ')
        name = name[0] + ' ' + name[len(name) - 1]
        try:
            names[name].append(self.properties[0])
        except (KeyError):
            names[name] = [self.properties[0]]

users = []
names = {}
uids = {}

while True:
    try:
        s = input()
        #print(s)
        users.append(User(s.split(':')))        
    except (EOFError):
        break

if sys.argv[1] == "-a":
    for name in names:
        user = names[name]
        if len(user) > 1:
            print(name, ':', sep='', end='')
            print(*user, sep=',')
elif sys.argv[1] == "-u":
    for id in uids:
        user = uids[id]
        if len(user) > 1:
            print(id, ':', sep='', end='')
            print(*user, sep=',')


