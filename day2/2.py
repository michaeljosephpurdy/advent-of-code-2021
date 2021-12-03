class Instruction:
  def __init__(self, data):
    split_instruction = data.split(' ')
    self.direction = split_instruction[0]
    self.amount = int(split_instruction[1])

def determine_final_position(instructions):
  horizontal_position, depth = 0, 0
  for instruction in instructions:
    if instruction.direction == 'forward':
      horizontal_position += instruction.amount
    elif instruction.direction == 'up':
      depth -= instruction.amount
    elif instruction.direction == 'down':
      depth += instruction.amount
  return horizontal_position * depth

def determine_final_position_via_aiming(instructions):
  horizontal_position, depth, aim = 0, 0, 0
  for instruction in instructions:
    if instruction.direction == 'forward':
      horizontal_position += instruction.amount
      depth += aim * instruction.amount
    elif instruction.direction == 'up':
      aim -= instruction.amount
    elif instruction.direction == 'down':
      aim += instruction.amount
  return horizontal_position * depth

def get_instructions():
  with open('data/2') as f:
    data = f.read().splitlines()
    return [Instruction(d) for d in data]

if __name__ == '__main__':
  instructions = get_instructions()
  print('PART ONE')
  print(f' final position: {determine_final_position(instructions)}')
  print('PART TWO')
  print(f' final position via aiming: {determine_final_position_via_aiming(instructions)}')