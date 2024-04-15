# *** Algorithm ***

# width = 5
# for i in range(1, width + 1):
#    if i <= width:
#        print('*' * i)
#        i = i + 1
#    else:
#        print('*' * i)
#        i = i - 1


width: int = 5
for i in range(1, 2*width):
    if i <= width:
        print('*' * i)
    else:
        print('*' * (2*width - i))
