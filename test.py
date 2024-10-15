import os
import re

def remove_print_statements(directory):
    print_pattern = re.compile(r'^\s*print\((.*)\)\s*$')  # Matches print statements

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                with open(file_path, 'w') as f:
                    for line in lines:
                        if not print_pattern.match(line):  # Remove print statements
                            f.write(line)

# Change this to your Django project directory
project_directory = '/var/www/ecommerce_backend/backend/'
remove_print_statements(project_directory)

