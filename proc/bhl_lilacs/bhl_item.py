from bhl_xml import BHL_XML

class BHL_Item:

    def __init__(self, report):
        self.report = report
        
        
    def download(self, bhl_api, item_id, xml_filename):
        xml = bhl_api.query_item_metadata(item_id)
        f = open(xml_filename, 'w')
        try: 
            
            f.write(xml)
            
        except:
            pass

        f.close()

    def load(self, xml_filename):
        self.bhl_xml = BHL_XML(xml_filename, '', self.report)
        

    def return_title_id(self):
        return self.bhl_xml.get_primary_title_id()
        
                

