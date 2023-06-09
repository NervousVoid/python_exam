
import re

s1 = '{(decl @"riat_941"<== {8038 ; -6099; 6732 ; -4037 } ) ( decl @"atleor_600"<=={ -6592 ;-7025 ;2002 ; 3453 } ) ( decl @"usor" <== { 449 ; 2145 ; -9193 } )(decl @"ararte_992" <== {-1159 ;359 } ) }'
s2 = '{ ( decl @"veed_336" <=={ 9120 ;3953 ;8865 })(decl @"diradi_335" <=={ 1129 ; 4054; 9234 } ) (decl @"aarle" <== { -9569; 8846; 8316} ) (decl @"veor_682"<== {1258 ; -1605 }) }'

def main(s):
    pattern = r'decl\s+@"(\w+)"\s*<==\s*{((?:\s*-?\d+\s*;\s*)*-?\d+\s*)}'
    matches = re.findall(pattern, s)
    return [(m[0], [int(x) for x in m[1].split(';')]) for m in matches]


main(s1)
main(s2)
