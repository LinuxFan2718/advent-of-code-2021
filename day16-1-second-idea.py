import math
DEBUG = True
version_sum = 0

def parse_raw_bits_with_length(raw_bits, total_length):
  global version_sum
  if DEBUG:
    pass#print(f"total length = {total_length} raw bits = {raw_bits} {bin(raw_bits)}")

  local_position = total_length - 3
  version_bitmask = 0b111 << local_position
  version = (version_bitmask & raw_bits) >> local_position
  version_sum += version
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
      parse_raw_bits_with_length(recursive_raw_bits, recursive_total_length)
    elif length_type == 1:
      local_position -= 11
      recursive_num_packets_bitmask = 0b11111111111 << local_position
      recursive_num_packets = (recursive_num_packets_bitmask & raw_bits) >> local_position
      local_position = parse_raw_bits_with_num_packets(raw_bits, recursive_num_packets, local_position)
  if local_position > 0:
    new_raw_bits = raw_bits & (2**local_position) - 1
    parse_raw_bits_with_length(new_raw_bits, local_position)

def parse_raw_bits_with_num_packets(raw_packet, num_packets, position):
  if DEBUG:
    print(f"num packets {num_packets}")
  global version_sum
  packets_parsed = 0
  while packets_parsed < num_packets:
    position -= 3
    version_bitmask = 0b111 << position
    version = (version_bitmask & raw_packet) >> position
    version_sum += version
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
        parse_raw_bits_with_length(raw_bits, total_length)
      elif length_type == 1:
        position -= 11
        recursive_num_packets_bitmask = 0b11111111111 << position
        recursive_num_packets = (recursive_num_packets_bitmask & raw_packet) >> position
        if DEBUG:
          print(f"recursive num packets {recursive_num_packets}")
        position = parse_raw_bits_with_num_packets(raw_packet, recursive_num_packets, position)

    packets_parsed += 1
  if DEBUG:
    print(f"packets parsed = {packets_parsed}")
  return position

# function param is string with hex representation of packet
# use this to determine left pad (maybe right pad later)
# function always returns number of bits parsed (including or not trailing zeroes?)
def parse_hex_packet(hex_packet):
  global version_sum
  num_bits = len(hex_packet) * 4
  raw_packet = int(hex_packet, 16)

  version_bitmask = 0b111 << num_bits - 3
  version = (version_bitmask & raw_packet) >> num_bits - 3
  version_sum += version
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
  else: # operator packet
    length_type_bitmask = 0b1 << num_bits - 7
    length_type = (length_type_bitmask & raw_packet) >> num_bits - 7
    if length_type == 0:
      total_length_bitmask = 0b111111111111111 << num_bits - 22
      total_length = (total_length_bitmask & raw_packet) >> num_bits - 22
      raw_bits_bitmask = (2**total_length - 1) << num_bits - 22 - total_length
      raw_bits = (raw_bits_bitmask & raw_packet) >> num_bits - 22 - total_length
      parse_raw_bits_with_length(raw_bits, total_length)
    elif length_type == 1:
      num_packets_bitmask = 0b11111111111 << num_bits - 18
      num_packets = (num_packets_bitmask & raw_packet) >> num_bits - 18
      position = num_bits - 18
      parse_raw_bits_with_num_packets(raw_packet, num_packets, position)

#hex_packet = 'D2FE28'
#hex_packet = '38006F45291200'
#hex_packet = 'EE00D40C823060'
#hex_packet = '8A004A801A8002F478'
#hex_packet =  '620080001611562C8802118E34'
#hex_packet = 'C0015000016115A2E0802F182340'
#hex_packet = 'A0016C880162017C3686B18A3D4780'
all_hex_packets = [
   'D2FE28',
   '38006F45291200',
   'EE00D40C823060',
   '8A004A801A8002F478',
   '620080001611562C8802118E34',
   'C0015000016115A2E0802F182340',
  'A0016C880162017C3686B18A3D4780'
 ]

for hex_packet in all_hex_packets:
  parse_hex_packet(hex_packet)
print(f"version sum = {version_sum} (111 correct)")

version_sum = 0
f = open('input16.txt')
hex_packet = f.readline()
#parse_hex_packet(hex_packet)

print(f"version sum = {version_sum} (unknown)")