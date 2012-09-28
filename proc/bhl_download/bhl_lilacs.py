import sys
import os

from bhl_collection import BHL_Collection 
from bhl_item import BHL_Item 
from bhl_title import BHL_Title
from doc2isis import Doc2ISIS
from record2id import record2id
from cisis import CISIS

class BHL_LILACS:

    def __init__(self, cisis, new_path, inproc_path, archive_path):
        self.cisis = cisis

        self.new_xml_path = new_path
        
        self.new_db_path = new_path + '/db'
        if not os.path.exists(self.new_db_path):
            os.makedirs(self.new_db_path)

        self.inproc_xml_path = inproc_path + '/xml'
        if not os.path.exists(inproc_xml_path):
            os.makedirs(inproc_xml_path)

        self.inproc_db_path = inproc_path + '/db'
        if not os.path.exists(inproc_db_path):
            os.makedirs(inproc_db_path)

        
        self.archive_xml_path = archive_path + '/xml'
        if not os.path.exists(archive_xml_path):
            os.makedirs(archive_xml_path)

        self.archive_db_path = archive_path + '/db'
        if not os.path.exists(archive_db_path):
            os.makedirs(archive_db_path)


    def generate_db_files(self, xml_src = 'new'):
        if xml_src == 'new':
            xml_path = self.new_xml_path 
            archive_path = self.archive_xml_path
        else:
            xml_path = self.archive_xml_path
            archive_path = ''

        xml_list = os.listdir(xml_path)
        for xml in xml_list:
            xml_filename = xml_path + '/' + xml
            id_filename = self.return_id_filename(xml_filename)

            if os.path.exists(id_filename):
                os.unlink(id_filename)
            if not os.path.exists(id_filename):
                self.generate_id_filename(xml_filename, id_filename)
            if os.path.exists(id_filename):
                if len(archive_path) > 0:
                    self.archive(xml_filename, archive_path + '/' + xml)
                self.cisis.id2i(id_filename, id_filename.replace('.id', ''))
                

    def archive(self, src, dest):
        if os.path.exists(src):
            if os.path.exists(dest):
                os.unlink(dest)
            if not os.path.exists(dest):
                shutil.move(src, dest)
  
    def generate_db(self, db_filename):
        #cisis = CISIS('/var/www/lildbibio_scielo_org/bases/cisis1660')
        path = os.path.dirname(db_filename)
        if not os.path.exists(path):
            os.makedirs(path)

        if os.path.exists(path):
            mst_files = os.listdir(self.mst_path )
            for mst_filename in mst_files:
                mst_filename = self.mst_path + '/' + mst_filename
                self.cisis.append(mst_filename, db_filename)


    def generate_id_filename(self, xml_filename, id_filename, report):
        bhl_item = BHL_Item(report)
        bhl_title = BHL_Title(report)
        doc2isis = Doc2ISIS()

        bhl_item.load_xml(xml_filename)
        title_id = bhl_item.return_title_id()
        
        item_metadata = bhl_item.return_item_metadata()
        print(item_metadata[0].fields)
        title_filename = self.return_new_filename(title_id)

        print(title_filename)
        bhl_title.load_xml(title_filename)

        title_metadata = bhl_title.return_metadata()
        print(title_metadata.fields)

        title_metadata.set_items(item_metadata)
        
        title_metadata.set_title_id(title_id)
        #title_metadata.set_oai_date(oai_date_list[i] + '^d' + query_date)

        print(title_metadata.fields)
        records = doc2isis.generate_records(title_metadata)

        print(records)
        r2id = record2id(id_filename)
        for r in records:
            r2id.save(r)
        r2id.close_files()
        

    

    

    def return_id_filename(self, archive_path, item_xml_name):
        name = os.path.basename(item_xml_name).replace('.xml', '.id')
        return self.archive_db_path + '/' + name

    def return_new_filename(self, title_id, item_id=''):
        filename = ''
        if item_id != '':
            filename = 'i/i' + item_id + '.xml'
            

        elif title_id != '':
            filename = self.new_xml_path + '/t/t' + title_id + '.xml'
        return filename

    
if __name__ == '__main__':

    #paths = ['/var/www/lildbibio_scielo_org/proc/xml_path/new', '/var/www/lildbibio_scielo_org/proc/xml_path/inproc', '/var/www/lildbibio_scielo_org/proc/xml_path/archive' ]
    #paths = ['/var/www/lildbibio_scielo_org/proc/teste/new', 'i', 't' ]
    #python3 bhl_lilacs.py /var/www/lildbibio_scielo_org/bases/cisis1660 /var/www/lildbibio_scielo_org/bases/bhl/bhl /var/www/lildbibio_scielo_org/proc/bhl_lilacs  /var/www/lildbibio_scielo_org/bases/bhl/bhl_xml
    
    
    
    paths = ['_new', '_inproc', '_archive' ]
    
    from parameters import Parameters

    parameter_list = ['', 'cisis path', 'db filename', 'report path', 'xml path']
    parameters = Parameters(parameter_list)

    if parameters.check_parameters(sys.argv):
        script_name, cisis_path, db_filename, report_path, xml_path = sys.argv

        report = Report(report_path + '/_bhl_db.log', report_path + '/_bhl_db.err', report_path + '/_bhl_db.txt')

        proc = BHL_LILACS(paths[0], paths[1], paths[2])
        cisis = CISIS(cisis_path)

        from datetime import date

        d = date.today().isoformat()
        bkp = db_filename + '.' + d
        if os.path.exists(db_filename + '.mst'):
            shutil.move(db_filename + '.mst', bkp + '.mst')
            shutil.move(db_filename + '.xrf', bkp + '.xrf')
        
        proc.generate_db_files(cisis, True)
        #proc.generate_db(cisis, db_filename)

    

                    
