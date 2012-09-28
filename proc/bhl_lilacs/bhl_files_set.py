# -*- coding: utf-8 -*-

import sys
import os


class BHL_Files_Set:

    def __init__(self, inbox_path, archive_path):
        self.inbox_path = inbox_path
        if not os.path.exists(self.inbox_path):
            os.makedirs(self.inbox_path)

        
        self.archive_xml_path = archive_path + '/xml'
        if not os.path.exists(self.archive_xml_path):
            os.makedirs(self.archive_xml_path)

        self.archive_db_path = archive_path + '/db'
        if not os.path.exists(self.archive_db_path):
            os.makedirs(self.archive_db_path)

        self.archive_id_path = archive_path + '/id'
        if not os.path.exists(self.archive_id_path):
            os.makedirs(self.archive_id_path)

    
    def return_db_filename(self, item_id):
        return self.archive_db_path + '/' + os.path.basename(item_id)



    def return_id_filename(self, item_id):
        return self.archive_id_path + '/' + os.path.basename(item_id)  + '.id'

    def return_title_xml_filename(self, title_id):
        return self.inbox_path + '/' + 't/t' + title_id + '.xml'
        
    def return_item_xml_filename(self, item_id, archived = False):
        filename = ''
        
        if archived:
            filename = self.archive_xml_path + '/i' + item_id + '.xml'
        else:
            filename = self.inbox_path + '/' + 'i/i' + item_id + '.xml'
    
        return filename

    

                    
