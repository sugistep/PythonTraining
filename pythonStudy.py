# # rows = ["〇×〇", "×〇〇","〇××"]
# # for i in range(3):
# #     print(rows[i])

# a = [0,0,0,0,0]

# b = []
# for i in range(5):
#     b.append(i) 
    
# for i in a:
#     print(i)
# for j in b:
#     print(j*2)
# print(b)

# data = [i for i in range(5)]
# print(data)

# a = [[0]*3]*3
# a[1][1]= 1
# print(a)



# a = [[0]*3 for i in range(3)]
# a[1][1] = 1
# print(a)


def print_board(rows):
    for i in range(3):
        for j in range (3):
            print(rows[i][j], end='')
        print()
    print()

def init_board():
    rows = [['A'] * 3 for i in range(3)]
    return rows

rows = init_board()
print_board(rows)