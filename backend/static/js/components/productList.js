// Definición del componente productList
function productList() {
    return {
        allProducts: [],
        products: [],
        categories: [],
        filters: {
            search: '',
            category: '',
            orderBy: 'name',
            maxPrice: 1000
        },
        loading: false,
        error: null,

        init() {
            // Obtener los datos iniciales del template
            this.allProducts = JSON.parse(document.getElementById('initial-products').textContent);
            this.categories = JSON.parse(document.getElementById('initial-categories').textContent);
            this.applyFilters();
        },

        formatPrice(price) {
            return new Intl.NumberFormat('es-ES', {
                style: 'currency',
                currency: 'EUR'
            }).format(price);
        },

        applyFilters() {
            this.loading = true;
            let filteredProducts = [...this.allProducts];

            // Aplicar filtro de búsqueda
            if (this.filters.search) {
                const searchTerm = this.filters.search.toLowerCase();
                filteredProducts = filteredProducts.filter(product => 
                    product.fields.name.toLowerCase().includes(searchTerm) ||
                    product.fields.description.toLowerCase().includes(searchTerm)
                );
            }

            // Aplicar filtro de categoría
            if (this.filters.category) {
                filteredProducts = filteredProducts.filter(product => 
                    product.fields.category === parseInt(this.filters.category)
                );
            }

            // Aplicar filtro de precio máximo
            if (this.filters.maxPrice) {
                filteredProducts = filteredProducts.filter(product => 
                    product.fields.price <= this.filters.maxPrice
                );
            }

            // Aplicar ordenamiento
            filteredProducts.sort((a, b) => {
                const field = this.filters.orderBy.startsWith('-') ? 
                    this.filters.orderBy.slice(1) : this.filters.orderBy;
                const direction = this.filters.orderBy.startsWith('-') ? -1 : 1;
                
                if (field === 'price') {
                    return direction * (a.fields.price - b.fields.price);
                }
                if (field === 'name') {
                    return direction * a.fields.name.localeCompare(b.fields.name);
                }
                if (field === 'created_at') {
                    return direction * (new Date(a.fields.created_at) - new Date(b.fields.created_at));
                }
                return 0;
            });

            this.products = filteredProducts;
            this.loading = false;
        },

        addToCart(product) {
            if (window.Alpine.store('cart')) {
                window.Alpine.store('cart').addItem(product);
                alert('Producto añadido al carrito');
            } else {
                console.error('El store del carrito no está disponible');
                alert('No se pudo agregar el producto al carrito');
            }
        },

        resetPriceFilter() {
            this.filters.maxPrice = 1000;
            this.applyFilters();
        }
    };
}

// Registrar el componente con Alpine.js
document.addEventListener('alpine:init', () => {
    Alpine.data('productList', productList);
}); 