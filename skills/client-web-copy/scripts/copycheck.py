import re,sys
src=open(sys.argv[1]).read()
strings=re.findall(r'"([^"]{30,})"', src)
strings=[c for c in strings if 'className' not in c and not c.startswith('http')]
# JSX text nodes: text between > and < that isn't markup
jsx=re.findall(r'>\s*([A-Z][^<>{}]{30,}?)\s*<', src)
text=' '.join(strings+jsx)
w=len(text.split())
print(f"copy words (strings + JSX text): {w}")
checks={
 # only dashes doing rhetorical work (reversal / negation / pronoun pivot),
 # not appositives, which are legitimate punctuation
 "rhetorical dashes":(len(re.findall(r'—\s*(?:not|it|that|they|we|you|and then)\b',text,re.I)),0),
 "all em-dashes (fyi)":(len(re.findall(r'—',text)),99),
 # the specific agency tic, not any use of the word — "compounding growth" is fine
 "compound/competing tic":(len(re.findall(r'compound\w* instead of|instead of competing|channels compound',text,re.I)),0),
 "vanity metrics":(len(re.findall(r'vanity metric',text,re.I)),0),
 "hedged intensifiers":(len(re.findall(r'\b(genuinely|remarkably|considerably|dramatically|arguably|notably|significantly|truly)\b',text,re.I)),0),
 "essay connectives":(len(re.findall(r'\b(that said|what.s more|crucially|importantly|it is worth noting)\b',text,re.I)),0),
 # "X, not Y" — fine once or twice in body prose, never in a heading
 # The hard rule is zero in HEADINGS — this counts the whole file, so a few
 # in body bullets is fine and normal. Read the hits before cutting any.
 "comma-contrast (check headings)":(len(re.findall(r'\w, not \w',text)),4),
 "magazine headline shapes":(len(re.findall(r'a different kind of|under one roof|built for (?:revenue|growth|scale|results)',text,re.I)),0),
 "setup-and-turn":(len(re.findall(r'—\s*(?:it|that|they|we|you)\b',text,re.I)),0),
 "marketing superlatives":(len(re.findall(r'\b(best-in-class|world-class|cutting-edge|seamless|unlock|supercharge|leverage|growth engine)\b',text,re.I)),0),
}
bad=0
for k,(v,limit) in checks.items():
    ok = v<=limit
    bad += 0 if ok else 1
    print(f"  {k:26} {v:2}  (max {limit})  {'ok' if ok else 'REVIEW'}")
sys.exit(1 if bad else 0)
