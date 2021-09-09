import csv
from konlpy.tag import Mecab
from textrank import KeywordSummarizer
import os
from collections import Counter

list_number = 598770  # list_number = 청원 글 시작 번호
file_list = os.listdir('D:\Project\data/')

# list_number = int(file_list[-1].strip('.csv')) #저장된 마지막 글 불러오기 (마지막글부터 새 데이터 받아오기 위함)


except_count = 0  # except_count = 예외 실행 횟수
list_high=[]
while except_count <= 10:  # 예외가 10번 실행될때까지 반복
    try:

        file = open('D:\Project\data/' + str(list_number) + '.csv', "r", encoding="utf-8-sig")
        data = csv.reader(file)
        data = next(data)[4:]

        text = data[1]
        cate = data[0]

        mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")


        def mecab_tokenizer(sent):
            words = mecab.pos(sent, join=True)
            word_list = []
            for w in words:
                #    print(w, w.split('/')[0], len(w.split('/')[0]))
                if len(w.split('/')[0]) > 1:  # 한글자 제거
                    if ('/NNP' in w or '/NNG' in w):
                        word_list.append(w)
            return word_list


        docs = text.replace("\r", "")
        docs = docs.replace("\t", "")
        docs = docs.replace("  ", "")
        sents = list(set(docs.split("\n")))

        # 키워드 뽑기
        summarizer = KeywordSummarizer(tokenize=mecab_tokenizer, min_count=2, min_cooccurrence=2)
        summarizer.summarize(sents, topk=10)

        kws = summarizer.summarize(sents, topk=10)
        #print(kws)
        kw = [kw for kw in kws]
        list_tx=[]

        for k in range(len(kw)):
            list_tx.append(kw[k][0].split('/')[0])


        list_number += 1
        
        list_high += list_tx
        print(list_high)

    except Exception as e:
        except_count += 1
        print(list_number, '예외가 발생했습니다.', e, except_count)
        # with open('exception_list.csv', 'a', newline='') as el:
        #     el = csv.writer(el)
        #     el.writerow([list_number, e, except_count])
        list_number += 1
