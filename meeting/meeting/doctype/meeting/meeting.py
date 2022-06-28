# Copyright (c) 2022, Gift and contributors
# For license information, please see license.txt

from webbrowser import get
import frappe
from frappe.model.document import Document

class Meeting(Document):
	def validate(self):
		"""Set missing Names"""
		found = []
		for attendee in self.attendees:
			if not attendee.full_name:
				attendee.full_name = get_full_name(attendee.attendee)

			if attendee.attendee in found:
				frappe.throw(("Attendee {0} entered twice").format(attendee.attendee))

			found.append(attendee.attendee)


@frappe.whitelist()
def get_full_name(attendee):
	user = frappe.get_doc("User", attendee)
	
	#concatenates by space if it has value
	return " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))

