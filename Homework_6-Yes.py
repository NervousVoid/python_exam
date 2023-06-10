def main(*r):
    s = ({2005, 1983, 'HYPHY'},
         {2005, 1983, 'CLICK'},
         {2005, 1983, 'FANCY'},
         {2005, 2008, 'HYPHY'},
         {2005, 2008, 'CLICK'},
         {2005, 2008, 'FANCY'},
         {2005, 1964, 'LSL'},
         {2005, 1964, 'D'},
         {1998, 'HYPHY'},
         {1998, 'CLICK'},
         {1998, 'FANCY'})
    s1 = set(*r)
    return [i for i in range(len(s)) if not(len(s[i] - s1))][0]
