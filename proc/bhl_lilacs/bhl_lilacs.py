import sys
import os

from utils.report import Report 
from utils.xml2json_converter import XML2JSONConverter
from utils.cisis import CISIS
from utils.json2id import JSON2IDFile

class BHL_LILACS:

    def __init__(self, new_path, inproc_path, archive_path, report):
        self.new_path = new_path
        if not os.path.exists(new_path):
            os.makedirs(new_path)

        self.id_path = inproc_path

        self.inproc_path = inproc_path
        if not os.path.exists(inproc_path):
            os.makedirs(inproc_path)

        self.archive_path = archive_path
        if not os.path.exists(archive_path):
            os.makedirs(archive_path)

        self.report = report 
        self.xml2json_converter = XML2JSONConverter('_bhl2isis.txt', report)
        f = open('lang.gzm.seq', 'r')
        c = f.readlines()
        f.close()

        self.languages = {}
        for r in c:
            pair = r.strip('\n').split('|')
            self.languages[pair[0]] = pair[1]
        print(self.languages)
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
        xml_list = os.listdir(self.new_path + '/i')
        for xml in xml_list:
            xml_filename = self.new_path + '/i/' + xml
            id_filename = self.return_id_filename(xml_filename)
            if os.path.exists(id_filename):
                if replace:
                    os.unlink(id_filename)
            if not os.path.exists(id_filename):
                self.generate_id_filename(xml_filename, id_filename)
                #mst_filename = id_filename.replace('.id', '').replace(self.id_path, self.archive_path )
                #cisis.id2i(id_filename, mst_filename)
            
    def generate_db(self, cisis, db_filename):
        #cisis = CISIS('/var/www/lildbibio_scielo_org/bases/cisis1660')
        path = os.path.dirname(db_filename)
        if not os.path.exists(path):
            os.makedirs(path)

        if os.path.exists(path):
            mst_files = os.listdir(self.archive_path )
            for mst_filename in mst_files:
                mst_filename = self.archive_path + '/' + mst_filename
                cisis.append(mst_filename, db_filename)


    def generate_id_filename(self, xml_filename, id_filename):
        json = self.xml2json_converter.convert(xml_filename)
        
        json = json['doc']
        title_id = json['900']
        title_xml_filename = self.return_new_filename(title_id)
        json_title = self.xml2json_converter.convert(title_xml_filename)
        
        json_title = json_title['doc']
        
        
        json.update(json_title)

        print(json)
        json = self.fix_data(json)
        json2id = JSON2IDFile(self.return_id_filename(xml_filename), self.report)
        json2id.format_and_save_document_data(json)
        print(self.return_id_filename(xml_filename))
    
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

    def return_id_filename(self, item_xml_name):
        
        return item_xml_name.replace('.xml', '.id').replace(self.new_path, self.id_path).replace('/i/', '/')

    def return_new_filename(self, title_id, item_id=''):
        filename = ''
        if item_id != '':
            filename = 'i/i' + item_id + '.xml'
            

        elif title_id != '':
            filename = 't/t' + title_id + '.xml'
            

        r = ''
        if len(filename) > 0:
            r = self.new_path + '/' + filename 
        
        return r

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
        
    
if __name__ == '__main__':

    #paths = ['/var/www/lildbibio_scielo_org/proc/xml_path/new', '/var/www/lildbibio_scielo_org/proc/xml_path/inproc', '/var/www/lildbibio_scielo_org/proc/xml_path/archive' ]
    #paths = ['/var/www/lildbibio_scielo_org/proc/teste/new', 'i', 't' ]

    p = '/Users/robertatakenaka/github.com/scieloorg/Biodiversidade/proc/test'
    if os.path.exists(p):
        path = p
    else:
        path = '/var/www/lildbibio_scielo_org/proc/xml_path/new'
    paths = [path, 'i', 't' ]
    
    from parameters import Parameters

    parameter_list = ['', 'cisis path', 'db filename']
    parameters = Parameters(parameter_list)
    if parameters.check_parameters(sys.argv):
        script_name, cisis_path, db_filename = sys.argv
        log_filename, err_filename, summary_filename = (path + '/' + 'r.log', path + '/' +'r.err', path + '/' +'report.txt')
        cisis = CISIS(cisis_path)
        report = Report(log_filename, err_filename, summary_filename, 0, False) 

        proc = BHL_LILACS(paths[0], paths[1], paths[2], report)
        
        from datetime import datetime
        d = datetime.now().isoformat()[0:10]
        bkp = db_filename + '.' + d
        if os.path.exists(db_filename + '.mst'):
            shutil.move(db_filename + '.mst', bkp + '.mst')
            shutil.move(db_filename + '.xrf', bkp + '.xrf')
            
        
        proc.generate_mst_files(cisis, True)
        #proc.generate_db(cisis, db_filename)

    

                    
