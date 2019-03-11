def bin_n(x, n):
    n_bin = len(bin(x))
    return bin(x).replace('0b', '0'*(n-n_bin+2))


f = open("list.txt", "w")
#for i in range(2**3):
#    print('x,',file = f,end = '')

# print('%s' % "[", file=f, end='')
# for j in range(11):
#     for i in range(2**(j+1)):
#         out = bin_n(i, j+1)[::-1]
#         out = int(out, 2)  # +1
#         if out == 0:
#             print('0',file = f,end = '')
#         else:
#             print(out, file=f, end='')
#         print('%s' % " ", file=f, end='')

#     print('\n #',file = f)
#     print('*')

# for i in range(11):
#     i = i+1
#     print('for n = 1:%d'%2**(11-i),file=f)
#     print('a{0} = X({1}*n - {2}:{3}*n - {4});'.format(str(i),str(2**i),str(2**i-1),str(2**i),str(2**(i-1))),file = f)
#     print('b{0} = X({1}*n - {2}:{3}*n ).*coef_{4};'.format(str(i),str(2**i),str(2**(i-1)-1),str(2**i),str(i)),file = f)
#     print('X({1}*n - {2}:{3}*n - {4}) = a{0}+b{0};'.format(str(i),str(2**i),str(2**i-1),str(2**i),str(2**(i-1))),file = f)
#     print('X({1}*n - {2}:{3}*n ) = a{0}-b{0};'.format(str(i),str(2**i),str(2**(i-1)-1),str(2**i),str(i)),file = f)
#     print('%% ',file = f)

# for i in range(8):
#     print('X(16*n{0}) = a4({1})-b4({1});'.format(str(-7+i),str(i+1)),file = f)

f.close()
for i in range(8):
    print(1+8*i)

