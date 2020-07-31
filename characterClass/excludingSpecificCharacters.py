Regex_Pattern = r'^[^\d]{1}[^aeiou]{1}[^bcDF]{1}[^\r\n\t\f ]{1}[^AEIOU]{1}[^\.,]{1}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())