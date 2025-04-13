import numpy as np

class VectorQuadraticMapper:
    def __init__(self, n=10) -> None:
        self.n = n
        self._vectors = []
        self.generate_vectors()
    
    def generate_vectors(self):
        for i in range((self.n * -1), (self.n + 1)):
            self._vectors.append(np.array([i, np.square(i)]))

    @property
    def vectors(self):
        return self._vectors
