import numpy as np

import param
import random
from numpy import unravel_index
import uuid
class Agent:
    def __init__(self):
        self.id = [str(uuid.uuid4())]
        self.mental = [param.Mental]
        self.physical = [param.Phisical]
        self.coord_x = [random.randint(0,param.N-1)]
        self.coord_y = [random.randint(0,param.N-1)]
        self.death = []
        self.resourse = []
    def get_x(self):
        return self.coord_x
    def get_y(self):
        return self.coord_y
    def scan(self, resourse):
        self.resourse = resourse
    def get_new_env(self):
        return self.resourse
    def get_agent_matrix(self):
        a_matrix = np.zeros((param.N, param.N))
        print("lenx = {}".format(len(self.coord_x)))
        print("leny = {}".format(len(self.coord_y)))
        for i in range(len(self.coord_y)):
            a_matrix[self.coord_y[i]][self.coord_x[i]] = 1
        return a_matrix
    def birth(self, x, y, id):

        self.id.append(str(uuid.uuid4()))
        self.mental.append(param.Mental)
        self.physical.append(param.Phisical)
        self.coord_x.append(x)
        self.coord_y.append(y)
        self.mental[id] = self.mental[id] - param.Mental_potr
        self.physical[id] = self.physical[id] - param.Food_potr
    def move(self, x, y, id, direction):
        (y_t, x_t) = direction

        self.coord_x[id] = x_t
        self.coord_y[id] = y_t

        self.mental[id] = self.mental[id] - param.Mental_potr
        self.physical[id] = self.physical[id] - param.Food_potr

    def harvest(self, id):
        hungry = param.Max_phisical - self.physical[id]
        harv = hungry - self.resourse[self.coord_y[id]][self.coord_x[id]]
        if self.resourse[self.coord_y[id]][self.coord_x[id]] > hungry:
            self.resourse[self.coord_y[id]][self.coord_x[id]] = self.resourse[self.coord_y[id]][self.coord_x[id]] - hungry
            self.physical[id] = self.physical[id] + hungry
            self.mental[id] = self.mental[id] - param.Mental_potr
        else:
            self.resourse[self.coord_y[id]][self.coord_x[id]] = 0
            self.physical[id] = self.physical[id] + self.resourse[self.coord_y[id]][self.coord_x[id]]
            self.mental[id] = self.mental[id] - param.Mental_potr
    def life_strategy(self):
        print("agents = {}".format(len(self.id)))
        for agent in range(len(self.id)):
            startRow = self.coord_y[agent] - 1 if self.coord_y[agent] > 0 else 0
            endRow = self.coord_y[agent] + 1
            startCol = self.coord_x[agent] - 1 if self.coord_x[agent] > 0 else 0
            endCol = self.coord_x[agent] + 1
            #print(startRow)
            #print(endRow)
            #print(startCol)
            #print(endCol)
            row_num = endRow - startRow + 1
            col_num = endCol - startCol + 1
            coord_arr = []
            buf1 = startCol
            buf2 = startRow
            for i in range(0, row_num):
                new = []
                startCol = buf1
                for j in range(0, col_num):
                    new.append((startRow, startCol))
                    startCol = startCol + 1
                startRow = startRow + 1
                coord_arr.append(new)
            startCol = buf1
            startRow = buf2
            scanned_field = self.resourse[startRow:endRow+1, startCol:endCol+1]
            maxindex = unravel_index(scanned_field.argmax(), scanned_field.shape)
            self.move(x=self.coord_x[agent], y=self.coord_y[agent], direction=coord_arr[maxindex[0]][maxindex[1]], id=agent)
            self.harvest(id=agent)
            if (self.mental[agent] == param.Death or self.physical[agent] == param.Death):
                self.death.append(agent)
            elif (self.mental[agent] % param.Birth == 0):
                self.birth(x=self.coord_x[agent], y=self.coord_y[agent], id=agent)
        self.death1(self.death)
        self.death.clear()
    def death1(self, id):
        for i in id:
            del self.id[i]
            del self.mental[i]
            del self.physical[i]
            del self.coord_x[i]
            del self.coord_y[i]



