import os
import ast

PROJECT = 'qiskit-algorithms'
# path where qiskit-algorithms test folder is located. In my case, it was in a folder called projects in my home directory
PROJECT_FOLDER = f'~/projects/{PROJECT}/test'

def count_test_methods_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            tree = ast.parse(f.read(), filename=file_path)
        except SyntaxError:
            # Skip files that can't be parsed due to syntax errors
            return 0

    test_method_count = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):            
            if node.name.startswith('test_'):
                test_method_count += 1
    return test_method_count

def count_tests_in_folder(folder_path, source_file_path):
    total_test_methods = 0
    with open(source_file_path, 'w', encoding='utf-8') as source_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.startswith('test_') and file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    test_method_count = count_test_methods_in_file(file_path)
                    source_file.write(f'{file_path}\n')
                    print(f'{file_path}')
                    total_test_methods += test_method_count
    return total_test_methods

if __name__ == "__main__":
    folder_path = os.path.expanduser(PROJECT_FOLDER)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_file_path = os.path.abspath(os.path.join(script_dir, '..', f'{PROJECT}_source_files.txt'))
    
    total_tests = count_tests_in_folder(folder_path, source_file_path)
    print(f'Total test methods found: {total_tests}')
    print(f'Source files saved at: {source_file_path}')
