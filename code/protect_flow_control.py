import sys
import re
import Protection
import CodeParser
import clang.cindex


def parse_arguments():
    if len(sys.argv) < 4:
        print("Incorrect number of arguments")
        print("Usage: protect_flow_control.py <code_file_path> <func1> <func2> ... <target_function>")
        exit(-1)
    file_name = sys.argv[1]
    functions_to_protect = sys.argv[2:-1]
    target_function = sys.argv[-1]
    return file_name, functions_to_protect, target_function


def find_all(str_data, sub_str):
    return [m.start() for m in re.finditer(sub_str, str_data)]


def main():
    file_path, functions_to_protect, target_function = parse_arguments()
    cfc = Protection.Protection(file_path)

    cfc.create_random_steps(len(functions_to_protect))
    cfc.define_step_constant()

    functions = functions_to_protect + [target_function]
    i = sum_all_steps = 0
    for f in functions_to_protect:
        body_start = cfc.parser.find_function_body(f)
        if body_start == -1:
            print(f"Could not find function \"{f}\".")
            exit(2)
        sum_step = cfc.add_step_count(body_start, i)
        sum_all_steps += sum_step

        call_indexes = cfc.parser.find_function_calls(functions[i+1])
        for appearance in range(len(call_indexes)):
            call_index = cfc.parser.find_next_function_call(functions[i+1], appearance)
            cfc.add_verification(call_index, sum_all_steps)
        i += 1

    protected_file_name = 'protected_' + file_path
    c_file_protected = open(protected_file_name, mode='w')
    c_file_protected.write(cfc.content)
    c_file_protected.close()


if __name__ == '__main__':
    main()
