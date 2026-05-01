def pivoting(matrix):
    for i in range(len(matrix)-1):
        if matrix[i][i]==0:
           for j in range(i,len(matrix)-1):
                matrix[j],matrix[j+1]=matrix[j+1],matrix[j]
                if matrix[i][i]!=0:
                    break
                       
        if all(matrix[j][i]==0 for j in range(i+1,len(matrix))):
            pass
        
        else:
            for j in range(i+1,len(matrix)):
                piv=[matrix[j][i]/matrix[i][i]*x for x in matrix[i]]
                matrix[j] = [ matrix[j][x]-piv[x] for x in range(len(matrix[i])) ]            

    return matrix


