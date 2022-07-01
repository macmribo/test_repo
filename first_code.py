import sys

print(sys.version)
print(sys.executable)


def greet(a_name):
  greeting = 'Hello, {}'.format(a_name)
  return greeting

print(greet('World'))
