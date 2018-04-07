from click._compat import raw_input
name = raw_input('What is your name?')
if name.endswith('tank'):
    print('Hello tank')
elif name.endswith('xiao'):
    print('Hello xiao')
else:
    print('Hello Strange')
    
a = [1, 2, 3, 5]
for i in a:
    print(i)

b = next(a)
for i in a:
    print(i)