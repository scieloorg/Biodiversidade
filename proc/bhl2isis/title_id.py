
class TitleId:
    def __init__(self):
        self.fields = {}

    def add(self, name, v):
        if name in self.fields.keys():
            pass
        else:
            self.fields[name] = []
        if v: self.fields[name] = v


    def set_name(self, value):
        self.add('other_db_title_id_name',value)

    def get_name(self):
        return self.fields['other_db_title_id_name']

    def set_value(self, value):
        self.add('other_db_title_id_value',value)

    def get_value(self):
        return self.fields['other_db_title_id_value']

