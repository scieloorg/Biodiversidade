from record2id  import record2id
from doc2isis import Doc2ISIS

from BHL_DATA_PROVIDER import BHL_DATA_PROVIDER


import os
import time



def create_path(path):
    try:
        os.mkdirs(path)
    except os.error:
        pass

def format(num):
    if num in range(1,10):
        return '0' + str(num)
    else:
        return str(num)
    
class BHL2LILACS:
    def __init__(self, xml_path, id_filename, debug=False):
        self.bhl_data = BHL_DATA_PROVIDER(xml_path)                       
        self.debug = debug
        self.doc2isis = Doc2ISIS()
        self.id_filename = id_filename
        
    def display_debug_message(self, message):
        if self.debug:
            print(message)
            
    def create_id_filename(self, processed_filename, p_from='', p_until=''):
        """
        create_id_filename
        """
        localtime = time.localtime(time.time())
        min_month = 3
        min_day = 29
        max_month = 13
        max_day = 32

        f = open(processed_filename)
        excluded_id_list = f.readlines()
        excluded_id_list = [ e.strip("\n") for e in excluded_id_list ]
        f.close()


        #print(excluded_id_list)
        self.display_debug_message('create_id_filename')

        self.r2id = record2id(self.id_filename)
        if p_from=='' and p_until=='':
            self.display_debug_message('create_id_filename for all')
            curr_date = str(localtime[0])+'-'+ str(localtime[1])+'-'+ str(localtime[2])
            previous=''
            for year in range(2009, localtime[0]+1):
                if year > 2009:
                    min_month = 1
                    min_day = 1
                for month in range(min_month, max_month):
                    for day in range(min_day, max_day):
                        curr = str(year) + '-' + format(month) + '-' + format(day)
                        if previous:
                            self.__get_data_and_create_records__(excluded_id_list, previous, curr)
                            if curr_date == previous:
                                max_month=1
                                max_day=1
                        previous = curr
                    min_day = 1
                min_month=1
        else:
            self.display_debug_message('create_id_filename for ' + p_from+ ' ' + p_until)
            self.__get_data_and_create_records__(excluded_id_list, p_from, p_until)
        self.r2id.close_files()
                    
    
    def __get_data_and_create_records__(self, excluded_id_list, p_from, p_until):
        """
        1) Query BHL items create between the date range p_from and p_until and
        2) Write in id_filename
        """
        if self.r2id:
            self.display_debug_message('Debug: executing download_most_recent_items ' + p_from +',' + p_until)

            f = open('last_date','w')
            f.write(p_until)
            f.close()

            item_id_list = self.bhl_data.get_item_id_list(p_from, p_until)
            for item_id in item_id_list:
                self.display_debug_message('Debug: item_id: '+item_id)
                item_metadata = self.bhl_data.get_item_metadata(item_id)

                if item_metadata:
                    title_id = item_metadata[0].get_primary_title_id()
                    # id in exclusion list?
                    test = item_id + '|' + title_id[0]
                    self.display_debug_message('Debug: test '+test)
                    if not test in excluded_id_list:
                        self.display_debug_message('Debug: do it')
                        self.display_debug_message('  get_title_metadata')
                        title_metadata = self.bhl_data.get_title_metadata(title_id[0])
                        title_metadata.set_items(item_metadata)
                        title_metadata.set_oai_date(p_from)

                        self.display_debug_message('  generate_records')
                        records = self.doc2isis.generate_records(title_metadata)
                        for r in records:
                            self.display_debug_message('  save')
                            self.r2id.save(r)
                            self.display_debug_message('  saved')
                        
                else:
                    self.display_debug_message('Debug: ERROR no item_metadata ')

        #return list
