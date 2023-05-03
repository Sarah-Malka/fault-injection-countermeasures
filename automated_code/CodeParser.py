import clang.cindex


class CodeParser:
    def __init__(self, content):
        self.content = content
        self.index = clang.cindex.Index.create()
        self.translation_unit = self.index.parse('login.c', unsaved_files=[('login.c', content)])

    def update_content(self, new_content):
        self.content = new_content
        self.translation_unit = self.index.parse('login.c', unsaved_files=[('login.c', self.content)])

    def get_nodes(self, name, type):
        index = clang.cindex.Index.create()
        translation_unit = index.parse('login5.c', unsaved_files=[('login5.c', self.content)])
        nodes = []
        for node in translation_unit.cursor.walk_preorder():
            if node.kind == type and node.spelling == name:
                nodes.append(node)
        return nodes

    def find_function_body(self, func_name):
        nodes = self.get_nodes(func_name, clang.cindex.CursorKind.FUNCTION_DECL)
        if not nodes or len(nodes) > 1:
            return -1

        node = nodes[0]
        # Get the start and end positions of the function
        start_pos = node.extent.start.offset
        end_pos = node.extent.end.offset

        # Extract the substring of the function body using the start and end positions
        function_body = self.content[start_pos:end_pos]

        # Find the curly braces within the function body
        opening_brace_pos = function_body.find('{')
        return start_pos + opening_brace_pos + 1

    def find_function_calls(self, func_name):
        nodes = self.get_nodes(func_name, clang.cindex.CursorKind.CALL_EXPR)
        calls_indexes = []
        for node in nodes:
            # Get the start position of call expression
            calls_indexes.append(node.extent.start.line-1)
        return calls_indexes

    def find_next_function_call(self, func_name, appearance_number):
        calls_indexes = self.find_function_calls(func_name)
        return calls_indexes[appearance_number]
