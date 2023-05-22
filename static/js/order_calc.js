const doCalculate = () => {
    console.log('doCalculate() -> Work')

    let checkedBoxes = $('.check:checked')
    let totalPrice = 0
    let selOrderIds = ""

    for (let box of checkedBoxes) {
        let parentRow = $(box).parent().parent()
        let currentPrice = parseFloat($(parentRow).find('th.price-cell').text())
        let currentCount = parseFloat($(parentRow).find('th.count-cell').find('input').val())
        totalPrice += currentPrice * currentCount
        selOrderIds += $(parentRow).find('th.id-cell').text() + ','
    }
    selOrderIds += totalPrice

    console.log(`totalPrice: ${totalPrice}`)
    console.log(`selOrderIds: ${selOrderIds}`)
    $('#total').text(`${totalPrice.toFixed(2)} uah`)
    $('#bill-btn').attr('href', `/orders/bill/${selOrderIds}`)

    if (totalPrice == 0) {
        $('#bill-btn').fadeOut(1000);
    } else {
        $('#bill-btn').fadeIn(1000);
    }
}

$(document).ready(() => {

    console.log('calc_order.js -> Start!')
    doCalculate()

    $('.check').click((event) => {
        console.log('input.check -> click')
        doCalculate()
    })
})