import urllib.request
import urllib.parse
import urllib.error

class MyAppError(Exception):
    pass

class BHL_API:
    mainurl = "http://www.biodiversitylibrary.org/api2/httpquery.ashx?"
    oaiurl = "http://www.biodiversitylibrary.org/oai?verb=ListIdentifiers&set=item&metadataPrefix=mods&from=<FROM>&until=<UNTIL>"
    oai_resumption = "http://www.biodiversitylibrary.org/oai?verb=ListIdentifiers&resumptionToken=<resumptionToken>"

    # 2009-03-29

    def __init__(self, key="b64e048b-e947-44c2-b5e3-b9ba4e47fce0"):
        self.access_key = key

    def query(self, op, other_params):
        url = self.mainurl + 'op=' + op + '&apikey=' + self.access_key + '&forma=xml' + other_params
        print(url)
        return str(urllib.request.urlopen(url).read(),'utf-8')

    def query_item_metadata(self, item_id):
        return self.query('GetItemMetadata', '&itemid=' + item_id)
    
    def query_items(self, par_from, par_until):
        url = self.oaiurl.replace('<FROM>',par_from).replace('<UNTIL>',par_until)
        print(url)
        return str(urllib.request.urlopen(url).read(),'utf-8')

    def query_items_resumption(self, resump):
        url = self.oai_resumption.replace('<resumptionToken>',resump)
        print(url)
        return str(urllib.request.urlopen(url).read(),'utf-8')

    def query_title_list_by_subject(self, subj):        
        return self.query('GetSubjectTitles','&subject=' + subj)

    def query_title_list(self):        
        return self.query('TitleSearchSimple')

    def query_title(self, id, t='t'):
        return self.query('GetTitleMetadata', '&titleid=' + id + '&items=' + t)

    def query_item_pages(self, item_id):
        return self.query('GetItemPages', '&itemid=' + item_id)

    def query_page_ocr(self, page_id):
        return self.query('GetPageOcrText', '&pageid=' + page_id)

    



