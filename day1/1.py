def get_sonar_data():
  with open('data/1') as f:
    data = f.read().splitlines()
    return [int(i) for i in data]

def count_depth_increases(sonar_data):
  increases = 0
  previous_data = sonar_data[0]
  for current_data in sonar_data:
    if current_data > previous_data:
      increases += 1
    previous_data = current_data
  return increases

def count_depth_increases_over_three_days(sonar_data):
  increases = 0
  sum_a = sonar_data[0] + sonar_data[1] + sonar_data[2]
  for i in range(0, len(sonar_data) - 2):
    sum_b = sonar_data[i] + sonar_data[i+1] + sonar_data[i+2]
    if sum_b > sum_a:
      increases += 1
    sum_a = sum_b
  return increases

if __name__ == '__main__':
  sonar_data = get_sonar_data()
  print('PART ONE')
  print(f'  depth increases: {count_depth_increases(sonar_data)}')
  print('PART TWO')
  print(f'  depth increases over three day sliding window: {count_depth_increases_over_three_days(sonar_data)}')