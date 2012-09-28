from utils.xml_manager import XMLManager

from utils.report import Report
#import chardet

class BHL_XML:
    def __init__(self, xml_filename, xml, report):
        if xml_filename == '':
            if len(xml)>0:
                xml_filename = 'xml'
                f = open(xml_filename, 'w')
                f.write(xml)
                f.close()

        self.xml_manager = XMLManager(xml_filename, report)
        #self.debug = debug
    
    def get_oai_item_id(self):
        item_id_list = self.xml_manager.get_text('identifier')
        print(item_id_list)
        r = []
        for i in item_id_list:
            s = i.split('/')
            try:
                r.append(s[1])
            except:
                r.append('')
        return r
    
    def get_resumption_token(self):
        return self.xml_manager.get_text('resumptionToken', True)
    
    def get_title_id(self):
        return self.xml_manager.get_text("TitleID", True)

    def get_primary_title_id(self):
        return self.xml_manager.get_text('PrimaryTitleID', True)

    def get_item_id(self):
        return self.xml_manager.get_text('ItemID', True)

    def get_identifier(self):
        return self.xml_manager.get_text('identifier', True)

    
    def get_oai_date_list(self):
        return self.xml_manager.get_text('datestamp')
        


    def get_page_list(self):
        return self.xml_manager.get_text('PageID')
    def get_subject_list(self):
        return self.xml_manager.get_text('SubjectText')


