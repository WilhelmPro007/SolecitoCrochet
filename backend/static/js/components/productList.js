document.addEventListener('alpine:init', () => {
    Alpine.data('productList', () => ({
        products: [],
        categories: [],
        searchQuery: '',
        selectedCategory: '',
        sortBy: 'name_asc',
        priceRange: {
            min: null,
            max: null
        },
        stockFilter: 'all',
        currentPage: 1,
        itemsPerPage: 9,
        
        async init() {
            await this.loadProducts()
            await this.loadCategories()
        },
        
        async loadProducts() {
            try {
                const response = await fetch('/api/v1/products/')
                if (!response.ok) throw new Error('Error cargando productos')
                this.products = await response.json()
            } catch (error) {
                console.error('Error:', error)
                this.products = []
            }
        },
        
        async loadCategories() {
            try {
                const response = await fetch('/api/v1/categories/')
                if (!response.ok) throw new Error('Error cargando categorías')
                this.categories = await response.json()
            } catch (error) {
                console.error('Error:', error)
                this.categories = []
            }
        },
        
        get filteredAndSortedProducts() {
            let filtered = this.products.filter(product => {
                // Filtro de búsqueda
                const matchesSearch = product.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                                   product.description.toLowerCase().includes(this.searchQuery.toLowerCase())
                
                // Filtro de categoría
                const matchesCategory = !this.selectedCategory || 
                                     product.category == this.selectedCategory
                
                // Filtro de precio
                const matchesPrice = (!this.priceRange.min || product.price >= this.priceRange.min) &&
                                   (!this.priceRange.max || product.price <= this.priceRange.max)
                
                // Filtro de stock
                const matchesStock = this.stockFilter === 'all' ||
                                   (this.stockFilter === 'in_stock' && product.stock > 0) ||
                                   (this.stockFilter === 'out_of_stock' && product.stock === 0)
                
                return matchesSearch && matchesCategory && matchesPrice && matchesStock
            })

            // Ordenamiento
            filtered.sort((a, b) => {
                switch(this.sortBy) {
                    case 'name_asc':
                        return a.name.localeCompare(b.name)
                    case 'name_desc':
                        return b.name.localeCompare(a.name)
                    case 'price_asc':
                        return a.price - b.price
                    case 'price_desc':
                        return b.price - a.price
                    case 'newest':
                        return new Date(b.created_at) - new Date(a.created_at)
                    default:
                        return 0
                }
            })

            return filtered
        },

        get paginatedProducts() {
            const start = (this.currentPage - 1) * this.itemsPerPage
            const end = start + this.itemsPerPage
            return this.filteredAndSortedProducts.slice(start, end)
        },

        get totalPages() {
            return Math.ceil(this.filteredAndSortedProducts.length / this.itemsPerPage)
        },

        nextPage() {
            if (this.currentPage < this.totalPages) {
                this.currentPage++
            }
        },

        previousPage() {
            if (this.currentPage > 1) {
                this.currentPage--
            }
        },

        goToPage(page) {
            if (page >= 1 && page <= this.totalPages) {
                this.currentPage = page
            }
        },
        
        addToCart(product) {
            cartStore.addItem(product)
            // Mostrar notificación de éxito
            this.$dispatch('notify', {
                message: 'Producto agregado al carrito',
                type: 'success'
            })
        }
    }))
}) 