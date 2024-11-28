document.getElementById('create-customer-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const customerName = document.getElementById('customer-name').value;
    if (customerName) {
        const customerSelect = document.getElementById('customer-select');
        const newOption = document.createElement('option');
        newOption.value = customerName;
        newOption.textContent = customerName;
        customerSelect.appendChild(newOption);
        document.getElementById('customer-name').value = '';
    }
});
document.getElementById('customer-select').addEventListener('change', function() {
    const selectedCustomer = this.value;
    const orderSection = document.getElementById('order-section');
    if (selectedCustomer) {
        orderSection.style.display = 'block';
    } else {
        orderSection.style.display = 'none';
    }
});

document.getElementById('add-order-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const orderDescription = document.getElementById('order-description').value;
    const orderPrice = parseFloat(document.getElementById('order-price').value);
    if (orderDescription && !isNaN(orderPrice)) {
        const ordersList = document.getElementById('orders');
        const newOrder = document.createElement('li');
        newOrder.textContent = `${orderDescription} - $${orderPrice.toFixed(2)}`;
        ordersList.appendChild(newOrder);

        const totalPriceElement = document.getElementById('total-price');
        const currentTotal = parseFloat(totalPriceElement.textContent);
        const newTotal = currentTotal + orderPrice;
        totalPriceElement.textContent = newTotal.toFixed(2);

        document.getElementById('order-description').value = '';
        document.getElementById('order-price').value = '';
    }
});