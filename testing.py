"""Test smart subprocess."""
import os
import subprocess as sp
import pickle


if __name__ == "__main__":
    read_pipe, write_pipe = os.pipe()
    os.set_inheritable(write_pipe, True)

    proc = sp.Popen(["python3", "script.py"],  close_fds=False,
                    stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
    os.close(write_pipe)
    pickle.dump(write_pipe, proc.stdin)

    stdout, stderr = proc.communicate()

    with os.fdopen(read_pipe, 'rb') as rp:
        print(pickle.load(rp))
        print(pickle.load(rp))

    print("stdout: ", stdout.decode().strip())
    print("stderr: ", stderr.decode().strip())
