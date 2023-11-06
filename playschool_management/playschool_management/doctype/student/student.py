# Copyright (c) 2023, nasreen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Student(Document):
    def validate(self):
        # Add custom validation logic here
        if not self.full_name:
            self.full_name = f"{self.first_name} {self.last_name or ''}"

    def calculate_age(self):
        if self.date_of_birth:
            dob = self.date_of_birth
            today = frappe.utils.nowdate()
            age = today.year - dob.year

            if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
                age -= 1

            self.age = age
