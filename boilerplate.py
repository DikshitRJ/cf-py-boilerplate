#region Boilerplate
import sys
from argparse import ArgumentParser
from datetime import datetime
class IOHandler:
    def __init__(self):
        self.input_data = sys.stdin.readline
        self.output_buffer = []
        parser = ArgumentParser()
        parser.add_argument('--islocal', action='store_true')
        args = parser.parse_args()
        self.islocal = args.islocal
        if self.islocal:
            program_name = parser.prog
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sys.stderr.write(f"\n{'='*30}\n")
            sys.stderr.write(f"RUNNING: {program_name}\n")
            sys.stderr.write(f"TIMESTAMP: {now}\n")
            sys.stderr.write(f"{'-'*30}\n")
            sys.stderr.flush()
    def input(self, cast_type=str, sep=None):
        try:
            line = self.input_data().strip()
            if not line:return None
            if isinstance(cast_type, list) and len(cast_type) == 0:return line.split(sep)
            if isinstance(cast_type, list) and len(cast_type) > 0:inner_type = cast_type[0];return [inner_type(x) for x in line.split(sep)]
            if isinstance(cast_type, tuple):
                if len(cast_type) == 0: return tuple(line.split(sep))
                inner_type = cast_type[0]
                return tuple(inner_type(x) for x in line.split(sep))
            return cast_type(line)            
        except (StopIteration, ValueError, TypeError):return None
    def debprint(self, *args, sep=" ", end="\n"):
        if self.islocal:
            processed = []
            for arg in args:
                if isinstance(arg, (list, tuple)):processed.append(sep.join(map(str, arg)))
                else:processed.append(str(arg)) 
            sys.stderr.write(sep.join(processed) + end)
            sys.stderr.flush()
    def print(self, *args, sep=" ", end="\n"):
        processed = []
        for arg in args:
            if isinstance(arg, (list, tuple)):processed.append(sep.join(map(str, arg)))
            else:processed.append(str(arg))        
        self.output_buffer.append(sep.join(processed) + end)
    def exit(self, *args):
        if self.output_buffer:sys.stdout.write("".join(self.output_buffer))
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
