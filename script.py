"""Testing script."""
import os
import sys
import pickle


with os.fdopen(pickle.load(sys.stdin.buffer), "wb") as write_pipe:
    pickle.dump([2, 3, 4], write_pipe)
    pickle.dump({'a': 12}, write_pipe)

print("HELLO WORLD")
print("OUCH! Error", file=sys.stderr)
