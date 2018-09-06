# Function to unwrap superfluous Python data structures recursively.
def vomit(thing):
  if type(thing) == type(set([])):
    return vomit(list(thing))
  elif type(thing) != type([]):
    return thing
  elif len(thing) > 1:
    return thing
  elif len(thing) <= 0:
    return None
  else:
    unwrapped, = thing
    return vomit(unwrapped)

