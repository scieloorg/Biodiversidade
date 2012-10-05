from utils.xml_manager import XMLManager

from utils.report import Report
#import chardet
import tempfile, os

class BHL_XML_FILE:
    def __init__(self, report):
        self.report = report

    def save_xml(self, xml_filename, content):
        if len(content)>0:
            try:
                f = open(xml_filename, 'w')
                f.write(content)
                f.close()
                
            except:
                f = open(xml_filename, 'wb')
                f.write(content)
                f.close()
                
            if os.path.exists(xml_filename):
                if os.path.getsize(xml_filename)==0:
                    self.report.write('BHL_XML_FILE.save_xml: ERROR: missing ' + xml_filename, False, True, False)
                    os.unlink(xml_filename)
        else:
            self.report.write('BHL_XML_FILE.save_xml: ERROR: empty content to ' + xml_filename, False, True, False)
                    
    def read_xml(self, xml_filename):
        xml = ''
        if os.path.exists(xml_filename):
            try:
                f = open(xml_filename, 'r')
                xml = f.read()
                f.close()
            except:
                f = open(xml_filename, 'rb')
                xml = f.read()
                f.close()
            
        else:
            self.report.write('BHL_XML_FILE.read_xml: ERROR: Missing ' + xml_filename, False, True, False)
        return xml 


class BHL_XML:
    def __init__(self, xml_filename, xml, report):
        self.report = report
        if xml_filename == '':
            if len(xml)>0:
                a, xml_filename = tempfile.mkstemp()
                BHL_XML_FILE(report).save_xml(xml_filename, xml)

        if os.path.exists(xml_filename):
            self.xml_manager = XMLManager(xml_filename, report)
        else:
            self.report.write('BHL_XML.init: ERROR: missing ' + xml_filename, False, True, False)
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


