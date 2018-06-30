from app import ma


class LawyerStructure(ma.Schema):
    class Meta:
        fields = ("id", "name", "lastname")
