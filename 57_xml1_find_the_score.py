# XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    attr_len = []
    for child in node.iter():
        attr_len.append(len(child.attrib))
    return sum(attr_len)
         

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

