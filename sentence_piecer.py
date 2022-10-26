import glob
from nltk.tokenize import sent_tokenize
import re

if __name__ == "__main__":
    for f in glob.glob("og_gutenberg/*.txt"):
        try:
            new_f = f.replace("og_gutenberg/", "sentences/")
            new_f = open(new_f, "w+")
            fls = open(f).readlines()
            fls = [l.replace("\n", "") for l in fls]
            all_lines = []
            record = False
            for s in fls:
                if 'START OF THE PROJECT' in s:
                    record = True
                elif 'END OF THE PROJECT' in s:
                    record = False
                if record and 'START OF THE PROJECT' not in s and 'CHAPTER' not in s:
                    all_lines.append(s)
            fls = " ".join(all_lines)
            sents = sent_tokenize(fls)
            for s in sents:
                sn = re.sub(r'[^a-zA-Z\'\t ]+', '', s).lower()
                sn = sn.strip()
                sn = re.sub(r' +', ' ', sn)
                new_f.write(sn + "\n")
        except UnicodeDecodeError:
            continue

