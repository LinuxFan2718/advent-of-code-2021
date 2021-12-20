import math
version_number_sum = 0

def parse(packets):
  global version_number_sum
  k = int(math.log(packets, 2))
  leftpad_size = 4 -(k % 4)
  k += leftpad_size
  position = k

  position -= 3
  version_bitmask = 0b111 << position
  version = (packets & version_bitmask) >> position
  version_number_sum += version
  print(f"version number sum = {version_number_sum}  version = {version}")

  position -= 3
  type_id_bitmask = 0b111 << position
  type_id = (packets & type_id_bitmask) >> position

  type_string = 'literal' if type_id == 4 else 'operator'

  print(f"packet version = {version}, type_id = {type_id}, type = {type_string}")
  if type_id == 4: # parse values
    bitmask = 2**position - 1
    number_data = packets & bitmask
    position = parse_value_packet(number_data)
    if position > 0:
      bitmask = 2**position - 1
      remaining_packets = number_data & bitmask
      parse(remaining_packets)
  else: # operator packet
    position = parse_operator_packet(packets)


def parse_value_packet(packet): # dropped version and id from argument
  num_binary_digits = int(math.log(packet, 2)) + 1
  position = num_binary_digits - 5

  last_group = False
  total_value = 0
  while not last_group:
    bitmask = 0b11111 << position
    literal = (packet & bitmask) >> position
    if literal & 0b10000 == 0:
      last_group = True
    else:
      position -= 5
    value = literal & 0b1111
    total_value = total_value << 4
    total_value += value
    print(f"intermediate total value = {total_value}. after adding {bin(value)}")
  print(f"value = {total_value}")
  bits_to_ignore = position % 4
  position -= bits_to_ignore
  return position

def parse_operator_packet(packet):
  k = int(math.log(packet, 2))
  leftpad_size = 4 -(k % 4)
  k += leftpad_size
  position = k - 6

  length_type_id_bitmask = 0b1 << position
  length_type_id = (packet & length_type_id_bitmask) >> position
  position -= 1

  if length_type_id == 0:
    num_bits_containing_total_length = 15
  elif length_type_id == 1:
    num_bits_containing_total_length = 11

  position -= num_bits_containing_total_length
  raw_bitmask = 2**num_bits_containing_total_length - 1
  total_length_bitmask = raw_bitmask << position
  bits_labeled_L = (packet & total_length_bitmask) >> position

  if length_type_id == 0:
    print(f"total length in bits = {bits_labeled_L}")

  elif length_type_id == 1:
    print(f"number of sub-packets = {bits_labeled_L}")
  pass
  return position


filename = 'input15.txt'
f = open(filename)
string_data = f.readline().strip()
string_data = 'D2FE28' # literal value

# operator packet examples
#string_data = '38006F45291200'
#string_data = 'EE00D40C823060' 
# string_data = '8A004A801A8002F478'
# string_data = '620080001611562C8802118E34'
# string_data = 'C0015000016115A2E0802F182340'
# string_data = 'A0016C880162017C3686B18A3D4780'

packets = int(string_data, 16)
parse(packets)
print(f"final version number sum = {version_number_sum}")