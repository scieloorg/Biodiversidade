# -*- coding: utf-8 -*-

import sys
import os


class BHL_Files_Set:

    def __init__(self, xml_path, id_path, mst_path):
        self.xml_path = xml_path
        if not os.path.exists(xml_path):
            os.makedirs(xml_path)

        self.item_path = xml_path + '/i' 
        self.title_path = xml_path + '/t' 
        
        self.id_path = id_path
        if not os.path.exists(id_path):
            os.makedirs(id_path)

        self.mst_path = mst_path
        if not os.path.exists(mst_path):
            os.makedirs(mst_path)

    def return_item_id(self, xml):
        xml = os.path.basename(xml)
        if xml.endswith('.xml'):
            xml = xml.replace('.xml', '')
            if xml.startswith('i'):
                xml = xml[1:]
        return xml
    def return_mst_filename(self, item_id):
        return self.mst_path + '/' + self.return_item_id(item_id)


    def return_id_filename(self, item_id):
        return self.id_path + '/' + self.return_item_id(item_id)  + '.id'

    def return_xml_filename(self, title_id, item_id = ''):
        filename = ''
        if item_id != '':
            filename = 'i/i' + item_id + '.xml'
        elif title_id != '':
            filename = 't/t' + title_id + '.xml'
        
        if len(filename) > 0:
            filename = self.xml_path + '/' + filename 
        
        return filename

    

                    
