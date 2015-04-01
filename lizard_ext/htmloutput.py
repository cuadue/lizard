import os
import datetime
import jinja2

template_filename = os.path.join(os.path.dirname(__file__), 'template.html')

def figure_of_merit(func_info):
    return ((func_info.cyclomatic_complexity ** 1.5) *
            (func_info.nloc))

def html_output(result, verbose):
    # Flatten out the nested list
    funcs = [f for src in result for f in src.function_list]
    mean_complexity = (sum(f.cyclomatic_complexity for f in funcs) /
                       float(len(funcs)))
    mean_fom = sum(figure_of_merit(f) for f in funcs) / float(len(funcs))
    threshold = 10

    bad_funcs = sorted(
        (f for f in funcs if f.cyclomatic_complexity > threshold),
        key = figure_of_merit,
        reverse = True)

    with open(template_filename, 'r') as f:
        template = jinja2.Template(f.read())

    return template.render(
        mean_complexity = mean_complexity,
        mean_fom = mean_fom,
        fom = figure_of_merit,
        timestamp = datetime.datetime.now(),
        funcs = bad_funcs)

