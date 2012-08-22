from BHL_XML import BHL_XML

class BHL_Title:

    def __init__(self):
        pass
        
    def load(self, bhl_api, title_id):
        self.xml = bhl_api.query_title(title_id, '')
        self.bhl_xml = BHL_XML('', self.xml)

    def load_xml(self, xml_filename):
        self.bhl_xml = BHL_XML(xml_filename, '')

    def return_metadata(self):
        return self.bhl_xml.get_title_and_items()
    
