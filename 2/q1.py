import importlib


def print_func(file, name, args, doc):
    file.write('        <function>\n')

    file.write('            <function_name>')
    file.write(name)
    file.write('</function_name>\n')

    if doc != "":
        lines_of_doc = doc.split('\n')
        file.write('            <annotations>')
        for line in lines_of_doc:
            file.write(line)
            file.write(' ')
        file.write('            </annotations>\n')

    if args is not None:
        file.write('            <arguments>\n')
        for arg_name in args:
            file.write('                <argument>\n')
            file.write('                    <argument_name>')
            file.write(arg_name)
            file.write('</argument_name>\n')
            file.write('                    <argument_type>')
            type = str(args[arg_name])
            # writing type normally :)
            if type.startswith('<class '):
                type = type[8:-2]
            file.write(type)
            file.write('</argument_type>\n')
            file.write('                </argument>\n')
        file.write('            </arguments>\n')

    file.write('        </function>\n')


def doc_to_html(file_name, output):
    # remove the .py ending
    index = file_name.find('.py')
    md = file_name[0:index]
    # getting module using the importlib library
    module = importlib.import_module(md)
    with open(output, 'w') as file:
        file.write('<html>\n')
        file.write('    <title>')
        file.write(module.__name__)
        file.write('</title>\n')
        doc = module.__doc__
        if doc != "":
            lines_of_doc = doc.split('\n')
            file.write('    <annotations>')
            for line in lines_of_doc:
                file.write(line)
                file.write(' ')
            file.write('   </annotations>\n')
        funcs_names = module.__dir__()[8:]
        if funcs_names is not None:
            file.write('    <functions>\n')
            for func_name in funcs_names:
                func_ref = module.__getattribute__(func_name)
                func_annotations = func_ref.__annotations__
                func_doc = func_ref.__doc__
                print_func(file, func_name, func_annotations, func_doc)
            file.write('\n    </functions>\n')
        file.write('</html>')


if __name__ == '__main__':
    doc_to_html('homeworkmodule.py', 'doc.html')
