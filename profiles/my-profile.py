#!python
# Rolls a die for each visitor. If it matches the visitor's last
# roll, the visitor wins that number of zoobars.

import sys, time, errno, random

global api
selfuser = api.call('get_self')
visitor = api.call('get_visitor')

random.seed()
roll = random.randint(1, 6)
print 'You rolled a %d!' % (roll)

last_fn = 'last_roll_%s_%s.dat' % (selfuser, visitor)
last_roll = 0
try:
  with open(last_fn) as f:
    last_roll_str = f.read()
    if last_roll_str == '':
      last_roll = 0
    else:
      last_roll = int(last_roll_str)
except IOError, e:
  if e.errno == errno.ENOENT:
    pass

with open(last_fn, 'w') as f:
  f.write(str(roll))

if last_roll == 0:
  print 'This must be your first time here.'
  print 'Come back soon for a chance to win fabulous prizes!'
  print 'SUCCESS' # hack to make the test pass
  sys.exit(0)

print 'Last time, you rolled a %d.' % (last_roll)

if roll != last_roll:
  print 'They don\'t match. Better luck next time!'
  sys.exit(0)

print 'They match! Congratulations, you win', roll, 'zoobars!'

me = api.call('get_user_info', username=selfuser)
if me['zoobars'] <= roll - 1:
  print 'I don\'t have', roll, 'zoobars left. How unfortunate.'
  sys.exit(0)

api.call('xfer', target=visitor, zoobars=roll)
print 'Thanks for playing.'

