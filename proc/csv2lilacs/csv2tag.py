#!/usr/bin/env python
# *-* coding: iso-8859-1 *-*
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
        f = open(content_filename,'r', encoding='iso-8859-1')
        rows = f.readlines()
        f.close()
	    
        r = []
        for row in rows:
            #print('...')
            #print('==LINHA ' + str(k) + '===')
            converted = {}
            cols = str(row).split(separator)
            col_idx = 0
            original = []
            for tag in self.convertion_table:                
                converted[tag] = []
                data = cols[col_idx].replace('VIRGULA',',').replace('PONTOCOMMA',';')
                converted[tag].append(data)
                original.append(data + '^x' + self.labels[col_idx])
                
                col_idx += 1
            converted['990'] = original
            converted = self.fix(converted)
            r.append(converted)
            
        return r

    def fix(self, data):
        data['2'] = self.fix_id(data['900'][0])
        if data['8']:            
            data['8'] = self.fix_url(data['8'][0])
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

    def fix_id(self,data):
        r = []
        r.append(str(50000000000000 + int(data)))
        return r

    def fix_url(self,data):
        # ^uhttp://www.scielo.br/scielo.php?script=sci_arttext&pid=S0102-86502001000200001&lng=pt&nrm=iso^qphp^yHTML DINÂMICO^gTexto completo^ipt'
        # [Português - Scielo] <a href='http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0101-81752007000400001&lng=pt&nrm=iso&tlng=pt' target='_blank'>http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0101-81752007000400001&lng=pt&nrm=</a>
        url = ''
        lang = ''
        r = []
        
        if '>' in data:
            if '</a>' in data:
                url = data[data.find('>')+1:data.rfind('</a>')]
        if '[' in data:
            if '-' in data:
                lang = data[data.find('[')+1:data.find('-')].strip(' ')
                lang = self.get_lang(lang)
                    
        if not url=='' and not lang=='':
            r.append('^u' + url + '^qphp^yHTML DINÂMICO^gTexto completo^i' + lang)

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
                v = it.split(']')
                if '[' in v[0] :
                    v[0] = v[0][1:]
                #print(v)
                r.append( v[1].strip() + '^i' + self.get_lang(v[0]))
                
        return r

    
    def fix_authors(self, data):
        #Santos-Wisniewski, Maria José, Rocha, Odete, Guntzel, Adriana Maria, Matsumura-Tundisi, Takako (Instituto Internacional de Ecologia (IIE) São Carlos Brasil)
        #Silva, Regina^1Universidade Federal de São Paulo^2Escola Paulista de Medicina^3Departamento de Enfermagem. Disciplina de Otorrinolaringologia. Sessão de Fonética^pBrasil^cSão Paulo
        r = []
        SEP_AUTHOR = ', '
        k=0
        #print(' ')
        #print(' inicio ')
        #print(data)

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

