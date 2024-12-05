import frappe
import re

def after_install():
    update_field_label()
    brand_name = frappe.get_hooks("brand_name")[0]
    update_onboard_details(brand_name)
    update_system_settings(brand_name)
    update_website_settings(brand_name)

def update_field_label():
	"""Update label of section break in employee doctype"""
	frappe.db.sql("""Update `tabDocField` set label='OneHash' where fieldname='erpnext_user' and parent='Employee'""")

def update_system_settings(brand_name):
	frappe.db.set_value("System Settings", "System Settings", "otp_issuer_name", brand_name)

def update_website_settings(brand_name):
	frappe.db.set_value("Website Settings", "Website Settings", "app_name", brand_name)

def update_onboard_details(brand_name):
	update_onboard_module(brand_name)
	update_onboard_steps(brand_name)

def update_onboard_module(brand_name):
	onboard_module_details = frappe.get_all("Module Onboarding",filters={},fields=["name"])
	for row in onboard_module_details:
		doc = frappe.get_doc("Module Onboarding",row.name)
		doc.title = re.sub("ERPNext", brand_name, doc.title)
		doc.success_message = re.sub("ERPNext", brand_name, doc.success_message)
		doc.documentation_url = ""
		doc.flags.ignore_mandatory = True
		doc.save(ignore_permissions = True)

def update_onboard_steps(brand_name):
	onboard_steps_details = frappe.get_all("Onboarding Step",filters={},fields=["name"])
	for row in onboard_steps_details:
		doc = frappe.get_doc("Onboarding Step",row.name)
		if doc.title:
			doc.title = re.sub("ERPNext", brand_name, doc.title)
		if doc.description:
			doc.description = re.sub("ERPNext", brand_name, doc.description)
		doc.intro_video_url = ""
		doc.flags.ignore_mandatory = True
		doc.save(ignore_permissions = True)