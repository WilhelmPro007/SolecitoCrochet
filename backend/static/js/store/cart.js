document.addEventListener('alpine:init', () => {
    Alpine.store('cart', {
        items: [],
        
        init() {
            const savedCart = localStorage.getItem('cart');
            if (savedCart) {
                this.items = JSON.parse(savedCart);
            }
        },
        
        addItem(product, quantity = 1) {
            const existingItem = this.items.find(item => item.id === product.id);
            
            if (existingItem) {
                existingItem.quantity += quantity;
            } else {
                this.items.push({
                    id: product.id,
                    name: product.name,
                    price: product.price,
                    quantity: quantity,
                    image: product.image
                });
            }
            
            this.saveCart();
        },
        
        removeItem(productId) {
            this.items = this.items.filter(item => item.id !== productId);
            this.saveCart();
        },
        
        updateQuantity(productId, quantity) {
            const item = this.items.find(item => item.id === productId);
            if (item) {
                item.quantity = quantity;
                this.saveCart();
            }
        },
        
        clearCart() {
            this.items = [];
            this.saveCart();
        },
        
        getTotal() {
            return this.items.reduce((total, item) => total + (item.price * item.quantity), 0);
        },
        
        getItemCount() {
            return this.items.reduce((count, item) => count + item.quantity, 0);
        },
        
        saveCart() {
            localStorage.setItem('cart', JSON.stringify(this.items));
        }
    });
}); 