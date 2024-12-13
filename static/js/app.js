$(document).ready(function() {
    $('#dueDateFilter').on('change', function() {
        const dueDate = $(this).val();
        const taxRate = $('#taxRate').val();

        $.ajax({
            url: `/filter_summary?due_date=${dueDate}&tax_rate=${taxRate}`,
            method: 'GET',
            success: function(data) {
                $('#summaryTable').html(`
                    <h5>Total Amount: $${data.total_amount.toFixed(2)}</h5>
                    <h5>Tax Due: $${data.tax_due.toFixed(2)}</h5>
                `);
            }
        });
    });
});
