from myXML import MyXML

from title_item import TitleItem
from title_id import TitleId
from author import Author
from TitleAndItems import TitleAndItems
#import chardet

class BHL_XML:

    def __init__(self, xml_filename, xml, debug=False):
        self.xml = MyXML(xml_filename, xml, debug)
        self.debug = debug
    
    def get_title_id(self):
        return self.xml.get_text("TitleID")

    def get_primary_title_id(self):
        return self.xml.get_text('PrimaryTitleID')

    def get_item_id(self):
        return self.xml.get_text('ItemID')

    def get_identifier(self):
        return self.xml.get_text('identifier')

    def get_oai_item_id(self):
        item_id_list = self.xml.get_text('identifier')
        r = []
        for i in item_id_list:
            s = i.split('/')
            try:
                r.append(s[1])
            except:
                r.append('')
        return r

    def get_oai_date_list(self):
        d = self.xml.get_text('datestamp')
        r=[]
        for date in d:
            r.append(date)
        return r

    def get_resumption_token(self):
        return self.xml.get_text('resumptionToken')

    def get_page_list(self):
        return self.xml.get_text('PageID')
    def get_subject_list(self):
        return self.xml.get_text('SubjectText')

    def get_authors(self):
        authors = self.xml.get_nodes('Creator')
        r_authors = []
        #self.debug = True
        for author in authors:
            #print(author)
            #print(type(author))
            a = Author()

            a.set_author_id(self.xml.get_text('CreatorID', author))
            a.set_author_date(self.xml.get_text('Dates', author))
            a.set_author_loc(self.xml.get_text('Location', author))
            a.set_author_name(self.xml.get_text('Name', author))
            a.set_author_num(self.xml.get_text('Numeration', author))
            a.set_author_role(self.xml.get_text('Role', author))
            a.set_author_title(self.xml.get_text('Title', author))
            a.set_author_unit(self.xml.get_text('Unit', author))
            if self.debug:
                print('xxx---------  ')
                print(a.get_author_id())
                print(a.get_author_date())
                print(a.get_author_loc())
                print(a.get_author_name())
                print(a.get_author_num())
                print(a.get_author_role())
                print(a.get_author_title())
                print(a.get_author_unit())
                print('---------  ')
            r_authors.append(a)
        #self.debug = False
        return r_authors

    def get_other_title_id(self):
        items = self.xml.get_nodes('Identifiers/TitleIdentifier')
        r_items = []
        for item in items:
            o = TitleId()
            o.set_name(self.xml.get_text('IdentifierName', item))
            o.set_value(self.xml.get_text('IdentifierValue', item))
            r_items.append( o)
        return r_items

    

    def get_title_and_items(self):
        b = TitleAndItems()
        b.set_title_id(self.xml.get_text('TitleID'))
        b.set_bibliographic_level(self.xml.get_text('BibliographicLevel'))

        ids = self.xml.get_nodes('TitleIdentifier')
        for i in ids:
            name = self.xml.get_text('IdentifierName', i)
            v = self.xml.get_text('IdentifierValue', i)
            if name == 'issn':
                b.set_issn(v)
            else:
                if name == 'isbn':
                    b.set_isbn(v)

        b.set_call_number(self.xml.get_text('CallNumber'))
        b.set_edition(self.xml.get_text('Edition'))
        b.set_full_title(self.xml.get_text('FullTitle'))
        b.set_part_name(self.xml.get_text('PartName'))
        b.set_part_number(self.xml.get_text('PartNumber'))
        b.set_publication_date(self.xml.get_text('PublicationDate'))
        b.set_publication_frequency(self.xml.get_text('PublicationFrequency'))
        b.set_publisher_name(self.xml.get_text('PublisherName'))
        b.set_publisher_place(self.xml.get_text('PublisherPlace'))
        b.set_short_title(self.xml.get_text('ShortTitle'))
        b.set_sort_title(self.xml.get_text('SortTitle'))
        b.set_subject_text(self.xml.get_text('Subjects/Subject/SubjectText'))
        b.set_authors(self.get_authors())
        b.set_title_ids(self.get_other_title_id())

        for ident in self.get_other_title_id():
            if ident.get_name()=='ISSN':
                b.set_issn(ident.get_value())
            if ident.get_name()=='ISBN':
                b.set_isbn(ident.get_value())

        #b.set_items(self.get_items())
        return b

    def get_items(self):
        items = self.xml.get_nodes('Items/Item')
        if not items:
            items = self.xml.get_nodes('Result')
        r_items = []

        for item in items:
            o = TitleItem()
            #self.debug = True
            o.set_contributor_id(self.xml.get_text('Contributor',item))
            o.set_copyright_region(self.xml.get_text('CopyrightRegion',item))
            o.set_copyright_status(self.xml.get_text('CopyrightStatus',item))
            o.set_due_diligence(self.xml.get_text('DueDiligence',item))
            o.set_item_id(self.xml.get_text('ItemID',item))
            o.set_url_item_thumb(self.xml.get_text('ItemThumbUrl',item))
            o.set_url_item(self.xml.get_text('ItemUrl',item))
            o.set_language(self.xml.get_text('Language',item))
            o.set_primary_title_id(self.xml.get_text('PrimaryTitleID',item))
            o.set_rights(self.xml.get_text('Rights',item))
            o.set_source(self.xml.get_text('Source',item))
            o.set_source_id(self.xml.get_text('SourceIdentifier',item))
            o.set_sponsor(self.xml.get_text('Sponsor',item))
            o.set_thumbnail_page_id(self.xml.get_text('ThumbnailPageID',item))
            #t = self.xml.get_nodes('ThumbnailPageID')
            #print('ThumbnailPageID')
            #print(t)
            #x={'x':'1'}
            t = []
            o.set_thumbnai_page_id_att(t)
            o.set_title_url(self.xml.get_text('TitleUrl',item))
            o.set_volume(self.xml.get_text('Volume',item))
            o.set_date_year(self.xml.get_text('Year',item))
            r_items.append(o)
        #print(r_items)    
        return r_items
