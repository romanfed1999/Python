from Lawyer import *
from Service import *


class LawFirmManager:
    lawyers_list = []

    def lawyer_search(self, service_type):
        found_lawyers = []
        for lawyer in self.lawyers_list:
            if self.service_type == lawyer.ability:
                found_lawyers.append(self, lawyer)
        return found_lawyers

    @staticmethod
    def lawyers_sort_by_name():
        LawFirmManager.lawyers_list.sort(key=lambda lawyer: lawyer.name, reverse=True)

    @staticmethod
    def print_list(printed_list):
        for lawyer in printed_list:
            print("\n")
            print(lawyer.to_str())

    @staticmethod
    def find_lawyer_by_name(name_to_compare):
        return list(filter(lambda lawyer: lawyer.name == name_to_compare,
                           LawFirmManager.lawyers_list))


law_firm_manager = LawFirmManager()
max = Lawyer("Max", ServiceType.aplication_form_creating)
john = Lawyer("John", ServiceType.contract_creation)
LawFirmManager.lawyers_list.append(max)
LawFirmManager.lawyers_list.append(john)
LawFirmManager.lawyers_sort_by_name()
LawFirmManager.print_list(law_firm_manager.find_lawyer_by_name("Max"))
