document.addEventListener('alpine:init', () => {
    Alpine.data('cart', () => ({
        items: [],
        
        init() {
            this.items = JSON.parse(localStorage.getItem('cart') || '[]')
        },
        
        get total() {
            return this.items.reduce((sum, item) => sum + (item.price * item.quantity), 0)
        },
        
        updateQuantity(item, change) {
            const newQuantity = item.quantity + change
            if (newQuantity > 0) {
                cartStore.updateQuantity(item.id, newQuantity)
                item.quantity = newQuantity
            } else {
                this.removeItem(item)
            }
        },
        
        removeItem(item) {
            cartStore.removeItem(item.id)
            this.items = this.items.filter(i => i.id !== item.id)
        },
        
        formatPrice(price) {
            return `S/. ${parseFloat(price).toFixed(2)}`
        },
        
        proceedToCheckout() {
            window.location.href = '/orders/checkout/'
        }
    }))
}) 