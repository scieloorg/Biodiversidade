import sys
import os

from bhl_collection import BHL_Collection 
from bhl_item import BHL_Item 
from bhl_title import BHL_Title
from doc2isis import Doc2ISIS
from record2id import record2id

def read_file(filename):
    f = open(filename,'r')
    list = f.read()
    f.close()
    return list

def save_file(file_name, file_content, mode='wb'):
    if not file_content=='':
        f = open(file_name, mode)
        f.write(file_content)
        f.close()

def generate_call():
    year = ['2009', '2010', '2011', '2012']
    year.reverse()

    months = range(1,13)
    months = [ '00' + str(m) for m in months  ]
    months = [ m[-2:] for m in months ]
    months.reverse()

    days = range(1,29)
    days = [ '00' + str(d) for d in days  ]
    days = [ d[-2:] for d in days ]
    days.reverse()

    limit_min = '2009-03-28'
    limit_max = '2012-08-01'
    for y in year:
        for m in months:
            for d in days:
                #proc.download('2012-08-01', '2012-08-17')
                year2 = y
                month2 = m

                if d == '28':
                    day2 = '01'
                    if m == '12':
                        month2 = '01'
                        year2 = str(int(y) + 1)
                    else:
                        month2 = '00' + str(int(m) + 1)
                        month2 = month2[-2:]
                else:
                    day2 = '00' + str(int(d) + 1)
                    day2 = day2[-2:]
                date1 = y + '-' + m + '-' + d
                date2 = year2 + '-' + month2 + '-' + day2

                if limit_min <= date1 <= limit_max:
                    print('python3 bhl_download_manager.py ' + date1 + ' ' + date2 + ' False False')

class BHL_DownloadManager:

    def __init__(self, donwload_path, item_subdir, title_subdir):
        #self.donwload_path = donwload_path
        

        self.item_path = donwload_path + '/' + item_subdir
        self.title_path = donwload_path + '/' + title_subdir

        if not os.path.exists(self.item_path):
            os.makedirs(self.item_path)
        if not os.path.exists(self.title_path):
            os.makedirs(self.title_path)
        

    def download(self, p_from, p_until, replace_item = True, replace_title = False):
        """
        Query BHL items create between the date range p_from and p_until and
        
        """
        from BHL_API import BHL_API 

        execute = True
        resumptionToken = ''
        
        bhl_api = BHL_API()
        bhl_collection = BHL_Collection()
        bhl_item = BHL_Item()
        bhl_title = BHL_Title()

        while execute:
            bhl_collection.load(bhl_api, p_from, p_until, resumptionToken)

            item_id_list = bhl_collection.return_items_id()
            resumptionToken = bhl_collection.return_resumption()

            for item_id in item_id_list:
                bhl_item.load(bhl_api, item_id)
                title_id = bhl_item.return_title_id()
                bhl_title.load(bhl_api, title_id)
                self.download_item(item_id, bhl_item.xml, title_id, bhl_title.xml, replace_item, replace_title)
            execute = (resumptionToken != '')
      
    
    def download_item(self, item_id, item_xml, title_id, title_xml, replace_item, replace_title):
        title_filename = self.return_new_filename(title_id)
        item_filename = self.return_new_filename(title_id, item_id)

        if replace_item:
            if os.path.exists(item_filename):
                os.unlink(item_filename)
        if replace_title:           
            if os.path.exists(title_filename):
                os.unlink(title_filename)

        if not os.path.exists(item_filename):
            save_file(item_filename, item_xml, 'w')
        if not os.path.exists(title_filename):
            save_file(title_filename, title_xml, 'w')


    
    
    def return_new_filename(self, title_id, item_id=''):
        filename = ''
        if item_id != '':
            filename = self.item_path + '/i' + item_id + '.xml'
            

        elif title_id != '':
            filename = self.title_path + '/t' + title_id + '.xml'
            

        
        
        return filename

    

if __name__ == '__main__':

    paths = ['/var/www/lildbibio_scielo_org/proc/xml_path/new', 'i', 't']
    from parameters import Parameters

    parameter_list = ['', 'start date', 'end date', 'replace item', 'replace title']
    parameters = Parameters(parameter_list)
    if parameters.check_parameters(sys.argv):
        script_name, start_date, end_date, rep_title, rep_item = sys.argv
        proc = BHL_DownloadManager(paths[0], paths[1], paths[2])
        proc.download(start_date, end_date, rep_title == 'True', rep_item == 'True' )
    else:
        generate_call()

                    
