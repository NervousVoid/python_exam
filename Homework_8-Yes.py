import re


def main(input_str):
    input_str = input_str.replace("\n", ' ')
    pattern = r"do declare\s*'(\w+)'\s*->\s*(\w+)\.\s+done\."
    declarations = re.findall(pattern, input_str)
    result = {}
    for declaration in declarations:
        key, value = declaration
        result[value] = key
    return result

#input_str = ".do do declare 'zaenza_790' -> titele_859. done. do declare 'xeza_115' -> bilaa. done. .end"
#input_str = ".do do declare 'laen' -> tiaren_741. done. do declare 'soorin_351' -> dienen. done. do declare 'raus_445' ->aarteri. done. .end"
input_str = ".do do declare'soar_208' -> attiar_822. done. do declare 'bebies_533' -> onat. done. do declare'esvear_367' ->raraqu_317. done. .end"
result = main(input_str)
print(result)