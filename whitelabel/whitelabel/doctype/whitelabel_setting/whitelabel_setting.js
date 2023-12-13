// Copyright (c) 2021, Abhishek chougule and contributors
// For license information, please see license.txt

frappe.ui.form.on('Whitelabel Setting', {
	after_save: function(frm) {
		frappe.ui.toolbar.clear_cache();
	}
});
