class DirectedConnectedComponents:
	pass
	# def __init__(self, G):
	# 	self._marked = [False] * G.V
	# 	self._id = [None] * G.V
	# 	self._count = 0
	# 	for v in range(G.V):
	# 		if not self._marked[v]:
	# 			self._dfs(G, v)
	# 			self._count += 1
	#
	# def _dfs(self, G, v):
	# 	self._marked[v] = True
	# 	self._id[v] = self._count
	# 	for w in G.adj(v):
	# 		if not self._marked[w]:
	# 			self._dfs(G, w)
	#
	# def connected(self, v, w):
	# 	return self._id[v] == self._id[w]
	#
	# def count(self):
	# 	return self._count
	#
	# def id(self, v):
	# 	return self._id[v]
