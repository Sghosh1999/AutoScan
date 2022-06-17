#!/usr/bin/env python
# coding: utf-8
#Author : Sayantan Ghosh
#Date : 21/04/2022


import numpy as np
import pandas as pd
import spacy
import PIL
import cv2
import re
import pytesseract
import warnings


from spacy import displacy
warnings.filterwarnings('ignore')



#Cleaning text
import string


#Load NER model
model_ner = spacy.load('./output/model-best/')

#Load Image
image = cv2.imread('./data/041.jpeg')
# cv2.imshow('business_card',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




def cleanText(txt):
    whitespace = string.whitespace
    punctuation = '!#$%\'()*+-:;<=>?[\\]^_`{|}~'

    tableWhiteSpace = str.maketrans('','',whitespace)
    tablePunctuation = str.maketrans('','',punctuation)
    text = str(txt)
    text = text.lower()
    removeWhiteSapce = text.translate(tableWhiteSpace)
    removePunctuation = removeWhiteSapce.translate(tablePunctuation)
    
    return str(removePunctuation)

#Parser
import re
def parser(text,label):
    if label == 'PHONE':
        text = text.lower()
        text = re.sub(r'\D','',text)
    
    elif label == 'EMAIL':
        text = text.lower()
        #text = re.findall('\S+@\S+',text)[0]
        allow_special_chars = '@_.\-'
        text = re.sub(r'[^A-Za-z0-9{} ]'.format(allow_special_chars),'',text)
        
    elif label == 'WEB':
        text = text.lower()
        allow_special_chars = ':/.'
        text = re.sub(r'[^A-Za-z0-9{} ]'.format(allow_special_chars),'',text)
    
    elif label in('NAME','DES'):
        text = text.lower()
        text = re.sub(r'[^A-Za-z]','',text)
        text = text.title()
        
    elif label == 'ORG':
        text = text.lower()
        text = re.sub(r'[^A-Za-z0-9]','',text)
        text = text.title()
    return text

#Grouping the Labels
class Groupgen():
    def __init__(self):
        self.id = 0
        self.text = ''
    def getGroup(self,text):
        if self.text == text:
            return self.id
        else:
            self.id = self.id + 1
            self.text = text
            return self.id

grp_gen = Groupgen()




#Designing the prediction Pipeline
def getPredictions(image):

    #Extract the TextData using Pytesseract
    text_data = pytesseract.image_to_data(image)
    #print(text_data)

    #Convert the Tesseract Information DataFrame
    dataList = list(map(lambda x: x.split('\t'),text_data.split('\n')))
    df = pd.DataFrame(data = dataList[1:],columns = dataList[0])
    df.dropna(inplace=True) #Drop Missing Values
    df['text'] = df['text'].apply(cleanText)


    #convert data into content
    df_clean = df.query('text != ""')
    content = " ".join([w for w in df_clean['text']])


    #Get prediction from the NER Model
    doc = model_ner(content)

    #Visualising the Entity
    #colors = {'B-PHONE':'linear-gradient(45deg,orange,red)'}
    #options={'colors':colors}
    #displacy.render(doc,style='ent',jupyter=True,options=options)




    #Tagging ( Converting doc into JSON)
    doc_json = doc.to_json()


    data_tokens = pd.DataFrame(doc_json['tokens'])
    doc_text = doc_json['text']



    #Extracting the text/token from the start and end positions
    data_tokens['word'] = data_tokens[['start','end']].apply(
    lambda x: doc_text[x[0]:x[1]],axis=1)




    right_dataLabel = pd.DataFrame(doc_json['ents'])[['start','label']]
    data_token = pd.merge(data_tokens,right_dataLabel,how='left',on='start')
    data_token['label'].fillna('O',inplace=True)


    #Join Table to df_clean DataFrame
    #End and Start position are created by end - len(word)
    df_clean['end'] = df_clean['text'].apply(lambda x: len(x)+1).cumsum() -1
    df_clean['start'] = df_clean[['text','end']].apply(lambda x: x[1] - len(x[0]),axis=1)


    #Inner Join based on Satrt
    dataframe_info = pd.merge(df_clean,data_token[['start','word','label']],how='inner',on='start')



    bb_df = dataframe_info.query("label != 'O' ")
    # img = image.copy()

    # for x,y, w,h,label in bb_df[['left','top','width','height','label']].values:
    #     x = int(x)
    #     y = int(y)
    #     w = int(w)
    #     h = int(h)

    #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #     cv2.putText(img,str(label),(x,y),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)

    # cv2.imshow('Predictions',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()




    #Filtering only the BIO Tagging Label name (Ex-Name, ORG, DES) w34 
    bb_df['label'] = bb_df['label'].apply(lambda x: x[2:])
    #Applying the Grouping Function
    bb_df['group'] = bb_df['label'].apply(grp_gen.getGroup)


    #Right and Bottom of Bounding Box for the whole Grouped Obkect
    bb_df[['left','top','width','height']] = bb_df[['left','top','width','height']].astype('int')
    bb_df['right'] = bb_df['left'] + bb_df['width']
    bb_df['bottom'] = bb_df['top'] + bb_df['height']



    #Logic to draw the Bounding Box
    #Top - Minimum
    #Left - Minimum
    #Right - Maximum
    #Bottom - Maximum
    col_grp = ['left','top','right','bottom','label','word','group']
    grp_tag_img = bb_df[col_grp].groupby(by = 'group')


    img_tagging = grp_tag_img.agg({
        'left':min,
        'right':max,
        'top':min,
        'bottom':max,
        'label':np.unique,
        'word':lambda x: " ".join(x)
    })

    ##Drawing the bounding Box in the Grouped Object
    img_bb = image.copy()
    for l,r,t,b,lbl, word in img_tagging.values:
        cv2.rectangle(img_bb,(l,t),(r,b),(0,255,0),2)
        cv2.putText(img_bb,lbl,(l,t),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)

    # cv2.imshow('Predictions-BB',img_bb)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



    #Entities
    info_array = dataframe_info[['word','label']].values
    entities = dict(NAME=[],ORG=[],DES=[],EMAIL=[],PHONE=[],WEB=[])

    previous = 'O'
    for word,label in info_array:
        #print(word, label)
        bio_tag = label[0]
        label_tag = label[2:]
        #print(bio_tag, label_tag)
        #Step 1: Parse the word/token
        text = parser(word,label_tag)
        if bio_tag in ('B','I'):

            #If the word label doesn't match insert into entities
            if previous != label_tag:
                entities[label_tag].append(text)
            #If it is sname check for the inside properties 
            else:
                if bio_tag == "B":
                    entities[label_tag].append(text)
                else:
                    if label in ("NAME","ORG","DES"):
                        entities[label_tag][-1] = entities[label_tag][-1] + " " + text
                    else:
                        entities[label_tag][-1] = entities[label_tag][-1] + " " + text

        previous = label_tag
    
    return img_bb, entities

# In[ ]:




