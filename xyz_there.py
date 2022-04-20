def xyz_there(str):
  sub_s = "xyz"
  r_sub = ".xyz"
  check = True
  
  if len(str) < 3:
    return False
  
  if len(str) == 3 and str == sub_s:
    return True
  
  if str[-3:] == sub_s and str[-4] == '.':
    return False
  
    
  for n in range(len(str)):
    if str[n:n+3] == sub_s:
      return True
  return False
