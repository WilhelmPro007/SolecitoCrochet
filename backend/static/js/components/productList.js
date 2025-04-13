document.addEventListener('alpine:init', () => {
    Alpine.data('productList', () => ({
        products: [],
        categories: [],
        searchQuery: '',
        selectedCategory: '',
        
        async init() {
            await this.loadProducts()
            await this.loadCategories()
        },
        
        async loadProducts() {
            this.products = await api.get('products/')
        },
        
        async loadCategories() {
            this.categories = await api.get('categories/')
        },
        
        get filteredProducts() {
            return this.products.filter(product => {
                const matchesSearch = product.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                                   product.description.toLowerCase().includes(this.searchQuery.toLowerCase())
                const matchesCategory = !this.selectedCategory || product.category == this.selectedCategory
                return matchesSearch && matchesCategory
            })
        },
        
        addToCart(product) {
            cartStore.addItem(product)
        }
    }))
}) 