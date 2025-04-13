document.addEventListener('alpine:init', () => {
    Alpine.data('featuredProducts', () => ({
        products: [],
        
        async init() {
            try {
                const response = await api.get('products/?featured=true')
                this.products = response.slice(0, 3)
            } catch (error) {
                console.error('Error loading featured products:', error)
            }
        }
    }))

    Alpine.data('testimonials', () => ({
        testimonials: [
            {
                id: 1,
                name: 'María López',
                avatar: '/static/images/testimonials/avatar-1.jpg',
                comment: 'Los productos son hermosos y de excelente calidad. ¡Superó mis expectativas!'
            },
            {
                id: 2,
                name: 'Juan Pérez',
                avatar: '/static/images/testimonials/avatar-2.jpg',
                comment: 'Compré un regalo para mi madre y quedó encantada. El servicio es excepcional.'
            },
            {
                id: 3,
                name: 'Ana García',
                avatar: '/static/images/testimonials/avatar-3.jpg',
                comment: 'Los detalles en cada pieza son increíbles. Definitivamente volveré a comprar.'
            }
        ]
    }))

    Alpine.data('contactForm', () => ({
        form: {
            name: '',
            email: '',
            message: ''
        },

        async submitForm() {
            try {
                await api.post('contact/', this.form)
                alert('Mensaje enviado correctamente')
                this.form = { name: '', email: '', message: '' }
            } catch (error) {
                console.error('Error sending message:', error)
                alert('Error al enviar el mensaje. Por favor, intenta nuevamente.')
            }
        }
    }))
}) 