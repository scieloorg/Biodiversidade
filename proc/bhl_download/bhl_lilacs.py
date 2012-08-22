import sys
import os

from bhl_collection import BHL_Collection 
from bhl_item import BHL_Item 
from bhl_title import BHL_Title
from doc2isis import Doc2ISIS
from record2id import record2id
from cisis import CISIS

class BHL_LILACS:

    def __init__(self, new_path, inproc_path, archive_path):
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
        bhl_item = BHL_Item()
        bhl_title = BHL_Title()
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

        proc = BHL_LILACS(paths[0], paths[1], paths[2])
        cisis = CISIS(cisis_path)
        from datetime import datetime
        d = datetime.now().isoformat()[0:10]
        bkp = db_filename + '.' + d
        if os.path.exists(db_filename + '.mst'):
            shutil.move(db_filename + '.mst', bkp + '.mst')
            shutil.move(db_filename + '.xrf', bkp + '.xrf')
            
        
        proc.generate_mst_files(cisis, True)
        #proc.generate_db(cisis, db_filename)

    

                    
