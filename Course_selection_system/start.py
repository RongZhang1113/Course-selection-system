import os, sys
import core.src

path = os.path.dirname(__file__)
sys.path.append(path)

if __name__ == '__main__':
    core.src.run()
