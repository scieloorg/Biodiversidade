from BHL_XML import BHL_XML

class BHL_Item:

    def __init__(self):
        pass
        
    def load(self, bhl_api, item_id):
        self.xml = bhl_api.query_item_metadata(item_id)
        self.bhl_xml = BHL_XML('', self.xml)
        #self.item_metadata = self.bhl_xml.get_items()
    
    def load_xml(self, xml_filename):
        self.bhl_xml = BHL_XML(xml_filename, '')

    def return_item_metadata(self):
        return self.bhl_xml.get_items()

    def return_title_id(self):
        r = self.bhl_xml.get_primary_title_id()
        if len(r)>0:
            r = r[0] 
        return r
                

