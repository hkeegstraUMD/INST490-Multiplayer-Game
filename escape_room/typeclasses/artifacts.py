from evennia import DefaultObject

class Red(DefaultObject):
           #@create/drop Red Artifact:artifacts.Red
        def at_object_creation(self):
            "this is called only once, when object is first created"
            # add a persistent attribute 'desc' 
            # to object (silly example).
            self.db.desc = "A glowing red artifact"
            self.locks.add("get:false()")
            self.db.get_err_msg = "The artifact is too heavy to pick up"
            self.db.touchtype = "givecolor"
            self.db.color = "red"

class Blue(DefaultObject):
           
        def at_object_creation(self):
            "this is called only once, when object is first created"
            # add a persistent attribute 'desc' 
            # to object (silly example).
            self.db.desc = "A glowing blue artifact"
            self.locks.add("get:false()")
            self.db.get_err_msg = "The artifact is too heavy to pick up"
            self.db.touchtype = "givecolor"
            self.db.color = "blue"

class Green(DefaultObject):
           
        def at_object_creation(self):
            "this is called only once, when object is first created"
            # add a persistent attribute 'desc' 
            # to object (silly example).
            self.db.desc = "A glowing green artifact"
            self.locks.add("get:false()")
            self.db.get_err_msg = "The artifact is too heavy to pick up"
            self.db.touchtype = "givecolor"
            self.db.color = "green"

class Yellow(DefaultObject):
           
        def at_object_creation(self):
            "this is called only once, when object is first created"
            # add a persistent attribute 'desc' 
            # to object (silly example).
            self.db.desc = "A glowing yellow artifact"
            self.locks.add("get:false()")
            self.db.get_err_msg = "The artifact is too heavy to pick up"
            self.db.touchtype = "givecolor"
            self.db.color = "yellow"

class HintShrine(DefaultObject):

        def at_object_creation(self):
            self.db.desc = "A mysterious statue that seems to depict an important being"
            self.locks.add("get:false()")
            self.db.get_err_msg = "The statue is too heavy to pick up"
            self.db.touchtype = "givehint"
            self.db.hintred = "combine"
            self.db.hintgreen = "all"
            self.db.hintblue = "the"
            self.db.hintyellow = "numbers"

class ClueObject(DefaultObject):

        def at_object_creation(self):
            self.db.desc = "A mural covered in hypnotic patterns"
            self.locks.add("get:false()")
            self.db.get_err_msg = "The mural is too heavy to pick up"
            self.db.touchtype = "giveclue"
            self.db.hintred = "5"
            self.db.hintgreen = "7"
            self.db.hintblue = "2"
            self.db.hintyellow = "4"

class AnswerObject(DefaultObject):

        def at_object_creation(self):
            self.db.desc = "A panel covered in numbered buttons"
            self.locks.add("get:false()")
            self.db.get_err_msg = "The panel is too heavy to pick up"
            self.db.answer = "18"