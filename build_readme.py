import glob
import os.path

INCLUDE_PREFIX = 'include_'

order = {}
for inc_file in glob.glob(f'*/{INCLUDE_PREFIX}*'):
    (repo_dir, i) = inc_file.split('/')
    order[int(i[len(INCLUDE_PREFIX):])] = repo_dir

with open('README.md', 'w') as fout:
    with open('base.md', 'r') as fin:
        fout.write(fin.read())
        fout.write('\n\n')
    k = list(order.keys())
    k.sort()
    for key in k:
        with open(os.path.join(order[key], 'README.md'), 'r') as fin:
            fout.write(fin.read())
            fout.write('\n\n')
    
