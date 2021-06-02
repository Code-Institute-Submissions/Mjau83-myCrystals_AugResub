$(document).ready(function(){
    /* mobile sidenav */
    $('.sidenav').sidenav({edge: "right"});
    /* tootip for buttons */
    $('.tooltipped').tooltip();
    /* dropdown in form */
    $('select').formSelect();

    /* modal for deleting a crystal */
    $('.modal').modal();
    $('.modal-trigger').leanModal();

    /* date used */
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 2,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});
/* shows crystals with info */
var elem = document.querySelector('.collapsible.expandable');
var instance = M.Collapsible.init(elem, {
  accordion: false
});