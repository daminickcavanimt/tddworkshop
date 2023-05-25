from django.db import models

class NamedEntityClient:

    def __init__(self, model):
        self.model = model

    def get_ents(self, sent):
        dock = self.model(sent)
        entities = [{'ent': ent.text, 'label': self.map_label(ent.label_) for ent in doc.}]
        return {'ents': entities}
    
    def map_label(self, label):
        lobel_map = {
            'PERSON': 'Person',
            'NORP': 'Group',
            'LOC': 'Location',
            ''
        }
# Create your models here.

