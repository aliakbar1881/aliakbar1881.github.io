from jinja2 import Template
import json
import argparse

parser = argparse.ArgumentParser(
                    prog='template_maker',
                    description='make template',
                    epilog='be happy!')

parser.add_argument('-i', '--input')

args = parser.parse_args()
# خواندن فایل JSON
with open(args.input, 'r', encoding='utf-8') as file:
    data = json.load(file)

# خواندن قالب HTML
with open('template.html', 'r', encoding='utf-8') as file:
    template = Template(file.read())

# جایگذاری اطلاعات در قالب HTML
result = template.render(data=data)


# ذخیره خروجی در یک فایل HTML
with open(f"{args.input.split('.')[0]}.html", 'w', encoding='utf-8') as file:
    file.write(result)