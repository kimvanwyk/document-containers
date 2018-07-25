''' Execute pandoc in the kimvanwyk/pandoc container, voluming in the 
dir of the input file and passing through additional arguments
'''

CONTAINER_NAME = 'pandoc'

import os.path
import subprocess as sp

def call_pandoc(in_path, out_name, args=[]):
    (workdir, in_name) = os.path.split(in_path)
    workdir = os.path.abspath(workdir)
    try:
        arg_string = ' '.join(args)
        out = sp.check_output(f'docker run --rm --name {CONTAINER_NAME} -v {workdir}:/io kimvanwyk/pandoc:1.0.0 {arg_string} -o {out_name} {in_name}', 
                              shell=True)
        print(out)
    except sp.CalledProcessError as e:
        print(f'Error: {e.output}')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run a containerised pandoc instance')
    parser.add_argument('in_path', help='Path to the file to process')
    parser.add_argument('out_name', help='Name to apply to the output file. It will be placed in the directory of the input file')
    parser.add_argument('additional_args', nargs=argparse.REMAINDER, help='Additional arguments to provide to pandoc')
    args = parser.parse_args()

call_pandoc(args.in_path, args.out_name, args.additional_args)
