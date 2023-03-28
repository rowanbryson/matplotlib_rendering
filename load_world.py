import numpy as np
from transformers import *
from itertools import chain, cycle

def world1():

    world = []
    # load the cube
    cube = np.loadtxt('assets/centered_cube.csv', delimiter=',')
    cube = np.vstack((cube, np.ones(cube.shape[1])))

    # put the cube in the world
    cube_origin = np.array([0, 0.5, 5])
    world.append(translate(*cube_origin) @ cube)
    cube_origin = np.array([4, 0.5, 5])
    world.append(translate(*cube_origin) @ cube)
    cube_origin = np.array([2, 0.5, 7])
    world.append(translate(*cube_origin) @ cube)
    cube_origin = np.array([2, 1.5, 7])
    world.append(translate(*cube_origin) @ cube)
    cube_origin = np.array([2, 2.5, 7])
    world.append(translate(*cube_origin) @ cube)



    # load the ground
    carpet = np.loadtxt('assets/carpet.csv', delimiter=',')
    carpet = carpet.T
    carpet = np.vstack((carpet, np.ones(carpet.shape[1])))

    # rotate the carpet into xz plane
    carpet = rotate_x(np.pi/2) @ carpet

    # scale the carpet by 5
    carpet = scale(5, 5, 5) @ carpet

    carpet_origin = np.array([0, 0, 0])
    world.append(translate(*carpet_origin) @ carpet)


    # stack the world with the NaN columns
    nan_col = np.array([np.nan] * 3 + [1]).reshape(4, 1)
    nan_col_iter = cycle([nan_col])
    piece_then_nan = chain.from_iterable(zip(world, nan_col_iter))

    world = np.hstack(list(piece_then_nan))

    return world


