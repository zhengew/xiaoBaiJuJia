import os
import sys
sys.path.append(os.path.dirname(__file__))

from .smtelca import telca
telca.telc()
telca.users()