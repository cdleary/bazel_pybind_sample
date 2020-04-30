import os
import sys

print('about to import', file=sys.stderr)
print('python is', sys.version_info)
print('pid is', os.getpid())

import my_pb_mod

print('imported, about to call', file=sys.stderr)

result = my_pb_mod.add(2, 3)
print(result)
assert result == 5

print('done!', file=sys.stderr)
