import numpy as np

def MF(input_matrix, k, learning_rate, lamda, iterations):
	u,i = input_matrix.shape
	W = np.random.rand(u,k)
	H = np.random.rand(i,k)

	data = [(a,b) for a in range(u) for b in range(i)]

	for _ in range(iterations):
	    for a,b in data:
		    p = W[a,:].dot(H[b,:].T)
		    e = input_matrix[a,b] - p

		    W[a,:] , H[b,:] = W[a,:]+learning_rate*(2*e*H[b,:]-lamda*W[a,:]) , H[b,:]+learning_rate*(2*e*W[a,:]-lamda*H[b,:])

	return W, H, W.dot(H.T)

if __name__ == "__main__":
	np.set_printoptions(precision=3, suppress=True)
	Dtrain = np.random.randint(low=0, high=2, size=(10, 10))

	W,H,Dpred = MF(Dtrain,
		k=10, 
		learning_rate=0.01, 
		lamda=0.02, 
		iterations=100
	)
	print("----------------------------------INPUT----------------------------------")
	print(Dtrain)
	print("----------------------------------Prediction----------------------------------")
	print(Dpred)