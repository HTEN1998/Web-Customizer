import re
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from indexpage_writer import html_writer

class nlp():
    labels = []
    tagged = []

    def stage1(self):

        output = []
        element_item = attribute_item = value_item =''
        element_found_flag = 0
        count = 0

        f = open('E:\DELL\Documents\WebCustomizer\corpus.json','r')
        data = json.load(f)

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
        
        print('stage 1 output= ',output)
        return output

    def stage2(self,List_of_tuples):

        def check_history(current_index):
            for i in range(0,current_index+1):
                if List_of_tuples[i][0] == List_of_tuples[current_index][0] and List_of_tuples[i][1] == List_of_tuples[current_index][1] and current_index!=0:
                    List_of_tuples[current_index][1] = 'fontcolor'
                    break

        print('--> Element processing done')

        for i in range(0,len(List_of_tuples)):
            if List_of_tuples[i][0] == '' and i-1>=0:
                List_of_tuples[i][0] = List_of_tuples[i-1][0]
        
        for i in range(0,len(List_of_tuples)):
            if List_of_tuples[i][0] == '':
                List_of_tuples.remove(List_of_tuples[i])
                break

        print('--> attribute processing done')

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
        p = html_writer()

        for i in range(0,len(tupled_data)):

            if tupled_data[i][0] == 'website' and tupled_data[i][1] == 'title':
                p.website_name = tupled_data[i][2]
            elif tupled_data[i][0] == 'website' and tupled_data[i][1] == 'tagline':
                p.website_tagline = tupled_data[i][2]
            elif tupled_data[i][0] == 'card' and tupled_data[i][1] == 'title':
                p.card_title = tupled_data[i][2]
            elif tupled_data[i][0] == 'button' and tupled_data[i][1] == 'title':
                p.button_title = tupled_data[i][2]
            
            elif tupled_data[i][0] == 'navbar' and tupled_data[i][1] == 'fontcolor':
                p.navbar_font_color = 'navbar-'+tupled_data[i][2]
            elif tupled_data[i][0] == 'dropdown' and tupled_data[i][1] == 'fontcolor':
                p.dropdown_font_color = 'text-'+tupled_data[i][2]
            elif tupled_data[i][0] == 'footer' and tupled_data[i][1] == 'fontcolor':
                p.footer_font_color = 'text-'+tupled_data[i][2]

            elif tupled_data[i][0] == 'navbar' and tupled_data[i][1] == 'color':
                p.navbar_bgcolor = 'bg-'+tupled_data[i][2]
            elif tupled_data[i][0] == 'dropdown' and tupled_data[i][1] == 'color':
                p.dropdown_bgcolor = 'bg-'+tupled_data[i][2]
            elif tupled_data[i][0] == 'footer' and tupled_data[i][1] == 'color':
                p.footer_bgcolor = 'bg-'+tupled_data[i][2]
            elif tupled_data[i][0] == 'button' and tupled_data[i][1] == 'color':
                p.button_color = 'bg-'+tupled_data[i][2]

            elif tupled_data[i][0] == 'card' and tupled_data[i][1] == 'fontsize':
                p.card_font_size = tupled_data[i][2]
            elif tupled_data[i][0] == 'footer' and tupled_data[i][1] == 'fontsize':
                p.footer_font_size = tupled_data[i][2]
            elif tupled_data[i][0] == 'card' and tupled_data[i][1] == 'fontalign':
                p.card_title_align = 'float-'+tupled_data[i][2]
            elif tupled_data[i][0] == 'button' and tupled_data[i][1] == 'align':
                p.button_align = 'float'+tupled_data[i][2]
            elif tupled_data[i][0] == 'footer' and tupled_data[i][1] == 'fontalign':
                p.footer_font_align = 'text'+tupled_data[i][2]
        
        p.file_writer()


    def intial_processing(self,user_input):
        self.labels = re.findall("'([^']*)'",user_input)

        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(user_input)
        filtered_sentence = [w for w in word_tokens if not w in stop_words] #stopwords removed
        
        start_location = -1
        label_found = 0
        count = 0
        for words in filtered_sentence:
            if label_found == 1:
                filtered_sentence.remove(words)

            if len(words)>1 and words[0] == "'":
                label_found = 1
                start_location = filtered_sentence.index(words)
                filtered_sentence[start_location] = self.labels[count]
                count+=1
            if len(words) == 1 and words == "'":
                    filtered_sentence.remove(words)
                    label_found = 0
        
        print('tokens= ',filtered_sentence)
        return filtered_sentence


n = nlp()
user_input1 = 'make the navbar color blue, and the whole page font 25px,the background of the page should be green.'
user_input2 =  'change color of the navigation bar to red and make the navigation font a bit bigger, and color them bold black.'
user_input3 = "I want website name to be change to 'Amazon' and with tagline as 'shop in your style' ."
user_input = input()
n.tagged = n.intial_processing(user_input)

output = n.stage1()
output = n.stage2(output)
n.stage3(output)

