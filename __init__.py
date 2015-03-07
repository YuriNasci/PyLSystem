from LSystem import LSystem
from interpretations import interpret_turtle_2D
from examples import KOCH, KOCH_ANGLE

s = LSystem('b', 'a->ab, b->a');
print(s.getProductions());
for i in range(6):
    print(s.iterate(i))

interpret_turtle_2D(KOCH.iterate(3), KOCH_ANGLE, 4)

