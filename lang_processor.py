import re
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from indexpage_writer import html_writer

class nlp():
    labels = []
    tagged = []
    paragraph = ""
    def __init__(self):
        self.p = html_writer()

    def stage1(self):

        output = []
        element_item = attribute_item = value_item =''
        element_found_flag,count = 0,0

        f = open('E:\DELL\Documents\WebCustomizer\corpus.json','r')
        data = json.load(f)
        f.close()
        for keywords in self.tagged:
            if keywords in data['elements']:
                if element_found_flag == 0:
                    element_item = data['elements'][keywords]
                    element_found_flag = 1
                    count+=1
                else:
                    output.append([element_item,attribute_item,value_item])
                    element_item = attribute_item = value_item =''
                    element_found_flag = 0
                    count = 0
            elif keywords in data['attributes']:
                attribute_item = data['attributes'][keywords]
                count+=1
            elif keywords in data['value']:
                value_item = data['value'][keywords]
                count+=1
            elif keywords in self.labels:
                value_item = self.labels.pop(0)
                count+=1

            if count == 3:
                output.append([element_item,attribute_item,value_item])
                element_item = attribute_item = value_item =''
                element_found_flag = 0
                count = 0
            
        if count != 0:
            output.append([element_item,attribute_item,value_item]) 
        print('Stage 1 output= ',output)       
        return output

    def stage2(self,List_of_tuples):

        def check_history(current_index):
            for i in range(0,current_index+1):
                if List_of_tuples[i][0] == List_of_tuples[current_index][0] and List_of_tuples[i][1] == List_of_tuples[current_index][1] and current_index!=0:
                    List_of_tuples[current_index][1] = 'fontcolor'
                    break
        #Element processing done

        for i in range(0,len(List_of_tuples)):
            if List_of_tuples[i][0] == '' and i-1>=0:
                List_of_tuples[i][0] = List_of_tuples[i-1][0]
        
        for i in range(0,len(List_of_tuples)):
            if List_of_tuples[i][0] == '':
                List_of_tuples.remove(List_of_tuples[i])
                break
        #attribute processing done

        for i in range(0,len(List_of_tuples)):
            if List_of_tuples[i][2] in {'danger','warning','success','primary','info','dark','light','secondary'}:
                List_of_tuples[i][1] = 'color'
                check_history(i)

            elif List_of_tuples[i][2] in {'h1','h6'}:
                List_of_tuples[i][1] = 'fontsize'
            elif List_of_tuples[i][2] in {'left','center','right'}:
                List_of_tuples[i][1] = 'fontalign'
        
        print('stage 2 output= ',List_of_tuples)
        return List_of_tuples

    def stage3(self,tupled_data):

        for i in range(0,len(tupled_data)):
            if (tupled_data[i][0] != "" and tupled_data[i][1] != "" and tupled_data[i][2] != ""):
                
                if tupled_data[i][0] == 'website' and tupled_data[i][1] == 'title':
                    self.p.website_name = tupled_data[i][2]
                    print('self.p.website_name= ',self.p.website_name)
                elif tupled_data[i][0] == 'website' and tupled_data[i][1] == 'tagline':
                    self.p.website_tagline = tupled_data[i][2]
                    print('self.p.website_tagline= ',self.p.website_tagline)
                elif tupled_data[i][0] == 'card' and tupled_data[i][1] == 'title':
                    self.p.card_title = tupled_data[i][2]
                    print('self.p.card_title= ',self.p.card_title)
                elif tupled_data[i][0] == 'button' and tupled_data[i][1] == 'title':
                    self.p.button_title = tupled_data[i][2]
                    print('self.p.button_title= ',self.p.button_title)
                
                elif tupled_data[i][0] == 'navbar' and tupled_data[i][1] == 'fontcolor':
                    self.p.navbar_font_color = 'navbar-'+tupled_data[i][2]
                    print('self.p.navbar_font_color= ',self.p.navbar_font_color)
                elif tupled_data[i][0] == 'dropdown' and tupled_data[i][1] == 'fontcolor':
                    self.p.dropdown_font_color = 'text-'+tupled_data[i][2]
                    print('self.p.dropdown_font_color= ',self.p.dropdown_font_color)
                elif tupled_data[i][0] == 'footer' and tupled_data[i][1] == 'fontcolor':
                    self.p.footer_font_color = 'text-'+tupled_data[i][2]
                    print('self.p.footer_font_color= ',self.p.footer_font_color)
                elif tupled_data[i][0] == 'website' and tupled_data[i][1] == 'color':
                    self.p.body_bgcolor = 'bg-'+tupled_data[i][2]
                    print('self.p.body_bgcolor= ',self.p.body_bgcolor)
                elif tupled_data[i][0] == 'navbar' and tupled_data[i][1] == 'color':
                    self.p.navbar_bgcolor = 'bg-'+tupled_data[i][2]
                    print('self.p.navbar_bgcolor= ',self.p.navbar_bgcolor)
                elif tupled_data[i][0] == 'dropdown' and tupled_data[i][1] == 'color':
                    self.p.dropdown_bgcolor = 'bg-'+tupled_data[i][2]
                    print('self.p.dropdown_bgcolor= ',self.p.dropdown_bgcolor)
                elif tupled_data[i][0] == 'footer' and tupled_data[i][1] == 'color':
                    self.p.footer_bgcolor = 'bg-'+tupled_data[i][2]
                    print('self.p.footer_bgcolor= ',self.p.footer_bgcolor)
                elif tupled_data[i][0] == 'button' and tupled_data[i][1] == 'color':
                    self.p.button_color = 'bg-'+tupled_data[i][2]
                    print('self.p.button_color= ',self.p.button_color)

                elif tupled_data[i][0] == 'card' and tupled_data[i][1] == 'fontsize':
                    self.p.card_font_size = tupled_data[i][2]
                    print('self.p.card_font_size= ',self.p.card_font_size)
                elif tupled_data[i][0] == 'footer' and tupled_data[i][1] == 'fontsize':
                    self.p.footer_font_size = tupled_data[i][2]
                    print('self.p.footer_font_size= ',self.p.footer_font_size)
                elif tupled_data[i][0] == 'card' and tupled_data[i][1] == 'fontalign':
                    self.p.card_title_align = 'float-'+tupled_data[i][2]
                    print('self.p.footer_font_size= ',self.p.footer_font_size)
                elif tupled_data[i][0] == 'button' and tupled_data[i][1] == 'align':
                    self.p.button_align = 'float-'+tupled_data[i][2]
                    print('self.p.button_align= ',self.p.button_align)
                elif tupled_data[i][0] == 'footer' and tupled_data[i][1] == 'fontalign':
                    self.p.footer_font_align = 'text-'+tupled_data[i][2]
                    print('self.p.footer_font_align= ',self.p.footer_font_align)
        
        self.p.file_writer()

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
            # print('Staging started')
            output = self.stage1()
            output = self.stage2(output)
            self.stage3(output)

    
print('modules loaded')
n = nlp()
# f = open('all inputs.txt','r') 
# # input_para = f.read().lower()
# input_para = n.paragraph.lower()
# sentences = input_para.split('.')

# for i in range(len(sentences)):
#     sentences[i] = sentences[i].strip()
#     n.tagged = n.intial_processing(sentences[i])

#     output = n.stage1()
#     output = n.stage2(output)
#     n.stage3(output)
