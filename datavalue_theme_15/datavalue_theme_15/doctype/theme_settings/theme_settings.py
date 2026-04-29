# Copyright (c) 2021, Abdo Hamoud and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ThemeSettings(Document):
	pass




@frappe.whitelist(allow_guest=True)
def get_theme_settings():
    doc = frappe.get_single("Theme Settings")
    return {
        "card_image": doc.card_image,
        "powered_by": doc.powered_by,
        "link": doc.link,
        "login_desc": doc.login_desc,
        "login_head": doc.login_head
    }