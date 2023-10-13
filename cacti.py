def cacti_number(twod: list):
    rows = len(twod)
    cols = len(twod[0])

    if (not all(isinstance(x, list) for x in twod)):
        raise TypeError
    
    count = 0
    valid_adj = True

    for r in range (rows):
        for c in range(cols):
            if (twod[r][c] == 0):
                # checking up
                if (r > 0 and twod[r - 1][c] == 1):
                    valid_adj = False
                
                # checking left
                if (c > 0 and twod[r][c - 1] == 1):
                    valid_adj = False

                # checking down
                if (r < rows - 1 and twod[r + 1][c] == 1):
                    valid_adj = False
                
                # checking right
                if (c < cols - 1 and twod[r][c + 1] == 1):
                    valid_adj = False

                if (valid_adj):
                    count += 1
    return count
                
