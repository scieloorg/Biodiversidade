from bhl_xml import BHL_XML

class BHL_Collection:

    def __init__(self, report):
        self.report =report 

    def load(self, bhl_api, start_date, end_date, resumptionToken):
        if resumptionToken:
            xml = bhl_api.query_items_resumption(resumptionToken)
        else:
            xml = bhl_api.query_items(start_date, end_date)
        
        self.bhl_xml = BHL_XML('', xml, self.report)

    def return_resumption(self):
        
        return self.bhl_xml.get_resumption_token()
        

    def return_items_id(self):
        return self.bhl_xml.get_oai_item_id()
        

