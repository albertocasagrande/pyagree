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
    for row in A:
    	for e in row:
            yield e

def test_agreement_matrix(A):
    if A.shape[0]!=A.shape[1]:
    	raise ValueError("Non-squared matrix")

    if numpy.any(A<0):
    	raise ValueError("The matrix contains some negative values")

    if numpy.all(A==0):
    	raise ValueError("The matrix is null")


