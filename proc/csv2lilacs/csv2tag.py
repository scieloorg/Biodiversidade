#!/usr/bin/env python
# *-* coding: iso-8859-1 *-*

import datetime

class csv2tag:


    def __init__(self, convertion_table_filename):
        self.languages = {'Por':'pt', 'Ing':'en', 'Esp':'es'}
        self.convertion_table = []
        self.labels = []
        self.load(convertion_table_filename)

    def load(self,filename):
        f = open(filename,'r')
        lines = f.readlines()
        for l in lines:
            v = l.split('|')
            self.convertion_table.append(v[1].strip("\n"))
            self.labels.append(v[0])

    def convert(self, content_filename, separator):
        # f = open(content_filename,'r', encoding='iso-8859-1')
        f = open(content_filename,'r')
        c = f.read()
        f.close()
        
        
        c = c.replace('|' + "\r\n", "|NOVALINHA")
        c = c.replace("\r\n", " ").replace("  "," ")
        c = c.replace("NOVALINHA", "\r\n")
        rows = c.split("\r\n")
        
        r = []
        row_index = 0
        done_count = 0 
        new_count = 0
        new_content = []
        for row in rows:
            row_index += 1
            cols = str(row).split(separator)
            test_row = row.replace('|','').replace(' ','')
            
            print "Line " + str(row_index)+ "/" + str(len(rows)) +   ": " + row[:50] + "..."
            
            if test_row=='':
                print "  invalid line..."
            else:
                print "  loading..."
                converted = {}
                col_idx = 0
                original = []
                if cols[0] == '':
                    cols[0] = self.generate_field2()
                    print "  creating a new id"
                    new_count = new_count  + 1
                    new_content.append(cols[0] + row)
                else:
                    new_content.append(row)
                    
                for tag in self.convertion_table:                
                    converted[tag] = []
                    data = cols[col_idx].replace('VIRGULA',',').replace('PONTOCOMMA',';')
                    converted[tag].append(data)
                    original.append(data + '^x' + self.labels[col_idx])
                
                    col_idx += 1
                converted['990'] = original

                converted = self.fix(converted)
                r.append(converted)
        
        f = open(content_filename + '.new','w')
        for s in new_content:
            f.write(s)
        f.close()
        
        print "Loaded: " + str(len(r)) + "/" + str(len(rows))
        print "new id: " + str(new_count) + "/" + str(len(r))
        return r

    def fix(self, data):
        lang = ''
        try:
            lang = self.get_lang(data['40'][0])
        except:
            lang = ''
            
        data['2'] = self.fix_id(data['900'][0])
        if data['8']:            
            data['8'] = self.fix_url(data['8'][0], lang)
        if data['12']:
            data['12'] = self.fix_titles_or_abstracts(data['12'][0])
            data['13'] = self.fix_title_translated_to_english(data['12'])
        if data['83']:
            data['83'] = self.fix_titles_or_abstracts(data['83'][0])
        if data['85']:
            data['85'] = self.fix_keywords(data['85'][0])
        if data['10']:
            data['10'] = self.fix_authors(data['10'][0])
        if data['14']:
            data['14'] = self.fix_pages(data['14'][0])
        if data['65']:
            data['65'] = self.fix_dateiso(data['65'][0])

        data['40'] = self.fix_lang(data['12'][0])
        return data


    def fix_lang(self,data):
        r = []
        r.append(data[data.find('^i')+2:])
        return r


    def generate_field2(self ):
        t = datetime.date.today().isoformat().replace('-','')
        now = datetime.datetime.now().timetuple()
        h = '0' + str(now[4])
        h = h[-2:]
        min = '0' + str(now[5])
        min = min[-2:]
        seg = '0' + str(now[6])
        seg = seg[-2:]
        return  t + h + min + seg 


    def fix_id(self, data):
        r = []
        r.append( str(50000000000000 + int(data)))
        return r

    def fix_url(self, data, language):
        # ^uhttp://www.scielo.br/scielo.php?script=sci_arttext&pid=S0102-86502001000200001&lng=pt&nrm=iso^qphp^yHTML DINÂMICO^gTexto completo^ipt'
        # [Português - Scielo] <a href='http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0101-81752007000400001&lng=pt&nrm=iso&tlng=pt' target='_blank'>http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0101-81752007000400001&lng=pt&nrm=</a>
        url = ''
        lang = ''
        r = []
        
        if '>' in data:
            temp = data[data.find('>')+1:]
            if '</a>' in temp:
                temp = temp[:temp.find('</a>')]
            url = temp
        else:
            if 'http:'  in data:
                url = data[data.find('http:'):]
            else:
                if data[0] == '[':
                    if ']'  in data:
                        url = data[data.find(']')+1]
                else:
                    url = data
                    
        if '[' in data:
            if '-' in data:
                lang = data[data.find('[')+1:data.find('-')].strip(' ')
                lang = self.get_lang(lang)
        if url=='':
             url = data
             
        if lang==''  or language!='':
             lang = language
        
        q = ''
        if '.pdf' in url:
            q = '^qpdf^yPDF' 
        else:
            if '.php' in url:
                q = '^qphp^yHTML DINåMICO'
            else:
                if '.htm' in url:
                    q = '^qHTML^yHTML' 
                else:
                    q = '^qweb^HTML DINåMICO' 
        
        print data
        print "  " + url 
        
        if not url=='' and not lang=='':
            r.append('^u' + url + q + '^gTexto completo^i' + lang)

        return r

    def get_lang(self,lang):
        l = lang
        lang = lang.strip(' ')
        lang = lang[0:3]
        if lang in self.languages:
            l =  self.languages[lang]
        return l

    def fix_title_translated_to_english(self, titles):
        k=0
        r = []
        removeit = ''
        for t in titles:
            if t.find('^ien')>0:
                if k>0:
                    r.append(t.replace('^ien',''))
                    removeit = t
                    
        if not removeit == '':
            titles.remove(t)
            k+=1
        return r

    def fix_titles_or_abstracts(self,data):
        
        r = []
        #print('_____')
        #print(data)
        items = data.split(', [')
        for it in items:
            if not it == '':
                if '[' in it:
                    v = it.split(']')
                    if '[' in v[0] :
                        v[0] = v[0][1:]
                    #print(v)
                    r.append( v[1].strip() + '^i' + self.get_lang(v[0]))
                else:
                    r.append(it + '^i' + self.try_lang(it) )
        return r

    def try_lang(self, text):
        lang = 'en' 
        
        return lang
    def fix_authors(self, data):
        #Santos-Wisniewski, Maria José, Rocha, Odete, Guntzel, Adriana Maria, Matsumura-Tundisi, Takako (Instituto Internacional de Ecologia (IIE) São Carlos Brasil)
        #Silva, Regina^1Universidade Federal de São Paulo^2Escola Paulista de Medicina^3Departamento de Enfermagem. Disciplina de Otorrinolaringologia. Sessão de Fonética^pBrasil^cSão Paulo
        r = []
        SEP_AUTHOR = ', '
        k=0
        #print(' ')
        #print(' inicio ')
        #print(data)
        data = data.replace('"', '')
        
        aff_and_authors = data.split('),')
        #print(aff_and_authors)
        for aff_author in aff_and_authors:
            if '(' in aff_author:
                authors = aff_author[0:aff_author.find('(')].split(SEP_AUTHOR)
                aff = aff_author[aff_author.find('(')+1:]
                aff = '^1' + aff.replace('(', '^9').replace('). ','^2')
                aff_parts = aff.split(' ')                
                aff_parts.reverse()

                country = '^p' + aff_parts[0]
                city = aff_parts[1]
                if aff_parts[2] in 'São de dos das':
                    city = aff_parts[2]+ ' '+ city
                if aff_parts[2] in 'de dos das':
                    city = aff_parts[3]+ ' '+ city
                c = city
                city = '^c' + city
                aff = aff[0:aff.rfind(c)] + city + country
            else:
                authors = aff_author.split(SEP_AUTHOR)
                aff = ''
            a = ''
            for author in authors:
                if a == '':
                    a = author + SEP_AUTHOR
                else:
                    a = a + author
                    r.append( a + aff)
                    a = ''
                    #print(r[k])
                    
        #print(' fim ')
        #print(' ')
        return r

    def fix_keywords(self,data):
        r = data.split(' - ')
        r = [ i + '^ipt' for i in r ]
        return r

    def fix_pages(self,data):
        r =[]
        if '-' in data:
            s = '^f' + data.replace('-','^l').replace(' ','')
        else:
            s = '^f' + data
        r.append(s)
        return r

    def fix_dateiso(self,data):
        r = []
        r.append(data + '0000')
        return r

