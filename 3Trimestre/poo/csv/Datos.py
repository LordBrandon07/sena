class Datos:
    def __init__(self, index, organizationId, name, website, country, description, founded, industry, numberOfEmployees):
        self.index = index
        self.organizationId = organizationId
        self.name = name
        self.website = website
        self.country = country
        self.description = description
        self.founded = founded
        self.industry = industry
        self.numberOfEmployees = numberOfEmployees
        
    def others(self):
        return self.index +'-'+ self.website
    
    def you(self):
        self.founded
    
        