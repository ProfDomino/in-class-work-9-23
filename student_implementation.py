import csv

INFILE = "/Users/m.domino/Downloads/DS5010_FALL_2025/SMS assignment/data/input/100_line_file.csv"
OUTFILE = "/Users/m.domino/Downloads/DS5010_FALL_2025/SMS assignment/data/output/Student_probs_100.csv"



def ingest(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        next(reader) # skip header line
        counts = {
            "ham":{"hey":1,},
            "spam":{"WINNER": 5, "click":2}
        }
        # label = "ham", message = "hey how r u?" 
        ham_total = 0
        spam_total = 0
        for label, message in reader:
            ham_total += 1 if label == "ham" else 0
            spam_total += 1 if label == "spam" else 0
            message_list = message.split()
            for word in message_list:
                if word in counts[label].keys():
                    counts[label][word] += 1
                else:
                    counts[label][word] = 1
    
    return (counts, ham_total, spam_total)

def calc_prob(counts, type_str, word, total):
    """
    counts: nested dict of all words 
    type_str: str of either 'ham' or 'spam'
    word: str of individual word in a message
    total: the total number of spams or hams
    """
    try:
        tt1 = counts[type_str][word]
        return round(tt1 / total, 5)
    except KeyError as e:
        return 0


def probability(filepath, counts_dict, ham_total, spam_total):
    # make a list of all words
    lexicon = list(set(counts_dict["spam"].keys()) | (set(counts_dict["ham"].keys())))
    with open(filepath, 'w', encoding='utf-8') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['word', 'ham_prob', 'spam_prob'])
        for word in lexicon:
            spam_prob = calc_prob(counts_dict, "spam", word, spam_total)
            ham_prob = calc_prob(counts_dict, "ham", word, ham_total)
            writer.writerow((word, ham_prob, spam_prob)) # vs [word, ham_prob, spam_prob]



def main():
    counts, ham_total, spam_total = ingest(INFILE)
    probability(OUTFILE, counts, ham_total, spam_total)
main()
   