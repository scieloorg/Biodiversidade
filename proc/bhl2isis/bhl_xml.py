from lxml import etree
from title_item import TitleItem
from title_id import TitleId
from author import Author
from doc import Doc
#import chardet

class APIBHLXML:
    tree = {}
    def __init__(self, xml_file):
        self.tree = etree.parse(xml_file)

    def get_titleid_list(self):
        return self.tree.xpath("//TitleID/text()")

    def get_itemid_list(self):
        return self.tree.xpath("//ItemID/text()")

    def get_page_list(self):
        return self.tree.xpath("//PageID/text()")

    def get_authors(self):
        authors = self.tree.xpath("//Creator")
        r_authors = []
        i=0
        for author in authors:
            i =+ 1
            #print(author)
            #print(type(author))
            a = Author()
            str_i = str(i)
            #print(self.tree.xpath('//Creator[" + str_i + "]/Name/text()'))
            a.set_author_id(self.tree.xpath("//Authors/Creator[" + str_i + "]/CreatorID/text()"))
            a.set_author_date(self.tree.xpath("//Authors/Creator[" + str_i + "]/Dates/text()"))
            a.set_author_loc(self.tree.xpath("//Authors/Creator[" + str_i + "]/Location/text()"))
            a.set_author_name(self.tree.xpath("//Authors/Creator[" + str_i + "]/Name/text()"))
            a.set_author_num(self.tree.xpath("//Authors/Creator[" + str_i + "]/Numeration/text()"))
            a.set_author_role(self.tree.xpath("//Authors/Creator[" + str_i + "]/Role/text()"))
            a.set_author_title(self.tree.xpath("//Authors/Creator[" + str_i + "]/Title/text()"))
            a.set_author_unit(self.tree.xpath("//Authors/Creator[" + str_i + "]/Unit/text()"))
            #print(a.get_author_id())
            #print(a.get_author_date())
            #print(a.get_author_name())
            r_authors.append(a)
        return r_authors

    def get_other_title_id(self):
        items = self.tree.xpath("//Identifiers/TitleIdentifier")
        r_items = []
        i = 0
        for item in items:
            i += 1
            str_i = str(i)
            o = TitleId()
            o.set_name(self.tree.xpath("//Identifiers/TitleIdentifier[" + str_i + "]/IdentifierName/text()"))
            o.set_value(self.tree.xpath("//Identifiers/TitleIdentifier[" + str_i + "]/IdentifierValue/text()"))
            r_items.append( o)
        return r_items

    def get_items(self):
        items = self.tree.xpath("//Items/Item")
        r_items = []
        i = 0
        for item in items:
            i += 1
            str_i = str(i)
            o = TitleItem()
            o.set_contributor_id(self.tree.xpath("//Items/Item[" + str_i + "]/Contributor/text()"))
            o.set_copyright_region(self.tree.xpath("//Items/Item[" + str_i + "]/CopyrightRegion/text()"))
            o.set_copyright_status(self.tree.xpath("//Items/Item[" + str_i + "]/CopyrightStatus/text()"))
            o.set_due_diligence(self.tree.xpath("//Items/Item[" + str_i + "]/DueDiligence/text()"))
            o.set_item_id(self.tree.xpath("//Items/Item[" + str_i + "]/ItemID/text()"))
            o.set_url_item_thumb(self.tree.xpath("//Items/Item[" + str_i + "]/ItemThumbUrl/text()"))
            o.set_url_item(self.tree.xpath("//Items/Item[" + str_i + "]/ItemUrl/text()"))
            o.set_language(self.tree.xpath("//Items/Item[" + str_i + "]/Language/text()"))
            o.set_primary_title_id(self.tree.xpath("//Items/Item[" + str_i + "]/PrimaryTitleID/text()"))
            o.set_rights(self.tree.xpath("//Items/Item[" + str_i + "]/Rights/text()"))
            o.set_source(self.tree.xpath("//Items/Item[" + str_i + "]/Source/text()"))
            o.set_source_id(self.tree.xpath("//Items/Item[" + str_i + "]/SourceIdentifier/text()"))
            o.set_sponsor(self.tree.xpath("//Items/Item[" + str_i + "]/Sponsor/text()"))
            o.set_thumbnail_page_id(self.tree.xpath("//Items/Item[" + str_i + "]/ThumbnailPageID/text()"))
            o.set_thumbnai_page_id_att(self.tree.xpath("//Items/Item[" + str_i + "]/ThumbnailPageID/@*/text()"))
            o.set_title_url(self.tree.xpath("//Items/Item[" + str_i + "]/TitleUrl/text()"))
            o.set_volume(self.tree.xpath("//Items/Item[" + str_i + "]/Volume/text()"))
            o.set_date_year(self.tree.xpath("//Items/Item[" + str_i + "]/Year/text()"))
            r_items.append(o)
        return r_items

    def get_title_data(self):
        b = Doc()
        b.set_title_id(self.tree.xpath("//TitleID/text()"))
        b.set_bibliographic_level(self.tree.xpath("//BibliographicLevel/text()"))
        b.set_issn(self.tree.xpath("//TitleIdentifier[IdentifierName='issn']/text()"))
        b.set_isbn(self.tree.xpath("//TitleIdentifier[IdentifierName='isbn']/text()"))
        b.set_call_number(self.tree.xpath("//CallNumber/text()"))
        b.set_edition(self.tree.xpath("//Edition/text()"))
        b.set_full_title(self.tree.xpath("//FullTitle/text()"))
        b.set_part_name(self.tree.xpath("//PartName/text()"))
        b.set_part_number(self.tree.xpath("//PartNumber/text()"))
        b.set_publication_date(self.tree.xpath("//PublicationDate/text()"))
        b.set_publication_frequency(self.tree.xpath("//PublicationFrequency/text()"))
        b.set_publisher_name(self.tree.xpath("//PublisherName/text()"))
        b.set_publisher_place(self.tree.xpath("//PublisherPlace/text()"))
        b.set_short_title(self.tree.xpath("//ShortTitle/text()"))
        b.set_sort_title(self.tree.xpath("//SortTitle/text()"))
        b.set_subject_text(self.tree.xpath("//Subjects/Subject/SubjectText/text()"))
        b.set_authors(self.get_authors())
        b.set_title_ids(self.get_other_title_id())
        b.set_items(self.get_items())
        return b
