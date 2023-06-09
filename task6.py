def main(*r):
    s = (
        {"PERL", 1967, "GOLO"},
        {"PERL", 1967, "NU", "LOGOS"},
        {"PERL", 1967, "NU", "EQ"},
        {"PERL", 1967, "NU", "J"},
        {"PERL", 1980, "LOGOS", "GOLO"},
        {"PERL", 1980, "LOGOS", "NU"},
        {"PERL", 1980, "EQ"},
        {"PERL", 1980, "J"},
        {"PERL", 1993, "LOGOS"},
        {"PERL", 1993, "EQ"},
        {"PERL", 1993, "J"},
        {"YACC"},
        {"FANCY"},
    )
    s1 = set(*r)
    return [i for i in range(len(s)) if not (len(s[i] - s1))][0]
