from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput

from application import a

with PyCallGraph(output=GraphvizOutput()):
    # Code to profile:
    a(9)
