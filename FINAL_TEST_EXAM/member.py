class Member:
    def __init__(self, id, gender, height, weight):
        self.id = id
        self.gender = gender
        self.height = height
        self.weight = weight


    def calc_BMI(self):
        result = (self.weight) / (self.height * self.height)
        return result
    

    def gen_file_record(self):
        return f"{self.id}|{self.gender}|{self.height}|{self.weight}"