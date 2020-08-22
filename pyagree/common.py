import numpy


def countNNRows(A):
	return sum(1 for row in A if not numpy.any(row))
		

def countNNCols(A):
	return sum(1 for col in A.T if not numpy.any(col))


def colSum_iter(A):
    for col in A.T:
        yield col.sum()	


def rowSum_iter(A):
    for row in A:
    	yield row.sum()

        
def item_iter(A):
    for y in range(A.shape[0]):
        for x in range(A.shape[1]):
            yield A[y,x]

