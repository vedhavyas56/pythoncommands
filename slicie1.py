colors=['red', 'green','orange','black', 'blue ','white ', 'red']
print(colors)

print("\n\n\n")
sub_colors=colors[0:3]
print(sub_colors)

print(colors)
print("\n\n\n")

print(f"the last{len(colors)}elements")
colors[0:2]=['gray','white','yellow']
print(colors)
print(f"the listnow has{len(colors)} elements")

print("\n\n\n Deleting The Slices")
print(colors)
del colors[1:3]
print(colors)

print("\n\n\n\n unpacking \n\n\n\n")
print(colors)
red,blue,*other=colors
print(red)
print(blue)
print(other)