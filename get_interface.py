import re


def read_sol_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        pattern = r'function.*public.*\)' \
                  r'|function.*external.*\)' \
                  r'|function.*\n.*public.*\)' \
                  r'|function.*\n.*external.*\)' \
                  r'|function.*\n.*\n.*public.*\)' \
                  r'|function.*\n.*\n.*external.*\)' \
                  r'|function.*\n.*\n.*\n.*public.*\)' \
                  r'|function.*\n.*\n.*\n.*external.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*public.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*external.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*public.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*external.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\)'\
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\)' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\)' \
                  r'|function.*public.*{' \
                  r'|function.*external.*{' \
                  r'|function.*\n.*public.*{' \
                  r'|function.*\n.*external.*{' \
                  r'|function.*\n.*\n.*public.*{' \
                  r'|function.*\n.*\n.*external.*{' \
                  r'|function.*\n.*\n.*\n.*public.*{' \
                  r'|function.*\n.*\n.*\n.*external.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*public.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*external.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*public.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*external.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*public.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*external.*{'\
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*{' \
                  r'|function.*public.*\n.*{' \
                  r'|function.*external.*\n.*{' \
                  r'|function.*\n.*public.*\n.*{' \
                  r'|function.*\n.*external.*\n.*{' \
                  r'|function.*\n.*\n.*public.*\n.*{' \
                  r'|function.*\n.*\n.*external.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*public.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*external.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*public.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*external.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*public.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*external.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*{'\
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*{' \
                  r'|function.*public.*\n.*\n.*{' \
                  r'|function.*external.*\n.*\n.*{' \
                  r'|function.*\n.*public.*\n.*\n.*{' \
                  r'|function.*\n.*external.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*public.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*external.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*public.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*external.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*public.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*external.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*{'\
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*{' \
                  r'|function.*public.*\n.*\n.*\n.*{' \
                  r'|function.*external.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*public.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*external.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*public.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*external.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*public.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*external.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*{'\
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*{' \
                  r'|function.*public.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*external.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*public.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*external.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*public.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*external.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*public.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*external.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*public.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*external.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*public.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*external.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*public.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{' \
                  r'|function.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*external.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*{'
        functions = re.findall(pattern, contents)
        for function in functions:
            if function[-1] == "{":
                function = re.sub("\n", "", function)
                function = re.sub("{", "", function)
                #function.replace("\n", "")
                print(function, ";")
            else:
                function = re.sub("\n", "", function)
                #function.replace("\n", "")
                print(function, ";")



def main(file_name) -> None:
    #file_path = "/sol_files/"
    file_path = file_name + ".sol"
    read_sol_file(file_path)
    #print(file_path)

if __name__ == '__main__':
    main("Contract_To_Interface")

