from itertools import chain
import json

def format_one_func(func_info):
    return dict(
        cyclomatic_complexity = func_info.cyclomatic_complexity,
        nloc = func_info.nloc,
        short_name = func_info.name,
        long_name = func_info.long_name,
        lines = [func_info.start_line, func_info.end_line],
        filename = func_info.filename)

def json_output(result, verbose):
    ret = [format_one_func(func)
               for src in result
                    for func in src.function_list]
    return json.dumps(ret, indent=4)

