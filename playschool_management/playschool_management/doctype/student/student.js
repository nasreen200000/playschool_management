frappe.ui.form.on('Student', {
    refresh: function(frm) {
        // Add custom logic to be executed when the Student form is loaded or refreshed.
    },
    date_of_birth: function(frm) {
        // Calculate age based on Date of Birth
        if (frm.doc.date_of_birth) {
            var dob = new Date(frm.doc.date_of_birth);
            var today = new Date();
            var age = today.getFullYear() - dob.getFullYear();

            // Check if the birthdate for this year has not occurred yet
            if (today.getMonth() < dob.getMonth() || (today.getMonth() === dob.getMonth() && today.getDate() < dob.getDate())) {
                age--;
            }

            frm.set_value('age', age);
        }
    }
});
