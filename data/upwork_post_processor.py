import requests
import re
import nltk
from bs4 import BeautifulSoup
import gzip
import json  
import docxpy
from dataclasses import dataclass
from typing import List

class DocX(object):

    @staticmethod
    def get_links(file = 'demo.docx'):

        # extract text
        text = docxpy.process(file)

        # if you want the hyperlinks
        doc = docxpy.DOCReader(file)
        doc.process()  # process file
        hyperlinks = doc.data['links']

        return hyperlinks

class Webpage2Text(object):
        
    def get_text(self, url='https://yubabikes.com/cargobikestore/mundo-electric/'):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.text.replace("\n", " ").replace("\t", " ").strip()
        text = re.sub(' +', ' ', text)
        return text


class Tokenizer(object):
    
    @staticmethod
    def tokenize(text):
        return nltk.word_tokenize(text)
    
    @staticmethod
    def get_ngrams(tokens, n=2):
        return [" ".join(o) for o in zip(*[tokens[i:] for i in range(n)])]


class Reddit(object):

    def __init__(self, filename="ebikes.RC_2022-10.gz"):
        '''Stuff from reddit in jsonl format'''
        self.filename = filename

    def get_comments_for_link_id(self, link_id):
        out = []
        with gzip.open(self.filename,'rb') as fin:        
            for line in fin:   
                line = line.decode()
                line = json.loads(line)
                if line["link_id"].endswith(link_id):
                    out.append(line)
        return out

    @staticmethod
    def get_comments_mentioning_product(comments, product):
        out = []
        for o in comments:
            if product in o["body"]:
                out.append(o["body"])
        return " ".join(out)
    
@dataclass
class URL:
    url: str
    tokens: List[str]
    ngrams: List[str]


@dataclass
class ProductMention:
    url: URL
    text: str
    comments: List[dict]
    ngrams: List[str]
        
class Processor(object):
    
    def __init__(self, w2t: Webpage2Text, tok: Tokenizer):
        self.w2t = Webpage2Text()
        self.tok = Tokenizer()
    
    def process_url(self, url):
        text = self.w2t.get_text(url)
        tokens = self.tok.tokenize(text)
        ngrams = self.tok.get_ngrams(tokens)
        return URL(url, tokens, ngrams)

nltk.download('punkt')

docx = DocX()
hyperlinks = docx.get_links()
links = hyperlinks[5:9]

reddit = Reddit()
comments = reddit.get_comments_for_link_id("yaz4wv")

w2t = Webpage2Text()
tokenizer = Tokenizer()
processor = Processor(w2t, tokenizer)

for product, url in links[1:]:
    product = product.decode()
    url = processor.process_url(url)
    comments_about_product: str = reddit.get_comments_mentioning_product(comments, product=product)
    tok = tokenizer.tokenize(comments_about_product)
    reddit_ngrams = tokenizer.get_ngrams(tokens=tok)
    mention = ProductMention(url, product, comments_about_product, reddit_ngrams)
