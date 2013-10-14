# import copy
# 
# test = [['grey'] * 3 for _ in range(3)]
# oldTest = copy.deepcopy(test)
# olderTest = oldTest[:]
# 
# olderTest[1][1] = 'CHANGED'
# 
# print test
# print oldTest
# print olderTest
# 
# def computerPlay1():
#     if turns == 0:
#         on_click(None,rows/2,cols/2)
#         return
#     positionScore = [0,0,0,0]
#     for ii, jj in IT.product(range(0,rows), range(0,cols)):
#         if board[ii][jj]['bg'] == 'grey':
#             score = scoreSquare1(ii,jj)
#             if score[0] > positionScore[2]:
#                 positionScore = [ii,jj,score[0],score[1]]
#             elif score[0] == positionScore[2]:
#                 if score[1] > positionScore[3]:
#                     positionScore = [ii,jj,score[0],score[1]]
#     if positionScore[0] == 0 and positionScore[1] == 0:
#         for ii, jj in IT.product(range(0,rows), range(0,cols)):
#             if board[ii][jj]['bg'] == 'grey':
#                 positionScore[0] = ii
#                 positionScore[1] = jj
#                 break
#     on_click(None,positionScore[0],positionScore[1])
# 
# def scoreSquare1(i,j):
#     score = [0,0] #opponent, player
#     for ii, jj in IT.product(range(i - 1, i + 2), range(j - 1, j + 2)):
#         if ii<0 or ii>=rows or jj<0 or jj>=cols: continue
#         square = board[ii][jj]
#         if square['bg'] != 'grey' and (ii, jj) != (i, j):
#             if square['bg'] != player:
#                 score[0] += 1
#             else:
#                 score[1] += 1
#     return score
# 
# def numberBordering():
#     checked = []
#     numBordering = 0
#     for i, j in IT.product(range(rows), range(cols)):
#         if computerBoard[i][j] == 'grey' and (i,j) not in checked:
#             checked.append((i,j))
#             for ii, jj in IT.product(range(i - 1, i + 2), range(j - 1, j + 2)):
#                 if ii<0 or ii>=rows or jj<0 or jj>=cols: continue
#                 if computerBoard[ii][jj] == 'red':
#                     numBordering += 1
#     return numBordering