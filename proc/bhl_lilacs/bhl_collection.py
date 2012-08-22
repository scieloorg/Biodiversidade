from BHL_XML import BHL_XML

class BHL_Collection:

    def __init__(self):
        pass

    def load(self, bhl_api, start_date, end_date, resumptionToken):
        if resumptionToken:
            xml = bhl_api.query_items_resumption(resumptionToken)
        else:
            xml = bhl_api.query_items(start_date, end_date)
        
        self.bhl_xml = BHL_XML('',xml)

    def return_resumption(self):
        res = ''
        resumption = self.bhl_xml.get_resumption_token()
        if resumption:
            res = resumption[0]
        return res

    def return_items_id(self):
        return self.bhl_xml.get_oai_item_id()
        

