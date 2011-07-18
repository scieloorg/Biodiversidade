import urllib.request
import urllib.parse
import urllib.error

class MyAppError(Exception):
    pass


class APIBHL:
    mainurl = "http://www.biodiversitylibrary.org/api2/httpquery.ashx?"


    def __init__(self, key):
        self.access_key = key
        self.title_list_url = self.mainurl + "op=TitleSearchSimple&title=&apikey=" + self.access_key + "&format=<format>"
        self.starturl = self.mainurl + "op=GetSubjectTitles&subject=Brazil&apikey=" + self.access_key + "&format=<format>"
        self.titleurl = self.mainurl + "op=GetTitleMetadata&titleid=<title id>&items=t&apikey=" + self.access_key + "&format=<format>"
        self.pageurl = self.mainurl + "op=GetItemPages&itemid=<item id>&apikey=" + self.access_key + "&format=<format>"
        self.pagemetaurl = self.mainurl + "op=GetPageOcrText&pageid=<page id>&apikey=" + self.access_key + "&format=<format>"


    def query_subject(self, format):
        url = self.starturl.replace('<format>', format)        
        return query(url)

    def query_title_list(self, format):
        url = self.title_list_url.replace('<format>', format)        
        return query(url)

    def query_title(self, format, id):
        url = self.titleurl.replace('<format>', format).replace('<title id>', id)        
        return query(url)

    def query_item_pages(self, format, title_id, item_id):
        url = self.pageurl.replace('<format>', format).replace('<title id>', title_id).replace('<item id>', item_id)       
        return query(url)

    def query_page_ocr(self, format, title_id, item_id, page_id):
        url = self.pagemetaurl.replace('<format>', format).replace('<title id>', title_id).replace('<item id>', item_id).replace('<page id>', page_id)
        return query(url)

    def query_subject_and_save(self, filename, format):
        c = self.query_subject(format)
        save_query_result(filename, c)
        return c

    def query_title_list_and_save(self, filename, format):
        c = self.query_title_list(format)
        save_query_result(filename, c)
        return c

    def query_title_and_save(self, filename, format, id):
        c = self.query_title(format, id)
        save_query_result(filename, c)
        return c

    def query_item_pages_and_save(self, filename, format, title_id, item_id):
        c = self.query_item_pages(format, title_id, item_id)
        save_query_result(filename, c)
        return c

    def query_page_ocr_and_save(self, filename, format, title_id, item_id, page_id):
        c = self.query_page_ocr(format, title_id, item_id, page_id)
        save_query_result(filename, c)
        return c


def query(url):
    print(url)
    return urllib.request.urlopen(url).read()

def save_query_result(file_name, file_content):    
    f = open(file_name, mode='wb')
    f.write(file_content)
    f.close()
