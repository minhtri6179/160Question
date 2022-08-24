# Solution 1 using hash tables
def generateDocument(characters, document):
    # Write your code here.
    table_cha = {}
    for ch in characters:
        table_cha[ch] = table_cha.get(ch, 0) + 1

    table_doc = {}
    for ch in document:
        table_doc[ch] = table_doc.get(ch, 0) + 1
    for k in document:
        if k not in table_cha:
            return False
        if table_doc[k] > table_cha[k]:
            return False
    return True

# Solution 2
