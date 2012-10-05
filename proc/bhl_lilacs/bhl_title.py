from bhl_xml import BHL_XML, BHL_XML_FILE

class BHL_Title:

    def __init__(self, report):
    	self.report = report
        
    def download(self, bhl_api, title_id, xml_filename):
        xml = bhl_api.query_title(title_id, '')
        BHL_XML_FILE(self.report).save_xml(xml_filename, xml)

        
    
        
    def load(self, xml_filename):
        self.bhl_xml = BHL_XML(xml_filename, '', self.report)

   