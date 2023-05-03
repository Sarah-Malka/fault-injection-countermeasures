import random
import uuid
import CodeParser

class Protection:
    def __init__(self, file_path):
        self.guid = str(uuid.uuid4()).replace('-', '')[:6]
        self.steps = []

        f = open(file_path, mode="r")
        self.content = f.read()
        self.parser = CodeParser.CodeParser(self.content)

    def set_content(self, c):
        self.content = c
        self.parser.update_content(c)

    def insert_code_by_index(self, index, code):
        self.set_content(self.content[:index] + code + self.content[index:])

    def insert_code_by_line(self, line, code):
        if line < 0:
            self.set_content(code + "\n" + self.content)
        lines = self.content.split("\n")
        lines = lines[:line] + [code] + lines[line:]
        self.set_content("\n".join(lines))

    def define_step_constant(self):
        definitions = ""
        for i in range(len(self.steps)):
            definitions += "#define METHOD_STEP_" + str(i) + " " + str(self.steps[i]) + "\n"
        code = definitions + f"int count{self.guid} = 0;\n"
        #report_error = f"__attribute__((noreturn, noinline)) void reportError{self.guid}() {{\n\twhile(true);\n}}\n"
        report_error = f"#include <stdbool.h>\nvoid reportError{self.guid}()\n{{\n\twhile(true);\n}}\n"
        self.insert_code_by_index(0, report_error + code)
        #self.insert_code_by_index(0, code)

    def create_random_steps(self, size):
        for i in range(size):
            self.steps.append(random.randint(1, 999))

    def add_step_count(self, body_start, i):
        code = f"\n\tcount{self.guid} += METHOS_STEP_" + str(i) + ";"
        self.insert_code_by_index(body_start, code)
        return self.steps[i]

    def add_verification(self, call_line, sum_all_steps):
        code = f"if (count{self.guid} != {sum_all_steps})" + f"\n{{\n\treportError{self.guid}();\n}}"
        self.insert_code_by_line(call_line, code)
