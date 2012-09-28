import sys
import os

from bhl_collection import BHL_Collection 
from bhl_item import BHL_Item 
from bhl_title import BHL_Title


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



class BHL_Download:

    def __init__(self, donwload_path, report):
        #self.donwload_path = donwload_path
        self.report = report

        self.item_path = donwload_path + '/i'
        self.title_path = donwload_path + '/t' 

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
        bhl_collection = BHL_Collection(self.report)
        bhl_item = BHL_Item(self.report)
        bhl_title = BHL_Title(self.report)

        while execute:
            bhl_collection.load(bhl_api, p_from, p_until, resumptionToken)

            item_id_list = bhl_collection.return_items_id()
            print(item_id_list)

            resumptionToken = bhl_collection.return_resumption()
            print(resumptionToken)

            for item_id in item_id_list:
                item_filename = self.return_new_filename('', item_id)
                print(item_filename)
                if replace_item:
                    if os.path.exists(item_filename):
                        os.unlink(item_filename)

                if not os.path.exists(item_filename):
                    print('downloaded')
                    bhl_item.download(bhl_api, item_id, item_filename)
                bhl_item.load(item_filename)
                
                title_id = bhl_item.return_title_id()
                title_filename = self.return_new_filename(title_id)
                print(title_filename)
                title_id = bhl_item.return_title_id()
                if replace_title:
                    if os.path.exists(title_filename):
                        os.unlink(title_filename)

                if not os.path.exists(title_filename):
                    print('downloaded')
                    bhl_title.download(bhl_api, title_id, title_filename)
                
            execute = (len(resumptionToken) > 0)
      
    
    
    def return_new_filename(self, title_id, item_id=''):
        filename = ''
        if item_id != '':
            filename = self.item_path + '/i' + item_id + '.xml'
            

        elif title_id != '':
            filename = self.title_path + '/t' + title_id + '.xml'
            

        
        
        return filename

    

if __name__ == '__main__':

    
    from utils.parameters import Parameters
    from utils.report import Report
    from configuration import Configuration

    configuration = Configuration('configuration.ini')
    if configuration.check_parameters(['REPORT_PATH', 'INBOX_PATH']):
        report_path, xml_path  = configuration.return_parameters(['REPORT_PATH', 'INBOX_PATH']) 
        
    
        parameter_list = ['', 'replace item', 'replace title', 'start date = iso date | start | current', 'end date = iso date | current ' ]
        parameters = Parameters(parameter_list)
    
        if parameters.check_parameters(sys.argv):
            script_name, rep_item, rep_title, start_date, end_date = sys.argv

            from datetime import  date, timedelta

            curr_date = date.today() - timedelta(days=5)
            next_date = date.today() + timedelta(days=1)
            
            next_date = next_date.isoformat()
            curr_date = curr_date.isoformat()

            if start_date == 'start' or start_date == '0' :
                start_date = '2009-03-28'
            elif start_date == 'current':
                start_date = curr_date
        
            if end_date == 'current':
                end_date = next_date
            elif end_date == '0':
                end_date = next_date      

            proc = BHL_Download(xml_path, Report(report_path + '/_bhl_xml.log', report_path + '/_bhl_xml.err', report_path + '/_bhl_xml.txt'))
            proc.download(start_date, end_date, rep_title == 'True', rep_item == 'True' )
    
                    
