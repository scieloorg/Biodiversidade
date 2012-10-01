# -*- coding: utf-8 -*-

import sys
import os

from utils.xml2json_converter import XML2JSONConverter
from utils.json2id import JSON2IDFile

class BHL2JSON:

    def __init__(self, files_set, report):
        self.xml2json_converter = XML2JSONConverter('_bhl2isis.txt', report)
        self.files_set = files_set
        self.report = report

        try:
            f = open('lang.gzm.seq', 'r')
            c = f.readlines()
            f.close()
        except:
            f = open('lang.gzm.seq', 'r', encoding='iso-8859-1')
            c = f.readlines()
            f.close()

        self.languages = {}
        for r in c:
            pair = r.strip('\n').split('|')
            self.languages[pair[0]] = pair[1]
        
        self.tests = {}
        self.tests[' the '] = 'en'
        self.tests[' and '] = 'en'
        self.tests[' on '] = 'en'
        self.tests[' y '] = 'es'
        self.tests[' los '] = 'es'
        self.tests[' und '] = 'de'
        self.tests[' die '] = 'de'
        self.tests[' der '] = 'de'
        self.tests[' e '] = 'pt'
        self.tests[' as '] = 'pt'
        self.tests[' os '] = 'pt'
        self.tests[' i '] = 'it'
        self.tests[' gli '] = 'it'
        self.tests[' les '] = 'fr'
        self.tests[' aux '] = 'fr'
        self.tests[' le '] = 'fr'

    
    def generate_id_filename(self, item_xml_filename, id_filename):
        self.report.log_event('Generating ' + id_filename + ' from ' + item_xml_filename)
        

        title_id = item_id = ''
        json = self.xml2json_converter.convert(item_xml_filename)
        if type(json) == type({}):
            json = json['doc']
            title_id = json['900']
            item_id = json['901']
        else:
            self.report.log_error(' ! Missing item data in ' + item_xml_filename , True)

        if len(title_id) > 0:
            title_xml_filename = self.files_set.return_title_xml_filename(title_id)
            json_title = self.xml2json_converter.convert(title_xml_filename)

            if type(json_title) == type({}):
                json_title = json_title['doc']
                json.update(json_title)
        else:
            self.report.log_error(' ! Missing title data in ' + item_xml_filename , True)
    
        
                
        
        if len(item_id) > 0:
            #print(json)
            json = self.fix_data(json)
            
            json2id = JSON2IDFile(id_filename, self.report)
            json2id.format_and_save_document_data(json)
            #print(self.return_id_filename(xml_filename))
        else:
            self.report.log_error(' ! Missing item id ' + item_xml_filename , True)
    
    def fix_data(self, json):
        print(json)
        if '71' in json.keys():
            v5 = json['71']
        else:
            v5 = 'M'
        if 'Serial' in v5:
            json['5'] = 'S'
            json['6'] = 'ms'
            tag_title = '30'
            tag_volume = '31'
            tag_author = '10'
        elif 'Monograph/Item' in v5:
            json['5'] = 'M'
            json['6'] = 'm'
            tag_title = '18'
            tag_volume = '21'
            tag_author = '10'
        else:
            json['5'] = 'M'
            json['6'] = 'm'
            tag_title = '18'
            tag_volume = '21'
            tag_author = '10'
        if 'title' in json.keys():
            json[tag_title] = json['title']
            del json['title']
        if 'volume' in json.keys():
            json[tag_volume] = json['volume']
            del json['volume']
        json['1'] = 'BHL'
        json['92'] = 'AUTO'
        json['98'] = 'FONTE'
        json['9'] = 'a'
        json['110'] = 's'
        if '901' in json.keys():
            json['2'] = 'bhl-' + json['901']

        keywords = ''
        if '85' in json.keys():
            keywords = json['85']

        if 'Brazil' in keywords:
            json['999'] = 'BHL Brasil'
            json['4'] = 'bhlb'
        else:
            json['999'] = 'BHL Global'
            json['4'] = 'bhlg'
            
        if '8' in json.keys():
            json['8'] = '^u' + json['8'] + '^qpdf^yPDF^gFull text'
        
        tag = '10'
        if '10' in json.keys():
            authors = json['10']
            if type(authors) != type([]):
                authors = [authors]
            for author in authors:
                if 'Personal' in ' '.join(author.values()):
                    if json['5'] == 'M':
                        tag = '16'
                    elif json['5'] != 'S':
                        tag = '23'
                else:
                    if json['5'] == 'M':
                        tag = '16'
                    elif json['5'] == 'S':
                        tag = '11'
                    else:
                        tag = '24'
        if tag != '10':
            json[tag] = json['10']
            del json['10']
        json = self.fix_dateiso(json)
        json = self.fix_language(json)
        return json 

    

    def fix_language(self, json):
        if '40' in json.keys():
            if json['40'] in self.languages.keys():
                json['940'] = json['40']
                json['40'] = self.languages[json['40']]
        else:
            text = ''
            if '12' in json.keys():
                text += json['12'] + ' '
            if '18' in json.keys():
                text += json['18'] + ' '
            text = text.lower()
            for test, lang in self.tests.items():
                if test in text:
                    json['40'] = lang
                    break
        return json
    
    def fix_dateiso(self, json):
        fix = False
        if '65' in json.keys():
            if len(json['65']) != 8:
                fix = True
        else:
            fix = True
        if fix:
            year = ''
            if '64' in json.keys():
                year = json['64'].strip('.')
                
            elif '964' in json.keys():
                year = json['964']
                json['64'] = year

            if len(year) == 4 and year.isdigit():
                year += '0000'
            else:
                y = ''
                for ch in year:
                    if ch.isdigit():
                        y += ch
                        if len(y) == 4:
                            break
                if y in year:
                    year = y + '0000'
            json['65'] = year
        return json


