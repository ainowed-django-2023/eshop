$(document).ready(() => {

    console.log('Start del order')

    $('.del-btn').click(event => {
        console.log('del-btn -> click')

        let productId = $(event.target).prev().val();
        console.log(`productId: ${productId}`)

        $.ajax({
            url: '/orders/ajax_order_del',
            data: `productId=${productId}`,
            success: (response) => {
                alert(response.result)
                window.location = '/orders'
            }
        })
    })
})