#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    g1 = Game('Harry Potter Legacy')

    p1= Player('kass')

    r1= Result(p1,g1,555)

    ipdb.set_trace()
