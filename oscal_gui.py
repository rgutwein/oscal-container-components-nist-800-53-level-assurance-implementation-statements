import datetime
import uuid
import os
from oscalkit import OSCAL_VERSION, OSCAL_PROFILE, OSCAL_COMPONENT, OSCAL_SYSTEMSECURITYPLAN, OSCAL_PARTY, OSCAL_ADDRESS, OSCAL_ROLE, OSCAL_PERSON, OSCAL_PROPERTY, OSCAL_CONTROL, OSCAL_CONTROLIMPLEMENTATION, OSCAL_CONTROLASSESSMENT, OSCAL_CONTROLSELECTOR, OSCAL_CONTROLOBJECTIVE, OSCAL_CONTROLSTATEMENT
import tkinter as tk
from tkinter import filedialog

class OSCALGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("OSCAL Generator")
        
        # Define variables
        self.ssp_title_var = tk.StringVar()
        self.ssp_version_var = tk.StringVar()
        self.export_path_var = tk.StringVar()
        
        # Create GUI elements
        tk.Label(self.master, text="System Security Plan Title").grid(row=0, column=0)
        tk.Entry(self.master, textvariable=self.ssp_title_var).grid(row=0, column=1)
        tk.Label(self.master, text="System Security Plan Version").grid(row=1, column=0)
        tk.Entry(self.master, textvariable=self.ssp_version_var).grid(row=1, column=1)
        tk.Label(self.master, text="Export Path").grid(row=2, column=0)
        tk.Entry(self.master, textvariable=self.export_path_var).grid(row=2, column=1)
        tk.Button(self.master, text="Browse", command=self.browse_export_path).grid(row=2, column=2)
        tk.Button(self.master, text="Generate OSCAL", command=self.generate_oscal).grid(row=3, column=1)
    
    def browse_export_path(self):
        export_path = filedialog.asksaveasfilename(defaultextension=".xml")
        if export_path:
            self.export_path_var.set(export_path)
    
    def generate_oscal(self):
        # Set variables
        ssp_title = self.ssp_title_var.get()
        ssp_uuid = str(uuid.uuid4())
        ssp_date = datetime.date.today().strftime("%Y-%m-%d")
        ssp_version = self.ssp_version_var.get()
        ssp_export_path = self.export_path_var.get()
        
        # Create OSCAL objects
        profile = OSCAL_PROFILE(id=ssp_uuid)
        component = OSCAL_COMPONENT(id=ssp_uuid)
        party = OSCAL_PARTY(id=ssp_uuid, type="organization")
        address = OSCAL_ADDRESS(type="postal", address_lines=["123 Main St", "Suite 100"], city="Anytown", state="CA", postal_code="12345", country="US")
        role = OSCAL_ROLE(id=ssp_uuid, title="System Owner", party_uuid=party.uuid)
        person = OSCAL_PERSON(id=ssp_uuid, type="author", name="John Doe", affiliation="Acme Corp")
        property = OSCAL_PROPERTY(id=ssp_uuid, name="example_property", value="example_value")
        control_selector = OSCAL_CONTROLSELECTOR(id=ssp_uuid, control_idref="AC-1")
        control_objective = OSCAL_CONTROLOBJECTIVE(id=ssp_uuid, description="example objective", control_selector_uuids=[control_selector.uuid])
        control_statement = OSCAL_CONTROLSTATEMENT(id=ssp_uuid, description="example statement", control_selector_uuids=[control_selector.uuid])

