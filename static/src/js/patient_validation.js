

//$(document).ready(function() {
//    // Wait for the document to be ready
//$(document).ready(function () {
//    // Initially, hide all sections
//    $("#studentClassOptions").hide();
//    $("#studentClassOptions11_12").hide();
//    $("#studentclgstream").hide();
//    $("#studentgraduation").hide();
//    $("#studentpostgraduation").hide();
//
//    // Listen for changes in the Admission Type radio buttons
//    $("input[name='remediation_type']").change(function () {
//        var selectedType = $("input[name='remediation_type']:checked").val();
//
//        // Hide all sections
//        $("#studentClassOptions").hide();
//        $("#studentClassOptions11_12").hide();
//        $("#studentclgstream").hide();
//        $("#studentgraduation").hide();
//        $("#studentpostgraduation").hide();
//
//        // Show the relevant section based on the selected Admission Type
//        if (selectedType === "school") {
//            $("#studentClassOptions").show();
//        } else if (selectedType === "jr_college") {
//            $("#studentClassOptions11_12").show();
//            $("#studentclgstream").show();
//        } else if (selectedType === "graduation") {
//            $("#studentclgstream").show();
//            $("#studentgraduation").show();
//        } else if (selectedType === "post_graduation") {
//            $("#studentclgstream").show();
//            $("#studentpostgraduation").show();
//        }
//    });
//});
//
//});





//odoo.define('school_management_web_portal.load_js_function', function (require){
//"Use strict";
//var core = require('web.core');
//var AbstractAction = require('web.AbstractAction');
//var FunctionName = AbstractAction.extend({
//
//$(document).ready(function () {
//        // Function to toggle the visibility of the "Student Class" field
//        function toggleStudentClassField() {
//            var remediationType = $("input[name='remediation_type']:checked").val();
//            if (remediationType === "school") {
//                // Hide the "Student Class" field
//                $("select[name='student_admission_type']").closest('.col-sm-5').hide();
//            } else {
//                // Show the "Student Class" field
//                $("select[name='student_admission_type']").closest('.col-sm-5').show();
//            }
//        }
//
//        // Initial call to set field visibility based on the default selected radio button
//        toggleStudentClassField();
//
//        // Attach an event listener to the radio buttons to update the field visibility when the selection changes
//        $("input[name='remediation_type']").change(function () {
//            toggleStudentClassField();
//        });
//    });
//
//});
//core.action_registry.add('js_function', FunctionName);
//});