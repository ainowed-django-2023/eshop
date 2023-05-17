$(document).ready(() => {

    console.log('cart-display.js -> start')
    const user_id = $('#user-id').val();

    $.ajax({
        url: "/orders/ajax_cart_display",
        data: `uid=${user_id}`,
        success: (response) => {
            console.log(response)
            $('#cart-count').text(response.count);
            $('#_count').text(`Products: ${response.count} qn.`)
            $('#_total').text(`Prise: ${response.total} uah`)
        }
    })

})