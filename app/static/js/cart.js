/**
 * iMarket Cart - Shopping cart functionality using localStorage
 */

document.addEventListener('DOMContentLoaded', function() {
    initCart();
    updateCartCount();
});

/**
 * Initialize cart functionality
 */
function initCart() {
    const cartToggles = document.querySelectorAll('.cart-toggle');
    const cartClose = document.getElementById('cartClose');
    const cartOverlay = document.getElementById('cartOverlay');
    const cartSidebar = document.getElementById('cartSidebar');
    
    // Open cart (attach to all toggles)
    if (cartToggles && cartToggles.length) {
        cartToggles.forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                openCart();
            });
        });
    }
    
    // Close cart
    if (cartClose) {
        cartClose.addEventListener('click', closeCart);
    }
    
    if (cartOverlay) {
        cartOverlay.addEventListener('click', closeCart);
    }
    
    // Close with Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeCart();
        }
    });
}

/**
 * Open cart sidebar
 */
function openCart() {
    const cartSidebar = document.getElementById('cartSidebar');
    const cartOverlay = document.getElementById('cartOverlay');
    
    if (cartSidebar) {
        cartSidebar.classList.add('open');
    }
    if (cartOverlay) {
        cartOverlay.classList.add('open');
    }
    
    document.body.style.overflow = 'hidden';
    renderCartItems();
}

/**
 * Close cart sidebar
 */
function closeCart() {
    const cartSidebar = document.getElementById('cartSidebar');
    const cartOverlay = document.getElementById('cartOverlay');
    
    if (cartSidebar) {
        cartSidebar.classList.remove('open');
    }
    if (cartOverlay) {
        cartOverlay.classList.remove('open');
    }
    
    document.body.style.overflow = '';
}

/**
 * Format price as Vietnamese Dong
 * Matches the format_vnd Python template filter
 * @param {number} price - The price in VND
 * @returns {string} Formatted price string like "65.000.000 VND"
 */
function formatVND(price) {
    return parseInt(price).toLocaleString('vi-VN').replace(/,/g, '.') + ' VND';
}

/**
 * Get cart from localStorage with error handling
 * @returns {Array} Cart items array
 */
function getCart() {
    try {
        const storedCart = localStorage.getItem('imarket_cart');
        if (storedCart) {
            return JSON.parse(storedCart);
        }
    } catch (e) {
        console.error('Error reading cart from localStorage:', e);
    }
    return [];
}

/**
 * Save cart to localStorage
 */
function saveCart(cart) {
    localStorage.setItem('imarket_cart', JSON.stringify(cart));
}

/**
 * Update cart count in navbar
 */
function updateCartCount() {
    const cart = getCart();
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    const cartCountElements = document.querySelectorAll('.cart-count');
    
    if (cartCountElements.length) {
        cartCountElements.forEach(function(el) {
            el.textContent = totalItems;
            if (totalItems > 0) {
                el.style.display = 'inline-flex';
            } else {
                el.style.display = 'none';
            }
        });
    }
}

/**
 * Render cart items in sidebar
 */
function renderCartItems() {
    const cart = getCart();
    const cartItemsContainer = document.getElementById('cartItems');
    const cartFooter = document.getElementById('cartFooter');
    const cartTotalElement = document.getElementById('cartTotal');
    
    if (!cartItemsContainer) return;
    
    if (cart.length === 0) {
        cartItemsContainer.innerHTML = `
            <div class="cart-empty">
                <i class="bi bi-bag"></i>
                <p>Giỏ hàng của bạn đang trống</p>
                <a href="/" class="btn btn-dark">Tiếp tục mua sắm</a>
            </div>
        `;
        if (cartFooter) {
            cartFooter.style.display = 'none';
        }
        return;
    }
    
    if (cartFooter) {
        cartFooter.style.display = 'block';
    }
    
    let html = '';
    let total = 0;
    
    cart.forEach((item, index) => {
        const itemTotal = item.price * item.quantity;
        total += itemTotal;
        
        const productUrl = `/${item.type}/${item.id}/`;
        
        html += `
            <div class="cart-item" data-key="${item.key}">
                <div class="cart-item-image">
                    ${item.image ? `<img src="${item.image}" alt="${item.name}">` : '<i class="bi bi-music-note-beamed"></i>'}
                </div>
                <div class="cart-item-details">
                    <a href="${productUrl}" class="cart-item-name">${item.name}</a>
                    <p class="cart-item-price">${formatVND(item.price)}</p>
                    <div class="cart-item-quantity">
                        <button class="qty-btn" onclick="updateItemQuantity('${item.key}', -1)">−</button>
                        <span>${item.quantity}</span>
                        <button class="qty-btn" onclick="updateItemQuantity('${item.key}', 1)">+</button>
                    </div>
                </div>
                <button class="cart-item-remove" onclick="removeFromCart('${item.key}')">
                    <i class="bi bi-trash3"></i>
                </button>
            </div>
        `;
    });
    
    cartItemsContainer.innerHTML = html;
    
    if (cartTotalElement) {
        cartTotalElement.textContent = formatVND(total);
    }
}

/**
 * Update item quantity
 */
function updateItemQuantity(key, change) {
    let cart = getCart();
    const index = cart.findIndex(item => item.key === key);
    
    if (index > -1) {
        cart[index].quantity += change;
        
        if (cart[index].quantity < 1) {
            cart.splice(index, 1);
        }
        
        saveCart(cart);
        updateCartCount();
        renderCartItems();
    }
}

/**
 * Remove item from cart
 */
function removeFromCart(key) {
    let cart = getCart();
    cart = cart.filter(item => item.key !== key);
    saveCart(cart);
    updateCartCount();
    renderCartItems();
}

/**
 * Clear entire cart
 */
function clearCart() {
    localStorage.removeItem('imarket_cart');
    updateCartCount();
    renderCartItems();
}
