document.getElementById('customer-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('customer-name').value;
    const email = document.getElementById('customer-email').value;
    
    // Send data to the server (you'll need to implement this)
    console.log(`Adding Customer: ${name}, Email: ${email}`);
});

document.getElementById('order-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const customerId = document.getElementById('customer-select').value;
    const totalAmount = document.getElementById('order-total').value;
    
    // Send data to the server (you'll need to implement this)
    console.log(`Placing Order for Customer ID: ${customerId}, Total Amount: ${totalAmount}`);
});