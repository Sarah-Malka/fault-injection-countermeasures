import subprocess
import sys
import re
import Protection
import Function


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
    target_function = routs[0][-1]
    critical_functions = list(set([func for rout in routs for func in rout[:-1]]))
    functions = critical_functions + [target_function]

    dict_func = {}
    for func in functions:
        dict_func[func] = Function.Function()

    runner = Protection.Protection(file_path, dict_func)

    runner.declare_error_func()
    runner.define_step_constant(critical_functions)

    for func in critical_functions:
        start_body = runner.parser.find_function_body(func)
        if start_body == -1:
            print(f"Could not find function \"{func}\".")
            exit(2)
        dict_func[func].start_body = start_body
        runner.add_step_count(func)

    for rout in routs:
        sum_of_steps = 0
        for i in range(1, len(rout)):
            sum_of_steps += dict_func[rout[i-1]].step
            if_statement = runner.dict_func[rout[i]].if_statement
            if not if_statement:
                if_statement = f"if (count{runner.guid} != {sum_of_steps})" + f"\n{{\n\treportError{runner.guid}();\n}}"
            else:
                index = if_statement.find(")")
                if_statement = if_statement[:index] + f" || count{runner.guid} != {sum_of_steps}" + if_statement[index:]
            runner.dict_func[rout[i]].if_statement = if_statement

    check_functions = list(set([func for rout in routs for func in rout[1:]]))
    for func in check_functions:
        call_indexes = runner.parser.find_function_calls(func)
        for appearance in range(len(call_indexes)):
            call_index = runner.parser.find_next_function_call(func, appearance)
            runner.insert_code_by_line(call_index, dict_func[func].if_statement)

    protected_file_name = 'protected_' + file_path
    c_file_protected = open(protected_file_name, mode='w')
    c_file_protected.write(runner.content)
    c_file_protected.close()

    clang_output = subprocess.check_output(["clang-format", "-style=file", protected_file_name])

    # Write the formatted output to a new file
    with open(protected_file_name, "w") as f:
        f.write(clang_output.decode("utf-8"))


if __name__ == '__main__':
    main()
