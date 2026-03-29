#region Boilerplate
"""
Codeforces I/O Python Boilerplate | Optimized Python boilerplate for competitive programming with fast I/O, type-safe input parsing, buffered output handling, and stderr-based debugging, designed for seamless use with the CPH VSCode extension. 
Author: DikshitRJ
Repo: https://github.com/DikshitRJ/cf-py-boilerplate
License: MIT
USAGE GUIDE:
--------------------------------------------------------------------------------
1. input(cast_type=str, sep=None)
   - Fetches the next available token from stdin.
   - cast_type: int, float, or list/tuple (e.g., input([int]) for a list of ints).
   - Automatically handles whitespace and buffers input for speed.
   - Example: n = input(int) | arr = input([int])

2. print(*args, sep=' ', end='\n')
   - Buffered output handler. Use this instead of the built-in print().
   - Automatically formats lists/tuples (e.g., [1,2,3] -> "1 2 3").
   - Buffers data and flushes only at program exit for max performance.
   - Example: print(arr) | print(x, y, sep='-')

3. debprint(*args, sep=' ', end='\n')
   - Debug-only logger; prints exclusively to stderr.
   - Only executes if the --islocal flag is provided. 
   - Safe to leave in code; ignored by judges on Codeforces.
   - Example: debprint("Debug val:", x)
--------------------------------------------------------------------------------
"""
import sys
from argparse import ArgumentParser
from datetime import datetime
import time 
class IOHandler:
    def __init__(self):
        self.input_data = (line for line in sys.stdin)
        self.output_buffer = []
        self.error_buffer = []
        parser = ArgumentParser()
        parser.add_argument('--islocal', action='store_true')
        args = parser.parse_args()
        self.islocal = args.islocal
        if self.islocal:
            self.start_time = time.perf_counter()
            program_name = parser.prog
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Store initial metadata in error_buffer
            self.error_buffer.append(f"\n{'='*30}\n")
            self.error_buffer.append(f"RUNNING: {program_name}\n")
            self.error_buffer.append(f"TIMESTAMP: {now}\n")
            self.error_buffer.append(f"{'-'*30}\n")
    def input(self, cast_type=str, sep=None):
        try:
            line = next(self.input_data).strip()
            if not line:return None
            if isinstance(cast_type, list) and len(cast_type) == 0:return line.split(sep)
            if isinstance(cast_type, list) and len(cast_type) > 0:inner_type = cast_type[0];return [inner_type(x) for x in line.split(sep)]
            if isinstance(cast_type, tuple):
                if len(cast_type) == 0: return tuple(line.split(sep))
                inner_type = cast_type[0]
                return tuple(inner_type(x) for x in line.split(sep))
            return cast_type(line)
        except (EOFError, StopIteration, ValueError, TypeError):return None 
    def debprint(self, *args, sep=" ", end="\n"):
        if self.islocal:
            processed = []
            for arg in args:
                if isinstance(arg, (list, tuple)):
                    processed.append(sep.join(map(str, arg)))
                else:
                    processed.append(str(arg)) 
            self.error_buffer.append(sep.join(processed) + end)
    def print(self, *args, sep=" ", end="\n"):
        processed = []
        for arg in args:
            if isinstance(arg, (list, tuple)):
                processed.append(sep.join(map(str, arg)))
            else:
                processed.append(str(arg))        
        self.output_buffer.append(sep.join(processed) + end)
    def exit(self, *args):
        if self.output_buffer:
            sys.stdout.write("".join(self.output_buffer))
        if self.islocal:
            self.end_time = time.perf_counter()
            self.error_buffer.append(f"EXECUTION TIME: {(self.end_time - self.start_time) * 1000000:.2f}microseconds\n")
            if self.error_buffer:
                sys.stderr.write("".join(self.error_buffer))
                sys.stderr.flush()
        sys.exit(0)
_io = IOHandler()
input = _io.input
print = _io.print
debprint=_io.debprint 
#endregion
    
#--START--your code begins here










#--STOP--your code ends here

#region Boilerplate
_io.exit()
#endregion
