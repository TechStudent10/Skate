from objects import Function
from utils import get_value
import variables as _variables

def parse(lines, variables={}):
    config = _variables.config
    functions = config['functions']
    variables = {**config['variables'], **variables}

    lines = lines.split('\n')
    for line_number in range(len(lines)):
        line = lines[line_number]
        config['line'] = line_number + 1
        if config["current_scope"] == None:
            keyword = line.split(' ')[0]

            # Function
            if keyword == "fn":
                function_name = line.split(' ')[1].split('(')[0]

                try:
                    function_args_strings = "(" + line.split('(')[1].split('\n')[0]
                except:
                    line_list = line.split(' ')
                    del line_list[0]
                    del line_list[0]
                    function_args_strings = ' '.join(line_list)

                function_args_list = function_args_strings.split(',')
                new_function_args_list = []
                for function_arg in function_args_list:
                    if function_arg.startswith('('):
                        function_arg = function_arg.lstrip("(")
                    if function_arg.endswith(')'):
                        function_arg = function_arg.rstrip(")")
                    
                    new_function_args_list.append(function_arg.lstrip(' '))

                functions[function_name] = Function(**{
                    "uid": function_name,
                    "args": new_function_args_list,
                    "lines": [],
                    "name": function_name
                })

                config["current_scope"] = function_name
            # Print to console
            elif keyword == "print":
                line_list = line.split(' ')
                del line_list[0]
                line = ' '.join(line_list)
                print(get_value(line, variables))
            # Execute function
            elif line.endswith(")"):
                line_list = line.split("(")
                function_name = line_list[0]

                if function_name not in functions:
                    print("Function", function_name, "not found")
                    return

                function = functions[function_name]

                del line_list[0]
                args_str = "(".join(line_list)
                args_str = args_str.lstrip("(")
                args_str = args_str.rstrip(")")
                if len(args_str) > 0:
                    args = args_str.split(",")
                    new_args = []

                    for arg in args:
                        if arg.startswith(" "):
                            arg = arg[1:]
                        
                        new_args.append(arg)

                    function_variables = {}
                    for arg in range(len(new_args)):
                        function_variables[function.args[arg]] = new_args[arg]
                else:
                    function_variables = {}

                parse("\n".join(function.lines), function_variables)
            # Create a variable
            elif keyword == "define":
                line_list = line.split(' ')
                del line_list[0]
                variable_name = line_list[0]
                del line_list[0]
                variable_value = ' '.join(line_list)

                variables[variable_name] = get_value(variable_value, variables)
        elif config["current_scope"] != None:
            if line == 'end':
                config["current_scope"] = None
            else:
                line = line.strip('\t')
                line = line.strip('    ')
                functions[config["current_scope"]].lines.append(line)
