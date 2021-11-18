import re
from pprint import pprint

interface_pattern = re.compile(r'"port-reference-ref-name".*?:[^"]+"(?P<Name>.+)')

# Adding addtional pattern to match Admin status and/or Interface ID
#                    r'"admin-status".? (?P<admin>.+)"|', flags=re.MULTILINE)

with open('ne-data-sample.txt', 'r') as file:
    output = file.read()                

    interface_output = interface_pattern.finditer(output)
    interface_list = []
    for interface_conf in interface_output:
        interface_list.append(interface_conf.groupdict())
    
    print('Interface details'.ljust(18) + ': ' )
    pprint(interface_list,indent=10)
