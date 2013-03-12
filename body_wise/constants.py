# Maybe consider making these in a separate file?
#from records.models import WeightMeasurement

LIFTS = [
    ('BP', 'Bench Press'),
    ('DL', 'Dead Lift'),
    ('BSq', 'Back Squat'),
    ('PlU', 'Pull Up'),
    ('PsU', 'Push Up'),
    ('BJ', 'Box Jump'),
    ('KbS', 'Kettlebell Swing'),
    ('PwCl', 'Power Clean'),
    ('HCl', 'Hang Clean'),
    ('Cl', 'Clean') 
]

PARTS = [
    ('RBc', 'Right Bicept'),
    ('LBc', 'Left Bicept'),
    ('C', 'Chest'),
    ('H', 'Hips'),
    ('Wa', 'Waist'),
    ('RTh', 'Right Thigh'),
    ('LTh', 'Left Thigh'),
    ('Nk', 'Neck'),
    ('FrA', 'Forearms'),
    ('RCv', 'Right Calf'),
    ('LCv', 'Left Calf') 
]

SUBRECORDS = [
    ('', None),
    ('Weight', records.models.WeightMeasurement),
    ('Body Fat', BodyFatMeasurement),
    ('Body Size', BodySizeMeasurement),
    ('Max Lift', MaxLiftMeasurement),
    ('Resting Heart Rate', RestingHRMeasurement),
    ('Mug Shot', MugShotMeasurement),
    ('Sleep', SleepMeasurement),
]
