import sys
import os
import shutil

from bhl2json import BHL2JSON

from utils.cisis import CISIS
from bhl_files_set import BHL_Files_Set


class BHL_LILACS:

    def __init__(self, cisis, files_set, report):
        self.cisis = cisis
        self.files_set = files_set
        self.bhl2json = BHL2JSON(files_set, report)
        self.report = report
        
    
    def files_count(self, path, pattern):
        c = os.listdir(path)

        c = [ filename for filename in c if filename.endswith(pattern) ]

        self.report.write('Files in ' + path + ': ' + str(len(c)), True, False)

    def generate_db_files(self, xml_src = 'new'):
        print('source of xml files: '  + xml_src )
        if xml_src == 'new':
            xml_path = self.files_set.inbox_path + '/i'
            archive_path = self.files_set.archive_xml_path
        else:
            xml_path = self.files_set.archive_xml_path
            archive_path = ''
        
        self.report.write('Processing XML from ' + xml_path, True )
        
        xml_list = os.listdir(xml_path)
        xml_list = [ xml for xml in xml_list if xml.endswith('.xml') and os.path.isfile(xml_path + '/' + xml) ]

        total_xml = len(xml_list)
        ok = 0
        empty_file = []
        

        self.files_count(self.files_set.archive_xml_path, '.xml')
        self.files_count(self.files_set.archive_id_path, '.xml.id')
        self.files_count(self.files_set.archive_db_path, '.xml.mst')
        self.files_count(self.files_set.archive_db_path, '.xml.xrf')

        

        self.report.write('There are ' + str(total_xml) + ' files in ' + xml_path, True )
        for xml in xml_list:
            xml_filename = xml_path + '/' + xml

            try:
                filesize = os.path.getsize(xml_filename)
            except:
                filesize = 0
            
            if filesize==0:
                self.report.write('Processing: Empty file ' + xml_filename, False, True)
                empty_file.append(xml_filename)
                os.unlink(xml_filename)
            else:
                
                id_filename = self.files_set.return_id_filename(xml)

                if os.path.exists(id_filename):
                    os.unlink(id_filename)
                if not os.path.exists(id_filename):
                    self.generate_id_filename(xml_filename, id_filename)
                if os.path.exists(id_filename):
                    if len(archive_path) > 0:
                        print('archive ' + xml_filename + ' -> ' +  archive_path + '/' + xml)
                        #self.archive(xml_filename, archive_path + '/' + xml)
                    
                    db_filename = self.files_set.return_db_filename(xml)
                    self.cisis.id2i(id_filename, db_filename)

                    if not os.path.exists(db_filename + '.mst'):
                        self.report.write('Unable to create db filename ' + db_filename, False, True)
                    else:
                        ok += 1
                else:
                    self.report.write('Unable to create id filename ' + id_filename, False, True)
        
        if ok != total_xml:
            self.report.write(str(ok) + '/' + str(total_xml) +  ' done.', True, False, True)

        self.files_count(xml_path, '.xml')
        self.files_count(self.files_set.archive_xml_path, '.xml')
        self.files_count(self.files_set.archive_id_path, '.xml.id')
        self.files_count(self.files_set.archive_db_path, '.xml.mst')
        self.files_count(self.files_set.archive_db_path, '.xml.xrf')
        


    def archive(self, src, dest):
        if os.path.exists(src):
            if os.path.exists(dest):
                os.unlink(dest)
            if not os.path.exists(dest):
                shutil.move(src, dest)
  
    def generate_db(self, db_filename):
        from datetime import date

        if os.path.exists(db_filename + '.mst'):
            d = date.today().isoformat()
            bkp = db_filename + '.' + d
            shutil.move(db_filename + '.mst', bkp + '.mst')
            shutil.move(db_filename + '.xrf', bkp + '.xrf')
        
        path = os.path.dirname(db_filename)
        if not os.path.exists(path):
            os.makedirs(path)

        if os.path.exists(path):
            db_files = os.listdir(self.files_set.archive_db_path )
            db_files = [ f[0:-4] for f in db_files if f.endswith('.mst')]

            self.report.write('db files: ' + str(len(db_files)), True)
            for db_file in db_files:
                self.report.write(db_file)
                db_file = self.files_set.archive_db_path + '/' + db_file
                self.cisis.append( db_file, db_filename)

    # /var/www/lildbibio_scielo_org/bases/bhl/archive/db/i105944.xml
    def generate_id_filename(self, xml_filename, id_filename):
        self.bhl2json.generate_id_filename(xml_filename, id_filename)

    
    
if __name__ == '__main__':

    #paths = ['/var/www/lildbibio_scielo_org/proc/xml_path/new', '/var/www/lildbibio_scielo_org/proc/xml_path/inproc', '/var/www/lildbibio_scielo_org/proc/xml_path/archive' ]
    #paths = ['/var/www/lildbibio_scielo_org/proc/teste/new', 'i', 't' ]
    #python3 bhl_lilacs.py /var/www/lildbibio_scielo_org/bases/cisis1660 /var/www/lildbibio_scielo_org/bases/bhl/bhl /var/www/lildbibio_scielo_org/proc/bhl_lilacs  /var/www/lildbibio_scielo_org/bases/bhl/bhl_xml
    from utils.parameters import Parameters
    from utils.report import Report
    from configuration import Configuration

    
    configuration = Configuration('configuration.ini')
    if configuration.check_parameters(['CISIS_PATH', 'REPORT_PATH', 'INBOX_PATH', 'ARCHIVE_PATH', 'DB_FILENAME']):
        cisis_path, report_path, inbox_path, archive_path, db_filename  = configuration.return_parameters(['CISIS_PATH', 'REPORT_PATH', 'INBOX_PATH', 'ARCHIVE_PATH', 'DB_FILENAME']) 
        
        parameter_list = ['', 'source of xml files: new|archive' ]
        parameters = Parameters(parameter_list)
    
        if parameters.check_parameters(sys.argv):
            script, xml_source = sys.argv
        
            if xml_source != 'archived' or xml_source != 'new':
                xml_source = 'new'

            cisis = CISIS(cisis_path)
            files_set = BHL_Files_Set(inbox_path, archive_path)
            report = Report(report_path + '/_bhl_db.log', report_path + '/_bhl_db.err', report_path + '/_bhl_db.txt')

            proc = BHL_LILACS(cisis, files_set, report)
        
            proc.generate_db_files(xml_source)
            proc.generate_db(db_filename)
