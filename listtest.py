

colors = ['black', 'write']
sizes = ['S', 'M', 'L']
tshifts = [(color, size) for color in colors for size in sizes]
print(tshifts)

for tshift in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshift)
