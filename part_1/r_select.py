class RSelect:
    def __init__(self, array):
        self.array = array

    def select(self, i):
        return self._select(self.array, i)
    
    def _select(self, array, i):

        return array[i]
        if i < j:
            return self._select(array, i)
        
        return self._select(array, i - j)