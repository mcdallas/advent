"""
You're airdropped near Easter Bunny Headquarters in a city somewhere.
"Near", unfortunately, is as close as you can get - the instructions
on the Easter Bunny Recruiting Document the Elves intercepted start here,
and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates
(where you just landed) and face North. Then, follow the provided sequence:
 either turn left (L) or right (R) 90 degrees, then walk forward the given
 number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so
you take a moment and work out the destination. Given that you can only walk
on the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?
"""

INPUT = 'R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3'

turns = {'N': {'R': 'E', 'L': 'W'},
         'E': {'R': 'S', 'L': 'N'},
         'S': {'R': 'W', 'L': 'E'},
         'W': {'R': 'N', 'L': 'S'}}


def turn(facing, direction):
    return turns[facing][direction]


def move(position, facing, direction, steps):

    new_facing = turn(facing, direction) if direction else facing
    x, y = position
    if new_facing == 'N': new_position = (x, y + steps)
    elif new_facing == 'E': new_position = (x + steps, y)
    elif new_facing == 'S': new_position = (x, y - steps)
    elif new_facing == 'W': new_position = (x - steps, y)
    return new_position, new_facing


def distance(position, origin=(0, 0)):
    x1, y1 = origin
    x2, y2 = position
    return sum([abs(x2 - x1), abs(y2 - y1)])


def walk(instructions, pos=(0, 0), face='N'):
    for step in instructions:
        direction, num_steps = step[0], int(step[1:])
        pos, face = move(pos, face, direction, num_steps)
    return pos, face


def walk_until_you_visit_twice(instructions, pos=(0, 0), face='N'):
    visited = set()
    for instruction in instructions:
        the_turn, num_steps = instruction[0], int(instruction[1:])
        face = turn(face, the_turn)
        for step in range(num_steps):
            pos, _ = move(pos, face, '', 1)
            if pos in visited:
                return pos, face
            visited.add(pos)

assert walk(['R3', 'R3']) == ((3, -3), 'S')
assert distance((3, -3)) == 6

print('FIRST PART: ')
pos, _ = walk(INPUT.split(', '))
print(distance(pos))
print('-------------------------------------')
print('SECOND PART: ')
pos, _ = walk_until_you_visit_twice(INPUT.split(', '))
print(distance(pos))
print('-------------------------------------')



