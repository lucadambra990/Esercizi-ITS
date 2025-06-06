class ContactManager:
    def __init__(self,contacts:dict[str,list[str]]):
        self.contacts=contacts
    
    def create_contact(self,name:str,phone_numbers:list[str])->dict[str,list[str]]:
        new_contact:dict[str,list[str]]={}
        if name in self.contacts:
            raise ValueError("Errore: il contatto è già presente nella rubrica")
        else:
            new_contact[name]=phone_numbers
            return new_contact
        

    def add_phone_number(self,contact_name:str,phone_number:str)->dict:
        update_contact:dict[str,list[str]]={}
        if contact_name not in self.contacts:
            raise ValueError("Errore: Il contatto non esiste!")
        
        if phone_number in self.contacts[contact_name]:
            raise ValueError("Il numero è già associato al contatto!")
        
        self.contacts[contact_name].append(phone_number)
        update_contact[contact_name]=phone_number
        return update_contact
    
    def remove_phone_numbers(self, contact_name:str, phone_number:str)->dict[str,list[str]]:
        delete_contact:dict[str,list[str]]={}
        if contact_name not in self.contacts:
            raise ValueError("Il contatto non esiste")
        if phone_number not in self.contacts[contact_name]:
            raise ValueError("Il numero di telefono non è nella lista")
        
        self.contacts[contact_name].remove(phone_number)
        delete_contact[contact_name]=phone_number
        return delete_contact
    
    def update_phone_number(self,contact_name: str, old_phone_number: str,new_phone_number: str)->dict[str,list[str]]:
        update_number:dict[str,list[str]]={}
        if contact_name not in self.contacts:
            raise ValueError("Il contatto non esiste")
        
        if old_phone_number not in self.contacts:
            raise ValueError("Il nuimero di telefono non è nella lista")
        
        index:int=self.contacts[contact_name].index(old_phone_number)
        self.contacts[contact_name][index] = new_phone_number
        update_number[contact_name]=new_phone_number
        return update_number
    
    def lista_contact(self)->list[str]:
        return list(self.contacts.keys())
    
    def list_phone_numbers(self,contact_name: str)->list[str]:
        if contact_name not in self.contacts:
            raise ValueError("Il contatto non esiste!")
        
        return self.contacts[contact_name]
    
    def search_contact_by_phone_number(self,phone_number: str)->list[str]:
        contacts_list:list[str]=[]
        for contacts, list_contacts in self.contacts.items():
            
            if phone_number in list_contacts:
                contacts_list.append(contacts)

        if not contacts_list:
            
            raise Exception("Nessun contatto trovato con questo numero di telefono")

        return contacts_list
