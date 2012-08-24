# -*- coding: utf-8 -*-

import sys
import os

from utils.report import Report 
from utils.xml2json_converter import XML2JSONConverter
from utils.cisis import CISIS
from utils.json2id import JSON2IDFile
from bhl_files_set import BHL_Files_Set

class BHL_LILACS:

    def __init__(self, xml_path, id_path, mst_path, report):
        self.files_set = BHL_Files_Set(xml_path, id_path, mst_path)
        self.report = report 
        self.xml2json_converter = XML2JSONConverter('_bhl2isis.txt', report)
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

           
    
    def generate_mst_files(self,  cisis, replace = True):
        xml_list = os.listdir(self.files_set.item_path)
        for xml in xml_list:
            xml_filename = self.files_set.item_path + '/' + xml
            id_filename = self.files_set.return_id_filename(xml)
            if os.path.exists(id_filename):
                if replace:
                    os.unlink(id_filename)
            if not os.path.exists(id_filename):
                self.generate_id_filename(xml_filename, id_filename)

            if os.path.exists(id_filename):
                mst_filename = self.files_set.return_mst_filename(xml)
                if os.path.exists(mst_filename + '.mst'):
                    if replace:
                        os.unlink(mst_filename + '.mst')
                        os.unlink(mst_filename + '.xrf')
                if not os.path.exists(mst_filename + '.mst'):
                    cisis.id2i(id_filename, mst_filename)
            else:
                self.report.log_error(' ! Expected ' + id_filename, True)
            

    def generate_id_filename(self, xml_filename, id_filename):
        self.report.log_event('Generating ' + id_filename + ' from ' + xml_filename)
        

        title_id = ''
        json = self.xml2json_converter.convert(xml_filename)
        if type(json) == type({}):
            json = json['doc']
            title_id = json['900']
            
        else:
            self.report.log_error(' ! Missing item data in ' + xml_filename , True)

        if len(title_id) > 0:
            title_xml_filename = self.files_set.return_xml_filename(title_id)
            json_title = self.xml2json_converter.convert(title_xml_filename)

            if type(json_title) == type({}):
                json_title = json_title['doc']
        
        
                json.update(json_title)

                #print(json)
                json = self.fix_data(json)
                
                json2id = JSON2IDFile(self.files_set.return_id_filename(xml_filename), self.report)
                json2id.format_and_save_document_data(json)
                #print(self.return_id_filename(xml_filename))
            else:
                self.report.log_error(' ! Missing title data in ' + title_xml_filename , True)
        
    def fix_data(self, json):
        v5 = json['71']
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
        if '85' in json.keys():
            if 'Brazil' in json['85']:
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

class DB:
    def __init__(self):
        pass 

    def generate_db(self, cisis, mst_path, db_filename, report):
        #cisis = CISIS('/var/www/lildbibio_scielo_org/bases/cisis1660')
        path = os.path.dirname(db_filename )
        if not os.path.exists(path):
            os.makedirs(path)

        if os.path.exists(path):
            mst_files = os.listdir(mst_path )
            for mst_filename in mst_files:
                if mst_filename.endswith('.mst'):
                    report.log_event('Appending ' + mst_filename, True)
                    mst_filename = mst_path + '/' + mst_filename.replace('.mst', '')
                    cisis.append(mst_filename, db_filename)

        
    
if __name__ == '__main__':

    #paths = ['/var/www/lildbibio_scielo_org/proc/xml_path/new', '/var/www/lildbibio_scielo_org/proc/xml_path/inproc', '/var/www/lildbibio_scielo_org/proc/xml_path/archive' ]
    #paths = ['/var/www/lildbibio_scielo_org/proc/teste/new', 'i', 't' ]

    #python3 bhl_lilacs.py cisis_path db_filename xml_path
    #python3 bhl_lilacs.py /var/www/lildbibio_scielo_org/bases/cisis1660 /var/www/lildbibio_scielo_org/bases/bhl/bhl /var/www/lildbibio_scielo_org/bases/bhl/bhl_xml

    from utils.parameters import Parameters

    parameter_list = ['', 'cisis path', 'db filename', 'xml path', 'id path', 'mst path', 'report_path', 'overwrite? (yes or no)']
    parameters = Parameters(parameter_list)
    if parameters.check_parameters(sys.argv):
        script_name, cisis_path, db_filename, xml_path, id_path, mst_path, report_path, replace = sys.argv
        

        log_filename, err_filename, summary_filename = (report_path + '/' + 'r.log', report_path + '/' +'r.err', report_path + '/' +'report.txt')
        report = Report(log_filename, err_filename, summary_filename, 0, False) 

        cisis = CISIS(cisis_path)
        

        proc = BHL_LILACS(xml_path, id_path, mst_path, report)
        
        from datetime import datetime
        d = datetime.now().isoformat()[0:10]
        bkp = db_filename + '.' + d
        if os.path.exists(db_filename + '.mst'):
            shutil.move(db_filename + '.mst', bkp + '.mst')
            shutil.move(db_filename + '.xrf', bkp + '.xrf')
            
        
        proc.generate_mst_files(cisis, (replace == 'yes'))

        db = DB()
        db.generate_db(cisis, mst_path, db_filename, report)

    else:
        parameter_list = ['', 'cisis path', 'db filename', 'mst path' , 'report_path']
        parameters = Parameters(parameter_list)
        if parameters.check_parameters(sys.argv):
            script_name, cisis_path, db_filename, mst_path, report_path = sys.argv

            log_filename, err_filename, summary_filename = (report_path + '/' + 'r.log', report_path + '/' +'r.err', report_path + '/' +'report.txt')
            report = Report(log_filename, err_filename, summary_filename, 0, False) 

            cisis = CISIS(cisis_path)
            db = DB()
            db.generate_db(cisis, mst_path, db_filename, report)
                    
