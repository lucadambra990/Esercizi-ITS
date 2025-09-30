class TaskManager:

    def _init_ (self, tasks: dict[str, dict[str, bool|str]] = {}) -> None:

# il dizionario tasks ha: una chiave che sarebbe il task_id, una description che ritorna una stringa 
# e un boleano che ritorna T o F se è stato completato o no


        self.tasks: dict[str, dict[str, bool|str]] = tasks

        if tasks is None:
            raise ValueError("")  # se tasks è vuoto restituisce un errore 
    
        # andiamo a definire la funzione

    def create_task ( self, task_id: str, description: str) -> dict | str:

        if task_id in self.tasks:
            raise KeyError (" Errore chiave esiste già!")
        
        else:

            self.tasks[task_id] = {" description" : description,
                                   "completato" : False}
            
# un'altro modo per farlo

        #  else:

        #     temp_dict: dict[str,dict[str, bool | str]] = {" description" : description,
        #                            "completato" : False}
        
        #     self.tasks[task_id] = temp_dict
        
        # return temp_dict '''
            
    def complete_task( self, task_id: str) -> dict[str,dict[str, bool | str]] | str: # questa funzione serve a cambiare il valore del complete  in True

        if task_id not in self.tasks:

            return " Chiave non esistente"
        
        else:
            # potremmo impostare un check per vedere il valore di completato, se è T non serve cambiarlo
            if self.tasks[task_id] ["Completato"]:

                return "Il task è già stato completato"
            else:
                self.tasks [task_id] ["completato"] = True
                
                return self.tasks[task_id]
    
    def update_desctiption(self,task_id:str,nuova_descrizione:str)-> dict|str:

        if task_id not in self.tasks:

            return "Il task non è nel dizionario"
        
        else:

            self.tasks[task_id]["description"] = nuova_descrizione

            return self.tasks[task_id]
        
    def remove_task(self,task_id:str)->dict|str:

        if task_id not in self.tasks:
            
            return "Task non presente"
        
        else:

           return self.tasks.pop(task_id)
        
    def list_task(self)->list[str]:
        # metodo con cilo for

        # lista_chiavi : list[str] = []
        # for key in self.tasks.keys():
        #     lista_chiavi.append(key)

        return list[self.tasks.keys()] # metodo più veloce per ritornare la lista delle chiavi del dizionario
    
    def get_task(self,task_id:str)->dict|str:

        if task_id not in self.tasks:

            return "Task non presente"
        
        else:

            return self.tasks[task_id]