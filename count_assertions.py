import os
import ast
import pandas as pd
# change this path so that the script reads the list of tests from a text file
SOURCE_FILE = 'Change me'
# Ex: SOURCE_FILE = '/home/user/projects/qta/source_files.txt'


def count_test_methods_and_assertions_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            tree = ast.parse(f.read(), filename=file_path)
        except SyntaxError:
            return 0, []

    test_method_count = 0
    assertion_usage = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
            test_method_count += 1
            assertions_in_method = find_assertions_in_test(node)
            if assertions_in_method:
                assertion_usage.append((node.name, assertions_in_method))

    return test_method_count, assertion_usage

def find_assertions_in_test(test_node):
    """Finds all assertions within a test function node."""
    assertions = []
    for node in ast.walk(test_node):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            method_name = node.func.attr
            method_name_lower = method_name.lower()
            print(f"method_name_lower: {method_name_lower}")
            if 'assert' in method_name_lower:
                print(f"Found quantum test: {method_name}")
                assertions.append(method_name)
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            method_name = node.func.id
            if 'assert' in method_name.lower():
                assertions.append(method_name)
    return assertions

def add_assertions_to_dict(assertions_dict, assertions_list):
    for assertion in assertions_list:
        assertions_dict[assertion] = assertions_dict.get(assertion, 0) + 1
    
def count_tests_and_assertions_in_folder(file_list_path):
    total_test_methods = 0
    all_assertions = []
    all_assertions_dict = dict()
    quantum_methods = []
    with open('source_quantum_methods.txt', 'r') as f:
        quantum_methods = f.readlines()
        quantum_methods = [x.strip().lower() for x in quantum_methods] 
    print(f"quantum_methods: {quantum_methods}")
    with open(file_list_path, 'r') as file_list:
        for file_path in file_list:
            file_path = file_path.strip()
            if file_path.endswith(".py"):
                test_method_count, assertion_usage = count_test_methods_and_assertions_in_file(file_path)
                print(f'{file_path}: {test_method_count} test methods')
                if assertion_usage:
                    for test_name, assertions in assertion_usage:
                        if test_name not in quantum_methods:
                            continue
                        add_assertions_to_dict(all_assertions_dict, assertions)
                        assertions_list = ','.join(assertions)
                        assertion_count = len(assertions)
                        result = f"{file_path};{test_name};{assertion_count};{assertions_list}"
                        print(result)
                        all_assertions.append(result)
                total_test_methods += test_method_count
    print(f"Assertions dictionary: {all_assertions_dict}")
    return total_test_methods, all_assertions, all_assertions_dict

if __name__ == "__main__":
    file_list_path = SOURCE_FILE
    total_tests, all_assertions, all_assertions_dict = count_tests_and_assertions_in_folder(file_list_path)
    print(f'Total test methods found: {total_tests}')
    print("Assertions used in tests:")
    for assertion_entry in all_assertions:
        print(assertion_entry)
    
    print("Assertions dataframe:")
    df = pd.DataFrame.from_dict(all_assertions_dict, orient='index', columns=['num_occur'])
    df.index.name = 'assertion_name'
    df.to_csv('data/assertions.csv')