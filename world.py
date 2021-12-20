import param
import numpy as np

class World:
    def __init__(self):
        self.resourse = np.full((param.N, param.N), param.Max_res)
    def get_res(self):
        return self.resourse
    def update_resourse(self, resourse):
        self.resourse = np.where(resourse > param.Max_res-1, resourse, resourse + 1)