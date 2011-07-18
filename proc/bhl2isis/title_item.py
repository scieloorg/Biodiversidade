
class TitleItem:
    def __init__(self):
        self.fields = {}

    def add(self, name, v):
        if name in self.fields.keys():
            pass
        else:
            self.fields[name] = []
        if v: self.fields[name]= v

    def set_contributor_id(self, value):
        self.add('contributor_id',value)

    def get_contributor_id(self):
        return self.fields['contributor_id']

    def set_copyright_region(self, value):
        self.add('copyright_region',value)

    def get_copyright_region(self):
        return self.fields['copyright_region']

    def set_copyright_status(self, value):
        self.add('copyright_status',value)

    def get_copyright_status(self):
        return self.fields['copyright_status']

    def set_due_diligence(self, value):
        self.add('due_diligence',value)

    def get_due_diligence(self):
        return self.fields['due_diligence']

    def set_item_id(self, value):
        self.add('item_id',value)

    def get_item_id(self):
        return self.fields['item_id']

    def set_url_item_thumb(self, value):
        self.add('url_item_thumb',value)

    def get_url_item_thumb(self):
        return self.fields['url_item_thumb']

    def set_url_item(self, value):
        self.add('url_item',value)

    def get_url_item(self):
        return self.fields['url_item']

    def set_language(self, value):
        self.add('language',value)

    def get_language(self):
        return self.fields['language']

    def set_primary_title_id(self, value):
        self.add('primary_title_id',value)

    def get_primary_title_id(self):
        return self.fields['primary_title_id']

    def set_rights(self, value):
        self.add('rights',value)

    def get_rights(self):
        return self.fields['rights']

    def set_source(self, value):
        self.add('source',value)

    def get_source(self):
        return self.fields['source']

    def set_source_id(self, value):
        self.add('source_id',value)

    def get_source_id(self):
        return self.fields['source_id']

    def set_sponsor(self, value):
        self.add('sponsor',value)

    def get_sponsor(self):
        return self.fields['sponsor']

    def set_thumbnail_page_id(self, value):
        self.add('thumbnail_page_id',value)

    def get_thumbnail_page_id(self):
        return self.fields['thumbnail_page_id']

    def set_thumbnai_page_id_att(self, value):
        self.add('thumbnai_page_id_att',value)

    def get_thumbnai_page_id_att(self):
        return self.fields['thumbnai_page_id_att']

    def set_title_url(self, value):
        self.add('title_url',value)

    def get_title_url(self):
        return self.fields['title_url']

    def set_volume(self, value):
        self.add('volume',value)

    def get_volume(self):
        return self.fields['volume']

    def set_date_year(self, value):
        self.add('date_year',value)

    def get_date_year(self):
        return self.fields['date_year']
