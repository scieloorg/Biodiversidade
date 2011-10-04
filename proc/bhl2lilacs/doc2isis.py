

class Doc2ISIS:
    
    def __init__(self):
        pass

    def generate_records(self, doc):
        r = []
        fonte = ['FONTE']
        for item in doc.get_items():
            field = ''
            v5 = doc.get_bibliographic_level()
            if 'Serial' in v5:
                
                f5 = ['S']
                f6 = ['ms']
                tag_full_title = '030'
                tag_volume = '31'
                
            else:
                if 'Monograph/Item' in v5:
                    f5 = ['M']
                    f6 = ['m']
                    tag_full_title = '018'
                    tag_volume = '21'
                else:
                    f5 = ['M']
                    f6 = ['m']
                    tag_full_title = '018'
                    tag_volume = '21'
            field = field + self.get_field('900',doc.get_title_id() , '^xTitleID')
            field = field + self.get_field('3',doc.get_call_number())
            field = field + self.get_field(tag_full_title,doc.get_full_title())
            field = field + self.get_field('62',doc.get_publisher_name())
            field = field + self.get_field('63',doc.get_edition())
            field = field + self.get_field('64',doc.get_publication_date())
            field = field + self.get_field('67',doc.get_publisher_place())
            field = field + self.get_field('340',doc.get_publication_frequency())
            field = field + self.get_field('930',doc.get_short_title() , '^xShortTitle')
            field = field + self.get_field('931',doc.get_sort_title() , '^xSortTitle')
            field = field + self.get_field('943',doc.get_part_name() , '^xPartName')
            field = field + self.get_field('944',doc.get_part_number() , '^xPartNumber')

            field = field + self.get_field('005',f5)
            field = field + self.get_field('006',f6)
            field = field + self.get_field('098',fonte)

            s = doc.get_subject_text()
            
            field = field + self.get_field('085',s)
            field = field + self.get_field('990',s, '^xSubjects/Subject/SubjectText')

            field = field + self.get_field('35',doc.get_issn())
            field = field + self.get_field('69',doc.get_isbn())
            ids = doc.get_title_ids()
            for id in ids:
                f = ''
                f = f + self.get_subf(id.get_name(), 'd')
                f = f + self.get_subf(id.get_value(), 'i')
                s = [f]
                field = field + self.get_field('993',s)
                field = field + self.get_field('990',s,'^xtitle_id')

            authors = doc.get_authors()
            for a in authors:
                f = ''
                f = f + self.get_subf(a.get_author_id(), 'i')
                f = f + self.get_subf(a.get_author_date(), 'd')
                f = f + self.get_subf(a.get_author_loc(), 'c')
                f = f + self.get_subf(a.get_author_name(), 'n')
                f = f + self.get_subf(a.get_author_num(), '1')
                f = f + self.get_subf(a.get_author_role(), 'r')
                f = f + self.get_subf(a.get_author_title(), 't')
                f = f + self.get_subf(a.get_author_unit(), 'u')
                s = [f]
                field = field + self.get_field('992',s)
                field = field + self.get_field('990',s , '^xAuthors/Creator')

            field = field + self.get_field('901',item.get_item_id() , '^xItems/Item/ItemID')
            field = field + self.get_field(tag_volume,item.get_volume())
            field = field + self.get_field('40',item.get_language())
            field = field + self.get_field('940',item.get_language() , '^xItems/Item/Language')
            field = field + self.get_field('65',item.get_date_year())
            field = field + self.get_field('8',item.get_url_item())
            field = field + self.get_field('8',item.get_url_item_thumb())
            field = field + self.get_field('8',item.get_title_url())
            field = field + self.get_field('950',item.get_contributor_id() , '^xItems/Item/Contributor')
            field = field + self.get_field('967',item.get_copyright_region() , '^xItems/Item/CopyrightRegion')
            field = field + self.get_field('966',item.get_copyright_status() , '^xItems/Item/CopyrightStatus')
            field = field + self.get_field('969',item.get_due_diligence() , '^xItems/Item/DueDiligence')
            field = field + self.get_field('910',item.get_primary_title_id() , '^xItems/Item/PrimaryTitleID')
            field = field + self.get_field('968',item.get_rights() , '^xItems/Item/Rights')
            field = field + self.get_field('994',item.get_source() , '^xItems/Item/Source')
            field = field + self.get_field('995',item.get_source_id() , '^xItems/Item/SourceIdentifier')
            field = field + self.get_field('951',item.get_sponsor() , '^xItems/Item/Sponsor')
            field = field + self.get_field('970',item.get_thumbnail_page_id() , '^xItems/Item/ThumbnailPageID')
            field = field + self.get_field('971',item.get_thumbnai_page_id_att() , '^xItems/Item/ThumbnailPageID/@*')

            field = field + self.get_field('990',doc.get_bibliographic_level() , '^xBibliographicLevel')
            field = field + self.get_field('990',doc.get_call_number() , '^xCallNumber')
            field = field + self.get_field('990',doc.get_full_title() , '^xFullTitle')
            field = field + self.get_field('990',doc.get_publisher_name() , '^xPublisherName')
            field = field + self.get_field('990',doc.get_edition() , '^xEdition')
            field = field + self.get_field('990',doc.get_publication_date() , '^xPublicationDate')
            field = field + self.get_field('990',doc.get_publisher_place() , '^xPublisherPlace')
            field = field + self.get_field('990',doc.get_publication_frequency() , '^xPublicationFrequency')
            field = field + self.get_field('990',doc.get_issn() , '^xTitleIdentifier[IdentifierName=issn]')
            field = field + self.get_field('990',doc.get_isbn() , '^xTitleIdentifier[IdentifierName=isbn]')
            field = field + self.get_field('990',item.get_volume() , '^xItems/Item/Volume')
            field = field + self.get_field('990',item.get_date_year() , '^xItems/Item/Year')
            field = field + self.get_field('990',item.get_url_item_thumb() , '^xItems/Item/ItemThumbUrl')
            field = field + self.get_field('990',item.get_url_item() , '^xItems/Item/ItemUrl')
            field = field + self.get_field('990',item.get_title_url() , '^xItems/Item/TitleUrl')
            field = field + self.get_field('965',doc.get_oai_date())
            r.append(field)
        #print(r)
        return r
    def get_field(self, tag, values, extra=''):
        r= ''
        tag = '000' + tag
        tag = tag[-3:]
        for occ in values:
            if len(occ)>0:
                r += '!v' + tag + '!' + occ + extra + "\n"
        return r
    def get_subf(self, value, subf):
        r=''
        if value:
            r = '^' + subf + value[0]
        return r
    