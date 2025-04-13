const cartStore = {
    items: [],
    
    init() {
        this.items = JSON.parse(localStorage.getItem('cart') || '[]')
        this.updateCartCount()
    },
    
    addItem(product, quantity = 1) {
        const existingItem = this.items.find(item => item.id === product.id)
        
        if (existingItem) {
            existingItem.quantity += quantity
        } else {
            this.items.push({ ...product, quantity })
        }
        
        this.save()
    },
    
    removeItem(productId) {
        this.items = this.items.filter(item => item.id !== productId)
        this.save()
    },
    
    updateQuantity(productId, quantity) {
        const item = this.items.find(item => item.id === productId)
        if (item) {
            item.quantity = quantity
            this.save()
        }
    },
    
    save() {
        localStorage.setItem('cart', JSON.stringify(this.items))
        this.updateCartCount()
    },
    
    updateCartCount() {
        document.dispatchEvent(new CustomEvent('cart-updated', {
            detail: { count: this.items.length }
        }))
    },
    
    getTotal() {
        return this.items.reduce((sum, item) => sum + (item.price * item.quantity), 0)
    },
    
    clear() {
        this.items = []
        this.save()
    }
} 