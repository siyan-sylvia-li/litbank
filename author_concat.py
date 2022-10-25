import glob
import pandas

if __name__ == "__main__":
    authors = pandas.read_csv("Author_List.csv")
    unique_ids = authors.groupby(by="Author")["Gutenberg ID"]
    print(unique_ids)
    author_dict = {}
    for s in unique_ids:
        author = s[0]
        ids = list(s[1])
        author_dict.update({author: ids})
    # now iterate through authors
    for a in author_dict:
        new_a_file = open("author_sentences/{f}.txt".format(f=a), "w+")
        for x in author_dict[a]:
            f_s = glob.glob("sentences/{n}_*.txt".format(n=x))[0]
            lines = open(f_s).readlines()
            new_a_file.writelines(lines)