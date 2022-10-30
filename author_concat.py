import glob
import pandas
from nltk.tokenize import word_tokenize
import json

if __name__ == "__main__":
    authors = pandas.read_csv("Author_List.csv")
    unique_ids = authors.groupby(by="Author")["Gutenberg ID"]
    word_colors = json.load(open("../../process_data/color_synonyms.json"))
    print(unique_ids)
    author_dict = {}
    word_counts = {}
    for s in unique_ids:
        author = s[0]
        ids = list(s[1])
        author_dict.update({author: ids})
    # now iterate through authors
    for a in author_dict:
        wc = 0
        new_cf = open("author_color/{x}.jsonl".format(x=a), "w+")
        for x in author_dict[a]:
            f_s = glob.glob("sentences_og/{n}-0.txt".format(n=x))
            if len(f_s):
                fa = f_s[0]
                lines = open(fa).readlines()
                for l in lines:
                    wc_lines = word_tokenize(l)
                    wc += len(wc_lines)
                    for k in word_colors:
                        if k in wc_lines:
                            new_cf.write(json.dumps({k: {"word": k, "line": l}}) + "\n")
                        else:
                            for w in word_colors[k]:
                                if w in wc_lines:
                                    new_cf.write(json.dumps({k: {"word": w, "line": l}}) + "\n")
                if len(lines) > 1:
                    new_a_file = open("author_sentences/{f}.txt".format(f=a), "a+")
                    new_a_file.writelines(lines)
        word_counts.update({a: wc})
    json.dump(word_counts, open("../../process_data/word_counts_per_author.json", "w+"))