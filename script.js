let cart = [];

function addToCart(name, price) {
    cart.push({ name, price });
    alert(`${name} added to cart`);
    updateCart();
}

function updateCart() {
    const cartList = document.getElementById('cart-items');
    const total = document.getElementById('total');

    if (!cartList) return; // If not on cart page

    cartList.innerHTML = '';
    let sum = 0;
    cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - $${item.price}`;
        cartList.appendChild(li);
        sum += item.price;
    });
    total.textContent = `Total: $${sum.toFixed(2)}`;
}

function checkout() {
    if (cart.length === 0) {
        alert("Your cart is empty!");
    } else {
        alert("Thank you for shopping with us!");
        cart = [];
        updateCart();
    }
}

window.onload = updateCart;
