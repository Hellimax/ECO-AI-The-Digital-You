import tweetnlp

def get_ners(raw_text):

    text=raw_text
    model = tweetnlp.load_model('ner')
    check=model.ner(text,return_probability=False)
    a=[]
    for i in check:
        a.append(i['type'])
    return(list(set(a)))
    

