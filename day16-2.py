import math
DEBUG = False

def parse_decoded_packet(packet_type_id, values):
  if packet_type_id == 0:
    return sum(values)
  elif packet_type_id == 1:
    return math.prod(values)
  elif packet_type_id == 2:
    return min(values)
  elif packet_type_id == 3:
    return max(values)
  elif packet_type_id == 5:
    return int(bool(values[0] > values[1]))
  elif packet_type_id == 6:
    return int(bool(values[0] < values[1]))
  elif packet_type_id == 7:
    return int(bool(values[0] == values[1]))


# does not know what the operation is
# return an array of values
def parse_raw_bits_with_length(raw_bits, total_length):
  global version_sum
  values = []

  local_position = total_length - 3
  version_bitmask = 0b111 << local_position
  version = (version_bitmask & raw_bits) >> local_position
  local_position -= 3
  packet_type_bitmask = 0b111 << local_position
  packet_type = (packet_type_bitmask & raw_bits) >> local_position

  if DEBUG:
    print(f"(length) embedded version = {version} packet type = {packet_type}")

  if packet_type == 4: # literal value packet
    value = 0
    this_digit_last = False

    while not this_digit_last:
      local_position -= 1
      this_digit_last_bitmask = 0b1 << local_position
      this_digit_last_bit = (this_digit_last_bitmask & raw_bits) >> local_position
      this_digit_last = not bool(this_digit_last_bit)

      local_position -= 4
      this_digit_bitmask = 0b1111 << local_position
      this_digit = (this_digit_bitmask & raw_bits) >> local_position
      value <<= 4
      value += this_digit
    if DEBUG:
      print(f"embedded (length) literal packet value = {value}")
    values.append(value)
  else:
    local_position -= 1
    length_type_bitmask = 0b1 << local_position
    length_type = (length_type_bitmask & raw_bits) >> local_position
    if DEBUG:
      print(f"embedded (length) operator packet of type {length_type}")
    if length_type == 0:
      local_position -= 15
      recursive_total_length_bitmask = 0b111111111111111 << local_position
      recursive_total_length = (recursive_total_length_bitmask & raw_bits) >> local_position
      local_position -= recursive_total_length
      raw_bits_bitmask = (2**recursive_total_length - 1) << local_position
      recursive_raw_bits = (raw_bits_bitmask & raw_bits) >> local_position
      sub_values = parse_raw_bits_with_length(recursive_raw_bits, recursive_total_length)
    elif length_type == 1:
      local_position -= 11
      recursive_num_packets_bitmask = 0b11111111111 << local_position
      recursive_num_packets = (recursive_num_packets_bitmask & raw_bits) >> local_position
      local_position, sub_values = parse_raw_bits_with_num_packets(raw_bits, recursive_num_packets, local_position)
    parsed_value = parse_decoded_packet(packet_type, sub_values)
    values.append(parsed_value)
  if local_position > 0:
    new_raw_bits = raw_bits & (2**local_position) - 1
    sub_values_2 = parse_raw_bits_with_length(new_raw_bits, local_position)
    values = values + sub_values_2
  return values

