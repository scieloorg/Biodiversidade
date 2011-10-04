from BHL_API import BHL_API
from BHL_XML import BHL_XML

import os

def read_file(filename):
    f = open(filename,'r')
    list = f.readlines()
    f.close()
    return list

def save_file(file_name, file_content, mode='wb'):
    if not file_content=='':
        f = open(file_name, mode)
        f.write(file_content)
        f.close()
def return_balanced_path(path, title_id, item_id):
    dir = '/t'
    if item_id:
        dir = '/i'
    return path + dir + '/' + title_id[0:1]


class BHL_DATA_PROVIDER:

    def __init__(self, xml_path):
        access_key="b64e048b-e947-44c2-b5e3-b9ba4e47fce0"
        self.bhl_api = BHL_API(access_key)
        self.xml_path = xml_path
        

    def get_item_id_list_by_batches(self, start_date, end_date, resumptionToken):
        if resumptionToken:
            xml = self.bhl_api.query_most_recent_resumption(resumptionToken)
        else:
            xml = self.bhl_api.query_most_recent(start_date, end_date)


        r_list = []
        d_list = []
        res = ''
        bhl_xml = BHL_XML('',xml)
        resumption = bhl_xml.get_resumption_token()
        if resumption:
            res = resumption[0]
        print(resumption)
        item_id_list = bhl_xml.get_oai_item_id()
        print(item_id_list)
        date_list = bhl_xml.get_oai_date_list()
        print(date_list)
        r_list += item_id_list
        d_list += date_list


        return [d_list,r_list,res]

    def get_item_id_list(self, start_date, end_date):
        xml = self.bhl_api.query_most_recent(start_date, end_date)
        execute = True
        r_list = []
        d_list = []
        while execute:
            bhl_xml = BHL_XML('',xml)
            resumption = bhl_xml.get_resumption_token()
            print(resumption)
            item_id_list = bhl_xml.get_oai_item_id()
            print(item_id_list)
            date_list = bhl_xml.get_oai_date_list()
            print(date_list)
            r_list += item_id_list
            d_list += date_list
            if resumption:
                xml = self.bhl_api.query_most_recent_resumption(resumption[0])
            else:
                execute = False


        return [d_list,r_list]

    def get_item_metadata(self, item_id):
        xml = self.bhl_api.query_item_metadata(item_id)
        bhl_xml = BHL_XML('', xml)
        
        return bhl_xml.get_items()

    def get_title_metadata(self, title_id):
        fname = self.return_filename(title_id)
        xml = ''
        if os.path.exists(fname):
            #print('exist ' + fname)
            f = open(fname, 'r')
            xml = f.read()
            f.close()

        if not xml:
            xml = self.bhl_api.query_title(title_id,'')
            save_file(fname, xml, 'w')

        bhl_xml = BHL_XML('', xml)
        return bhl_xml.get_title_and_items()
        

    def return_filename(self, title_id, item_id=''):
        """
        Return full path of title or title item XML file
        """
        f = ''
        if not item_id=='':
            f = '_' + item_id
        return  return_balanced_path(self.xml_path, title_id, item_id)+ '/' + title_id + f + '.xml'

