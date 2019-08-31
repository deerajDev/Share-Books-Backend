def branchChoices():
    branches = [
        ('Mechancial','Mechancial'),
        ('Computer Science','Computer Science'),
        ('Information science','Information science'),
        ('Electrical','Electrical'),
        ('Civil','Civil'),
        ('Biotechnology','Biotechnology'),
        ('Chemical','Chemical'),
        ('Electronics and Communication','Electronics and Communication'),
        ('Industrial and Management','Industrial and Management'),
        ('Medical Electronics','Medical Electronics'),
    ]

    return branches


def yearChoice():
    semester =[
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),


    ]
    return semester


def imageUpload(instance, filename):
    branch = instance.branch
    semester = instance.semester
    return f'{branch}/{semester}/{instance.id}_{filename}'