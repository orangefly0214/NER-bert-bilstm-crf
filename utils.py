
LABELS=["O","Investor","Investee","Transferor","Transferee","RC(B)","RC(A)","ACC(CI)","ACC(CD)","ACC(ST)",
        "Change of RC(CI)","Change of RC(CD)","Change of RC(ST)", "Change of CR(CI)","Change of CR(CD)", "Change of CR(ST)",
        "Valuation(B)", "Valuation(A)","Ratio(B)","Ratio(A)", "Change of ratio(CI)", "Change of ratio(CD)",
        "Change of ratio(ST)","X", "[CLS]", "[SEP]"]

def bio_label(LABELS):
    bio_label=[]
    for label in LABELS:
        if label in ["O","X", "[CLS]", "[SEP]"]:
            bio_label.append(label)
        else:
            b_label="B-"+label
            i_label="I-"+label
            bio_label.extend([b_label,i_label])
    return bio_label

