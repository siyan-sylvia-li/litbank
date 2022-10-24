import glob
from nltk.tokenize import sent_tokenize
import re

if __name__ == "__main__":
    for f in glob.glob("original/*.txt"):
        new_f = f.replace("original/", "sentences/")
        new_f = open(new_f, "w+")
        fls = open(f).readlines()
        fls = [l.replace("\n", "") for l in fls]
        fls = " ".join(fls)
        sents = sent_tokenize(fls)
        for s in sents:
            sn = re.sub(r'[^a-zA-Z\' ]+', '', s).lower()
            new_f.write(sn + "\n")

