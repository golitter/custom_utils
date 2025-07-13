"""
Author: Golemon
Created: 2025.7.13
Version: 1.0

    - Jupyter Notebook to Python Script Converter

        Converts .ipynb files to .py scripts, preserving code cells and converting markdown cells to comments.
        Includes conversion timestamp and tool info in the output file.
        Usage: convertipynb2py('input.ipynb', 'output.py', needidx=False)
        
"""

import json
from datetime import datetime

def convert_ipynb2py(ipynb_file_path, py_file_path = None, need_idx = True):
    if py_file_path == None:
        py_file_path = ipynb_file_path.split('.')[0] + '.py'
    with open(ipynb_file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    with open(py_file_path, 'w', encoding='utf-8') as f:
        # log: time function_name author
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"# Converted from Jupyter Notebook on {current_time}\n")
        f.write("# Conversion tool: convert_ipynb2py\n")
        f.write("# Author: Golemon\n\n")

        for idx, cell in enumerate(notebook['cells'],1):
            
            if cell['cell_type'] != 'code':
                cell['source'] = ["# " + line for line in cell['source']]
                cell['source'].insert(0, '\n################################################\n')
                cell['source'].append('\n################################################\n')
            if need_idx:
                f.write(f'# cell [{idx}]\n')
            f.write(''.join(cell['source']) + '\n\n')


if __name__ == '__main__':
    convert_ipynb2py('1.ipynb')