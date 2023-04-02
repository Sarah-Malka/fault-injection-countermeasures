import subprocess
import sys
import re
import Protection

# userlogin login, managelogin login [enterpage] a b, d e f [c]
# {"login": {"step_method": 156, "count_added":False}, ""}

def parse_arguments():
    args = sys.argv
    if len(args) < 4:
        print("Incorrect number of arguments")
        print("Usage: protect_flow_control.py <code_file_path> -r <func1> <func2> ... <target_function> \
         -r <func1> <func2> ... <target_function> ...")
        exit(-1)
    file_name = args[1]

    routs = [s.split() for s in " ".join(args).split("-r")[1:]]
    return file_name, routs


def find_all(str_data, sub_str):
    return [m.start() for m in re.finditer(sub_str, str_data)]


def main():
    file_path, routs = parse_arguments()
    cfc = Protection.Protection(file_path)

    functions_to_protect = routs[0][:-1]
    target_function = routs[0][-1]
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

        call_indexes = cfc.parser.find_function_calls(functions[i + 1])
        for appearance in range(len(call_indexes)):
            call_index = cfc.parser.find_next_function_call(functions[i + 1], appearance)
            cfc.add_verification(call_index, sum_all_steps)
        i += 1

    protected_file_name = 'protected_' + file_path
    c_file_protected = open(protected_file_name, mode='w')
    c_file_protected.write(cfc.content)
    c_file_protected.close()

    clang_output = subprocess.check_output(["clang-format", "-style=file", protected_file_name])

    # Write the formatted output to a new file
    with open(protected_file_name, "w") as f:
        f.write(clang_output.decode("utf-8"))


if __name__ == '__main__':
    main()
