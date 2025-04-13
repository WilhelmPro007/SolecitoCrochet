const formatters = {
    price: (amount) => {
        return `S/. ${parseFloat(amount).toFixed(2)}`
    },
    
    date: (dateString) => {
        return new Date(dateString).toLocaleDateString('es-PE')
    }
} 