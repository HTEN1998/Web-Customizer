import re
import json
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from indexpage_writer import html_writer

class Nlp():
    labels = []
    tagged = []
    List_of_sets = []
    def __init__(self):
        self.p = html_writer()

    def stage1(self):
        # generates list of sets of 3 keywords containing element, attribute & value
        element_item = attribute_item = value_item =""
        is_element_found,count = 0,False
        # count indicate no.of items in each set of keywords
        # set of 3 keywords is appended into self.List_of_sets[]
        f = open(os.path.abspath('corpus.json'),'r') 
        corpus = json.load(f)
        f.close()
        # generating set of keywords by checking it with corpus data
        for word in self.tagged:
            if word in corpus['elements']:
                if is_element_found == False:
                    element_item = corpus['elements'][word]
                    is_element_found = True
                    count+=1
                else:
                    self.List_of_sets.append([element_item,attribute_item,value_item])
                    element_item = attribute_item = value_item =""
                    is_element_found = False
                    count = 0
            elif word in corpus['attributes']:
                attribute_item = corpus['attributes'][word]
                count+=1
            elif word in corpus['value']:
                value_item = corpus['value'][word]
                count+=1
            elif word in self.labels:
                value_item = self.labels.pop(0)
                count+=1

            if count == 3:
                self.List_of_sets.append([element_item,attribute_item,value_item])
                element_item = attribute_item = value_item =""
                is_element_found = False
                count = 0
            
        if count != 0:
            self.List_of_sets.append([element_item,attribute_item,value_item]) 
        print('Stage 1 output= ',self.List_of_sets)       
        # return self.List_of_sets

    def stage2(self):
        # does analysis and rearrangement of keywords in each sets
        def check_history(current_index):
            for i in range(0,current_index): #changes made from current -index to current index+1
                if (self.List_of_sets[i][0] == self.List_of_sets[current_index][0] and self.List_of_sets[i][1] == self.List_of_sets[current_index][1]) and current_index!=0:
                    print('------------------------------->helll')
                    self.List_of_sets[current_index][1] = 'fontcolor'
                    break

        for keyword_set in range(0,len(self.List_of_sets)):
            if self.List_of_sets[keyword_set][0] == '' and keyword_set-1>=0:
                self.List_of_sets[keyword_set][0] = self.List_of_sets[keyword_set-1][0]
        
        for keyword_set in range(0,len(self.List_of_sets)):
            if self.List_of_sets[keyword_set][0] == '':
                self.List_of_sets.remove(self.List_of_sets[keyword_set])
                break
        #Element processing done

        for keyword_set in range(0,len(self.List_of_sets)):
            if self.List_of_sets[keyword_set][2] in {'danger','warning','success','primary','info','dark','light','secondary'}:
                self.List_of_sets[keyword_set][1] = 'color'
                check_history(keyword_set)
            elif self.List_of_sets[keyword_set][2] in {'h1','h6'}:
                self.List_of_sets[keyword_set][1] = 'fontsize'
            elif self.List_of_sets[keyword_set][2] in {'left','center','right'}:
                self.List_of_sets[keyword_set][1] = 'fontalign'
        #attribute processing done
        
        print('stage 2 output= ',self.List_of_sets)
        # return self.List_of_sets

    def stage3(self):
        # apply change to html pages accoriding to the output of keywords analysis
        for i in range(0,len(self.List_of_sets)):
            if (self.List_of_sets[i][0] != "" and self.List_of_sets[i][1] != "" and self.List_of_sets[i][2] != ""):
                print('stage 3')
                if self.List_of_sets[i][0] == 'website' and self.List_of_sets[i][1] == 'title':
                    self.p.website_name = self.List_of_sets[i][2]
                    print('self.p.website_name= ',self.p.website_name)
                elif self.List_of_sets[i][0] == 'website' and self.List_of_sets[i][1] == 'tagline':
                    self.p.website_tagline = self.List_of_sets[i][2]
                    print('self.p.website_tagline= ',self.p.website_tagline)
                elif self.List_of_sets[i][0] == 'button' and self.List_of_sets[i][1] == 'title':
                    self.p.button_title = self.List_of_sets[i][2]
                    print('self.p.button_title= ',self.p.button_title)
                
                elif self.List_of_sets[i][0] == 'navbar' and self.List_of_sets[i][1] == 'fontcolor':
                    self.p.navbar_font_color = 'navbar-'+self.List_of_sets[i][2]
                    print('self.p.navbar_font_color= ',self.p.navbar_font_color)
                elif self.List_of_sets[i][0] == 'dropdown' and self.List_of_sets[i][1] == 'fontcolor':
                    self.p.dropdown_font_color = 'text-'+self.List_of_sets[i][2]
                    print('self.p.dropdown_font_color= ',self.p.dropdown_font_color)
                elif self.List_of_sets[i][0] == 'footer' and self.List_of_sets[i][1] == 'fontcolor':
                    self.p.footer_font_color = 'text-'+self.List_of_sets[i][2]
                    print('self.p.footer_font_color= ',self.p.footer_font_color)
                elif self.List_of_sets[i][0] == 'website' and self.List_of_sets[i][1] == 'color':
                    self.p.body_bgcolor = 'bg-'+self.List_of_sets[i][2]
                    print('self.p.body_bgcolor= ',self.p.body_bgcolor)
                elif self.List_of_sets[i][0] == 'navbar' and self.List_of_sets[i][1] == 'color':
                    self.p.navbar_bgcolor = 'bg-'+self.List_of_sets[i][2]
                    print('self.p.navbar_bgcolor= ',self.p.navbar_bgcolor)
                elif self.List_of_sets[i][0] == 'dropdown' and self.List_of_sets[i][1] == 'color':
                    self.p.dropdown_bgcolor = 'bg-'+self.List_of_sets[i][2]
                    print('self.p.dropdown_bgcolor= ',self.p.dropdown_bgcolor)
                
                elif self.List_of_sets[i][0] == 'card' and self.List_of_sets[i][1] == 'color':
                    self.p.card_bgcolor = 'bg-'+self.List_of_sets[i][2]
                    print('self.p.card_bgcolor= ',self.p.card_bgcolor)

                elif self.List_of_sets[i][0] == 'footer' and self.List_of_sets[i][1] == 'color':
                    self.p.footer_bgcolor = 'bg-'+self.List_of_sets[i][2]
                    print('self.p.footer_bgcolor= ',self.p.footer_bgcolor)
                elif self.List_of_sets[i][0] == 'button' and self.List_of_sets[i][1] == 'color':
                    self.p.button_color = 'bg-'+self.List_of_sets[i][2]
                    print('self.p.button_color= ',self.p.button_color)

                elif self.List_of_sets[i][0] == 'card' and self.List_of_sets[i][1] == 'fontsize':
                    self.p.card_font_size = self.List_of_sets[i][2]
                    print('self.p.card_font_size= ',self.p.card_font_size)
                elif self.List_of_sets[i][0] == 'footer' and self.List_of_sets[i][1] == 'fontsize':
                    self.p.footer_font_size = self.List_of_sets[i][2]
                    print('self.p.footer_font_size= ',self.p.footer_font_size)
                elif self.List_of_sets[i][0] == 'card' and self.List_of_sets[i][1] == 'fontalign':
                    self.p.card_title_align = 'float-'+self.List_of_sets[i][2]
                    print('self.p.footer_font_size= ',self.p.footer_font_size)
                elif self.List_of_sets[i][0] == 'button' and self.List_of_sets[i][1] == 'align' or self.List_of_sets[i][1] == 'fontalign':
                    self.p.button_align = 'float-'+self.List_of_sets[i][2]
                    print('self.p.button_align= ',self.p.button_align)
                elif self.List_of_sets[i][0] == 'footer' and self.List_of_sets[i][1] == 'fontalign':
                    self.p.footer_font_align = 'text-'+self.List_of_sets[i][2]
                    print('self.p.footer_font_align= ',self.p.footer_font_align)
        
        self.p.file_writer()
        self.List_of_sets.clear()

    def intial_processing(self,user_input):
        self.labels = re.findall("'([^']*)'",user_input)

        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(user_input)
        filtered_sentence = [w for w in word_tokens if not w in stop_words] #stopwords removed
        
        label_found, count = 0,0
        newli=[]
        for words in filtered_sentence:
            if len(words)>1 and words[0] == "'":
                label_found = 1
                newli.append(self.labels[count])
                count+=1
            elif len(words) == 1 and words == "'":
                label_found = 0
            elif  label_found == 0:
                newli.append(words)
        filtered_sentence = newli
        print('filtered= ',filtered_sentence)
        return filtered_sentence
    
    def proccessInput(self,changes):
        input_para = changes.lower()
        sentences = input_para.split('.')
        print('sentence= ',sentences)

        for i in range(len(sentences)):
            sentences[i] = sentences[i].strip()
            self.tagged = self.intial_processing(sentences[i])
            self.stage1()
            self.stage2()
            self.stage3()

    
print('modules loaded')
n = Nlp()
# input_para = input("Enter input sentence: ")
# input_para = n.paragraph.lower()
# sentences = input_para.split('.')

# for i in range(len(sentences)):
#     sentences[i] = sentences[i].strip()
#     n.tagged = n.intial_processing(sentences[i])

#     n.stage1()
#     n.stage2()
#     n.stage3()
