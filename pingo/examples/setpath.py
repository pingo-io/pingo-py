### horrible hack: need to properly package and install pingo library
import sys
import os
path = os.path.abspath(__file__)
path = path[:path.rfind('pingo')]
sys.path.append(path)
### please ignore this line and all above it
