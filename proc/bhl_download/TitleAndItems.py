

class TitleAndItems:
    def __init__(self):
        self.fields = {}

    def add(self, name, v):
        if name in self.fields.keys():
            pass
        else:
            self.fields[name] = []
        if v: self.fields[name] = v

    
    def get(self, name, i):
        #print('==>get ' + name)
        #print(self.fields[name])
        if name in self.fields.keys():
            return self.fields[name]
        else:
            return ''

    def set_title_id(self, value):
        self.add('title_id',value)

    def get_title_id(self):        
        return self.get('title_id', 0)

    def set_bibliographic_level(self, value):
        self.add('bibliographic_level',value)

    def get_bibliographic_level(self):
        return self.get('bibliographic_level', 0)

    def set_issn(self, value):
        self.add('issn',value)

    def get_issn(self):
        return self.get('issn', 0)

    def set_isbn(self, value):
        self.add('isbn',value)

    def get_isbn(self):
        return self.get('isbn', 0)

    def set_call_number(self, value):
        self.add('call_number',value)

    def get_call_number(self):
        return self.get('call_number',0)

    def set_edition(self, value):
        self.add('edition',value)

    def get_edition(self):
        return self.get('edition',0)

    def set_full_title(self, value):
        self.add('full_title',value)

    def get_full_title(self):
        return self.get('full_title', 0)

    def set_part_name(self, value):
        self.add('part_name',value)

    def get_part_name(self):
        return self.get('part_name',0)

    def set_part_number(self, value):
        self.add('part_number',value)

    def get_part_number(self):
        return self.get('part_number', 0)

    def set_publication_date(self, value):
        self.add('publication_date',value)

    def get_publication_date(self):
        return self.get('publication_date', 0)

    def set_publication_date_norm(self, value):
        self.add('publication_date_norm',value)

    def get_publication_date_norm(self):
        return self.get('publication_date_norm', 0)

    def set_publication_frequency(self, value):
        self.add('publication_frequency',value)

    def get_publication_frequency(self):
        return self.get('publication_frequency',0)

    def set_publisher_name(self, value):
        self.add('publisher_name',value)

    def get_publisher_name(self):
        return self.get('publisher_name', 0)

    def set_publisher_place(self, value):
        self.add('publisher_place',value)

    def get_publisher_place(self):
        return self.get('publisher_place', 0)

    def set_short_title(self, value):
        self.add('short_title',value)

    def get_short_title(self):
        return self.get('short_title', 0)

    def set_sort_title(self, value):
        self.add('sort_title',value)

    def get_sort_title(self):
        return self.get('sort_title', 0)

    def set_subject_text(self, value):
        self.add('subject_text',value)

    def get_subject_text(self):
        return self.get('subject_text',0)

    def set_authors(self, value):
        self.add('author',value)

    def get_authors(self):
        return self.get('author',0)

    def set_title_ids(self, value):
        self.add('other_db_title_id',value)

    def get_title_ids(self):
        return self.get('other_db_title_id',0)

    def set_items(self, value):
        self.add('item',value)

    def get_items(self):
        return self.get('item',0)

    def set_oai_date(self, value):
        v = []
        v.append(value)
        self.add('oai_date',v)
        
    def get_oai_date(self):
        return self.get('oai_date',0)