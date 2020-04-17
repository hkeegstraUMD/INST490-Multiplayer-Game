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

class Blue(DefaultObject):
           
        def at_object_creation(self):
            "this is called only once, when object is first created"
            # add a persistent attribute 'desc' 
            # to object (silly example).
            self.db.desc = "A glowing blue artifact"
            self.locks.add("get:false()")
            self.db.get_err_msg = "The artifact is too heavy to pick up"

class Green(DefaultObject):
           
        def at_object_creation(self):
            "this is called only once, when object is first created"
            # add a persistent attribute 'desc' 
            # to object (silly example).
            self.db.desc = "A glowing green artifact"
            self.locks.add("get:false()")
            self.db.get_err_msg = "The artifact is too heavy to pick up"

class Yellow(DefaultObject):
           
        def at_object_creation(self):
            "this is called only once, when object is first created"
            # add a persistent attribute 'desc' 
            # to object (silly example).
            self.db.desc = "A glowing yellow artifact"
            self.locks.add("get:false()")
            self.db.get_err_msg = "The artifact is too heavy to pick up"