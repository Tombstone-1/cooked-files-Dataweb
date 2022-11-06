$(document).ready(function() {
    $('#datatable').DataTable( {
        "iDisplayLength": 5,
        dom: 'Bfrtip',
        buttons: [
            'copyHtml5',
            'excelHtml5',
            'csvHtml5',
            'pdfHtml5'
        ],
    } );
} );
 s