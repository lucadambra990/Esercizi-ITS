from Dottore import *
from Paziente import *

class Fattura(Dottore,Paziente):
    _fatture:int
    _salary:int
    def __init__(self,patient:list[Paziente],doctor:Dottore):
        if doctor.isAValidDoctor():
            self.getFattura(len(patient))
            self._salary=0
        else:
            self.patient=None
            self.doctor=None
            self._fatture=None
            self._salary=None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
    
    def setDoctor(self,dottore:Dottore):
        self.doctor = dottore

    def getDoctor(self):
        return self.doctor
    
    def getSalary(self):
        salario = self._salary = self.doctor.getParcel() * len(self.patient)
        return salario
    
    def getFattura(self):
        return f"I pazienti del dottor {self.doctor} sono {len(self.patient)}"
    
    def addPatient(self,newPatient:Paziente):
        self.patient.append(newPatient)
        self.getSalary()
        self.getFattura()
        print(f"Alla lista del Dottor {self.doctor.getLastName()} è stato aggiunto il paziente {newPatient.getIdCode()}")
        