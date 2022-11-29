
def sequential_map(*args):
  list_of_values = args[-1]
  def funccc(x):
    for arg in args[:-1]:
      x = list(map(arg, x))
    return x
  return funccc(list_of_values)



def consensus_filter(*args):
  list_of_values = args[-1]
  for arg in args[:-1]:
    list_of_values = list(filter(arg, list_of_values))
  return list_of_values



def reduce_function(funct, list_of_val):
  while len(list_of_val)>1:
    list_of_val[1] = funct(list_of_val[0], list_of_val[1])
    del list_of_val[0]
  return list_of_val[0]

def conditional_reduce(boolean_function, function_for_reducing, list_of_values):
  list_of_values = list(filter(boolean_function, list_of_values))
  return(reduce_function(function_for_reducing, list_of_values))



def func_chain(*args):
  def sequential_run(x):
    for arg in args:
      x = (arg)(x)
    return x
  return sequential_run