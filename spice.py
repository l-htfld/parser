from corpy.udpipe import Model
import json
import re

#загрузили модель
model = Model(r'C:/Users/HP/Documents/python/russian-syntagrus-ud-2.5-191206.udpipe') 

with open("C:/Users/HP/Documents/python/curesache 2/тексты/@TheBadComedian.json", 'r', encoding='utf-8') as f: #открыли файл с данными
    text = json.load(f) #загнали все, что получилось в переменную

#чистим от ссылок, знаков препинания и text
clear_text = []
for elem in text:
    antilink = elem['text']
    data = re.sub(r'[https:\/\/youtu.be\/]+\w+', ' ', antilink)
    data = re.sub(r'[^\w\s]','', data)
    clear_text.append(data)
    
    #print(doc)
    
#делаем разметку
with open('C:/Users/HP/Documents/python/curesache 2/data3.json', 'w', encoding='utf-8') as f: #упаковываем в json
    for i in clear_text:
        sents = model.process(i)

        mylst = []
        for sent in sents:
            sentlist = []
            for word in sent.words:
                sentlist.append({'form': word.form, 
                                 'LEMMA': word.lemma, 
                                 'POS': word.upostag, 
                                 'GRAM_INF': word.feats,
                                 'DEP': word.deprel
                                 })
            mylst.append(sentlist)
                

    json.dump(mylst, f, ensure_ascii=False, indent=4)




