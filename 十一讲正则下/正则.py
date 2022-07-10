import re
# print(re.match('.*[1-9]$','a123456789').span())
# print(re.findall('.','15264\0\t315+-/-/'))
# print(re.findall('010-\d{3,9}?','010-12345'))
s='010-89456132165489'
rule="010-\d*?"
rule_compile=re.compile(rule)
print(rule_compile.findall(s))