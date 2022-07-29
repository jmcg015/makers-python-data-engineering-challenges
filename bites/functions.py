def subtract_low_from_high(a, b):
  if a > b:
    return a - b
  else:
    return b - a

def superify(word):
  return f"super{word}"

print(superify("Sophie"))
print(superify(superify("Sophie")))