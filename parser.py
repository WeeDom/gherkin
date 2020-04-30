from gherkin.parser import Parser
from os import listdir


DATA_DIR = "cuc/"
OUT_DIR = "res/"
OUTPUT = OUT_DIR + "output.txt"

try:
    p = Parser()
    with open(OUTPUT, mode='w') as op:
        for f in listdir(DATA_DIR):
            res = p.parse(DATA_DIR + f)
            op.write("filename: {}\n\n".format(DATA_DIR + f))
            for ft in res['feature']['children']:
                op.write("{}\t".format(ft['name']))
                for t in ft['tags']:
                    op.write("{}\t".format(t['name']))
                op.write("\n")

except Exception as e:
    print(e)
