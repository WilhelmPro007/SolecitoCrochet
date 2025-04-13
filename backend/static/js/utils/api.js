const api = {
    async get(endpoint) {
        try {
            const response = await fetch(`/api/${endpoint}`)
            if (!response.ok) throw new Error('Network response was not ok')
            return await response.json()
        } catch (error) {
            console.error(`Error fetching ${endpoint}:`, error)
            throw error
        }
    },

    async post(endpoint, data) {
        try {
            const response = await fetch(`/api/${endpoint}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify(data)
            })
            if (!response.ok) throw new Error('Network response was not ok')
            return await response.json()
        } catch (error) {
            console.error(`Error posting to ${endpoint}:`, error)
            throw error
        }
    }
} 