def parse_raw_bits_with_num_packets(raw_packet, num_packets, position):
  global version_sum
  values = []
  packets_parsed = 0
  while packets_parsed < num_packets:
    position -= 3
    version_bitmask = 0b111 << position
    version = (version_bitmask & raw_packet) >> position
    position -= 3
    packet_type_bitmask = 0b111 << position
    packet_type = (packet_type_bitmask & raw_packet) >> position

    if packet_type == 4: # literal value packet
      value = 0
      this_digit_last = False

      while not this_digit_last:
        position -= 1
        this_digit_last_bitmask = 0b1 << position
        this_digit_last_bit = (this_digit_last_bitmask & raw_packet) >> position
        this_digit_last = not bool(this_digit_last_bit)

        position -= 4
        this_digit_bitmask = 0b1111 << position
        this_digit = (this_digit_bitmask & raw_packet) >> position
        value <<= 4
        value += this_digit
      if DEBUG:
        print(f"embedded (num packets) literal packet value = {value}")
      values.append(value)
    else:
      position -= 1
      length_type_bitmask = 0b1 << position
      length_type = (length_type_bitmask & raw_packet) >> position
      if DEBUG:
        print(f"embedded (num packets) operator packet of type {length_type}")
      if length_type == 0:
        position -= 15
        total_length_bitmask = 0b111111111111111 << position
        total_length = (total_length_bitmask & raw_packet) >> position
        position -= total_length
        raw_bits_bitmask = (2**total_length - 1) << position
        raw_bits = (raw_bits_bitmask & raw_packet) >> position
        sub_values = parse_raw_bits_with_length(raw_bits, total_length)
      elif length_type == 1:
        position -= 11
        recursive_num_packets_bitmask = 0b11111111111 << position
        recursive_num_packets = (recursive_num_packets_bitmask & raw_packet) >> position
        if DEBUG:
          print(f"recursive num packets {recursive_num_packets}")
        position, sub_values = parse_raw_bits_with_num_packets(raw_packet, recursive_num_packets, position)
      parsed_value = parse_decoded_packet(packet_type, sub_values)
      values.append(parsed_value)
    packets_parsed += 1
  if DEBUG:
    print(f"packets parsed = {packets_parsed} position = {position}")
  return position, values

def parse_hex_packet(hex_packet):
  global version_sum
  num_bits = len(hex_packet) * 4
  raw_packet = int(hex_packet, 16)

  version_bitmask = 0b111 << num_bits - 3
  version = (version_bitmask & raw_packet) >> num_bits - 3
  packet_type_bitmask = 0b111 << num_bits - 6
  packet_type = (packet_type_bitmask & raw_packet) >> num_bits - 6

  if packet_type == 4: # literal value packet
    value = 0
    this_digit_last = False

    offset = 0
    while not this_digit_last:
      this_digit_last_bitmask = 0b1 << num_bits - 7 - offset
      this_digit_last_bit = (this_digit_last_bitmask & raw_packet) >> num_bits - 7 - offset
      this_digit_last = not bool(this_digit_last_bit)
      this_digit_bitmask = 0b1111 << num_bits - 11 - offset
      this_digit = (this_digit_bitmask & raw_packet) >> num_bits - 11 - offset
      value <<= 4
      value += this_digit
      offset += 5
    
    if DEBUG:
      print(f"literal packet value = {value}")
    return value
  else: # operator packet

    length_type_bitmask = 0b1 << num_bits - 7
    length_type = (length_type_bitmask & raw_packet) >> num_bits - 7
    if length_type == 0:
      total_length_bitmask = 0b111111111111111 << num_bits - 22
      total_length = (total_length_bitmask & raw_packet) >> num_bits - 22
      raw_bits_bitmask = (2**total_length - 1) << num_bits - 22 - total_length
      raw_bits = (raw_bits_bitmask & raw_packet) >> num_bits - 22 - total_length
      values = parse_raw_bits_with_length(raw_bits, total_length)
    elif length_type == 1:
      num_packets_bitmask = 0b11111111111 << num_bits - 18
      num_packets = (num_packets_bitmask & raw_packet) >> num_bits - 18
      position = num_bits - 18
      _position, values = parse_raw_bits_with_num_packets(raw_packet, num_packets, position)
    print(f"parsing packet type {packet_type} with values {values}")
    return parse_decoded_packet(packet_type, values)

all_hex_packets = [
  #  'D2FE28',
  #  '38006F45291200',
  #  'EE00D40C823060',
  #  '8A004A801A8002F478',
  #  '620080001611562C8802118E34',
  #  'C0015000016115A2E0802F182340',
  # 'A0016C880162017C3686B18A3D4780'
  'C200B40A82',
  '04005AC33890',
  '880086C3E88112',
  'CE00C43D881120',
  'D8005AC2A8F0',
  'F600BC2D8F',
  '9C005AC2F8F0',
  '9C0141080250320F1802104A08'
 ]

for hex_packet in all_hex_packets:
  res = parse_hex_packet(hex_packet)
  print(f"result = {res}")
  print()

f = open('input16.txt')
hex_packet = f.readline().strip()
res = parse_hex_packet(hex_packet)
print(f"result = {res}")
print()