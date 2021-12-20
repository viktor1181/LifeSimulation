from world import World
from agent import Agent
import  numpy as np
import pygame
from display import GameDisplay


#w = World()
#a = Agent()

#def init():
#    return w.get_res()

#for i in range(60):
#    print("index = {}".format(i))
#    a.scan(w.get_res())
#    a.life_strategy()
#    w.update_resourse(a.get_new_env())
    #return w.get_res(),
    #print(w.get_res())
    #print(a.get_agent_matrix())

#fig, ax = plt.subplots()
#ax.axis('off')
##im = plt.imshow(w.get_res(), cmap = cm.binary, animated=True)
##anim = animation.FuncAnimation(fig, updatefig, frames=200, interval=50, blit=True)
#ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), init_func=init, blit=True)
##plt.close()
##anim
#plt.show()

WIDTH = 360
HEIGHT = 480
FPS = 2

def main(disp):
    running = True
    w = World()
    a = Agent()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        print(w.get_res().shape)
        disp.draw_cell(a.get_agent_matrix(), w.get_res())
        pygame.display.flip()
        a.scan(w.get_res())
        a.life_strategy()
        w.update_resourse(a.get_new_env())
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = GameDisplay(640, 480 , 20)
    main(screen)