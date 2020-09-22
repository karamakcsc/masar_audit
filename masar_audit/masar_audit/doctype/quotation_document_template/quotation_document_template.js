// Copyright (c) 2020, KCSC and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quotation Document Template', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on("Quotation Document Template Detail", {
    "document_code" : function(frm,cdt,cdn) {
      var ReqDoc = frappe.model.get_doc(cdt,cdn);
      show_alert(ReqDoc.document_code, 5);
      if (ReqDoc.document_code) {
        frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Required Document",
                name: ReqDoc.document_code
            },
            callback: function (data) {
                show_alert(ReqDoc.name, 5);
                frappe.model.set_value(cdt,
                    cdn, "document_description",
                    data.message.document_description)
            }
        })
      }
      else {
        frappe.model.set_value(cdt,cdn,"document_description",null);
      }

    }
});
