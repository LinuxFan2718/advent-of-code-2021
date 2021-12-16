filename = 'input12.txt'
f = open(filename)
edges = {}
paths = [['start']]
while True:
  line = f.readline().strip()
  if line == '':
    break
  vertex1, vertex2 = line.split('-')
  if 'start' == vertex1 or 'end' == vertex2:
    if vertex1 in edges:
      edges[vertex1].append(vertex2)
    else:
      edges[vertex1] = [vertex2]
  elif 'start' == vertex2 or 'end' == vertex1:
    if vertex2 in edges:
      edges[vertex2].append(vertex1)
    else:
      edges[vertex2] = [vertex1]
  else:
    if vertex1 in edges:
      edges[vertex1].append(vertex2)
    else:
      edges[vertex1] = [vertex2]
    if vertex2 in edges:
      edges[vertex2].append(vertex1)
    else:
      edges[vertex2] = [vertex1]
pass

old_num_paths = None
new_num_paths = len(paths)
while old_num_paths != new_num_paths:
  old_num_paths = len(paths)
  new_paths = []

  for path in paths:
    if 'end' in path:
      new_paths.append(path)
    else:
      for cave in edges[path[-1]]:
        candidate = path[:]
        if cave == 'start':
          continue
        if cave.islower() and cave in candidate:
          # if any small cave has been visited twice move on
          lowers = [cave for cave in candidate if cave.islower()]
          if len(lowers) != len(set(lowers)):
            continue
          # else this is the cave we visit twice
        candidate.append(cave)
        if candidate in new_paths:
          continue
        new_paths.append(candidate)

  paths = new_paths
  new_num_paths = len(paths)

print(f"number of path = {len([path for path in paths if path[-1] == 'end'])}")