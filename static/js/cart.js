$(document).ready(() => {

    console.log('cart.js -> Start')

    $('#catalog').on('click', '.add-to-cart-btn', (event) => {
         console.log('add-btn -> Click')
         const userId = $('#user-id').val();
         console.log('User-ID: ' + userId)

         if (userId == 'None') {
             alert('For using cart you should be authorized!!!')
         } else {
            let productId = $(event.target).prev().val()
            console.log('Product-ID: ' + productId)

            $.ajax({
                url: '/orders/ajax_cart',
                data: `uid=${userId}&pid=${productId}`,
                success: (response) => {
                    console.log(response);
                    $('#cart-count').text(response.count);
                    $('#_count').text(`Products: ${response.count} qn.`)
                    $('#_total').text(`Prise: ${response.total} uah`)
                }
            });
         }
    });
});