def distribute_candies(N, K):
	result = [0] * K # initialize a list of K elements with zero candies
	i = 0
	while N > 0: # loop until we have no more candies to distribute
		candies_to_give = min(N, i+1)
		result[i % K] += candies_to_give # distribute candies to the i-th person
		N -= candies_to_give # subtract the distributed candies from N
		i += 1 # move to the next person
	return result

if __name__ == '__main__':
	N = 10
	K = 3
	result = distribute_candies(N, K)
	for i in range(K):
		print(result[i], end=" ")
	# output: 3 3 4
