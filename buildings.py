class Building:
    def __init__(self, nameAbb, lat, long):
        self.nameAbb = nameAbb
        self.lat = lat
        self.long = long
    
    def __str__(self):
        return f"{self.nameAbb}\n{self.lat}\n{self.long}"

sampleBuildings = [
                    Building("ILCB", 30.611989292762015, -96.34449602492593),
                    Building("HELD", 30.61512622178035, -96.33868499747159),
                    Building("HRBB", 30.619038913869666, -96.338787228331),
                    Building("ARCB", 30.619255249600748, -96.3383525289919),
                    Building("BLOC", 30.619478623934423, -96.34213402035815),
                    Building("MSC", 30.612258740025453, -96.34154345301322),
                    Building("MPHY",30.62025, -96.34243),
                    Building("DUNN",30.61519, -96.33694),
                    Building("HEB", 30.61295641575897, -96.31882650766944),
                    Building("EVANS", 30.617024931518685, -96.33894877045664),
                    Building("KYLE", 30.610234849575964, -96.33984326736388),
                    Building("REC", 30.607120558785486, -96.34282904361197),
                    Building("ACAD", 30.61574, -96.34078),
                    Building("REED", 30.60584, -96.34625),
                    Building("SBSA", 30.61720, -96.34373),
                    Building("MOSE", 30.61557, -96.34571),
                    Building("LECH", 30.61617, -96.34388),
                  ]