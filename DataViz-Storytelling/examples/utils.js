// Utility functions for DataViz-Storytelling exercises

// Parse CSV text to array of objects
function parseCSV(text) {
    const lines = text.trim().split('\n');
    const headers = lines[0].split(',').map(h => h.trim());
    
    return lines.slice(1).map(line => {
        const values = line.split(',').map(v => v.trim());
        const obj = {};
        headers.forEach((header, index) => {
            obj[header] = values[index];
        });
        return obj;
    });
}

// Convert array of objects to CSV text
function arrayToCSV(data) {
    if (!data || data.length === 0) return '';
    
    const headers = Object.keys(data[0]);
    const csvRows = [];
    
    csvRows.push(headers.join(','));
    
    for (const row of data) {
        const values = headers.map(header => {
            const val = row[header];
            return typeof val === 'string' && val.includes(',') ? `"${val}"` : val;
        });
        csvRows.push(values.join(','));
    }
    
    return csvRows.join('\n');
}

// Download data as file
function downloadFile(content, filename, contentType = 'text/plain') {
    const blob = new Blob([content], { type: contentType });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    link.click();
    URL.revokeObjectURL(url);
}

// Save to localStorage
function saveToLocalStorage(key, data) {
    try {
        localStorage.setItem(key, JSON.stringify(data));
        return true;
    } catch (e) {
        console.error('Error saving to localStorage:', e);
        return false;
    }
}

// Load from localStorage
function loadFromLocalStorage(key) {
    try {
        const data = localStorage.getItem(key);
        return data ? JSON.parse(data) : null;
    } catch (e) {
        console.error('Error loading from localStorage:', e);
        return null;
    }
}

// Calculate score from answers
function calculateScore(answers, correctAnswers) {
    let correct = 0;
    const total = Object.keys(correctAnswers).length;
    
    for (const [question, correctAnswer] of Object.entries(correctAnswers)) {
        if (answers[question] === correctAnswer) {
            correct++;
        }
    }
    
    return Math.round((correct / total) * 100);
}

// Format date for display
function formatDate(date = new Date()) {
    return date.toISOString().split('T')[0];
}

// Format time for display
function formatTime(date = new Date()) {
    return date.toLocaleTimeString('es-ES');
}

// Get unique values from array
function getUniqueValues(array, key) {
    return [...new Set(array.map(item => item[key]))];
}

// Group data by key
function groupBy(array, key) {
    return array.reduce((result, item) => {
        (result[item[key]] = result[item[key]] || []).push(item);
        return result;
    }, {});
}

// Aggregate data (sum, avg, count)
function aggregate(array, groupKey, valueKey, operation = 'sum') {
    const grouped = groupBy(array, groupKey);
    const result = {};
    
    for (const [group, items] of Object.entries(grouped)) {
        const values = items.map(item => parseFloat(item[valueKey]) || 0);
        
        switch (operation) {
            case 'sum':
                result[group] = values.reduce((a, b) => a + b, 0);
                break;
            case 'avg':
                result[group] = values.reduce((a, b) => a + b, 0) / values.length;
                break;
            case 'count':
                result[group] = values.length;
                break;
            case 'max':
                result[group] = Math.max(...values);
                break;
            case 'min':
                result[group] = Math.min(...values);
                break;
        }
    }
    
    return result;
}

// Show notification
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 25px;
        background: ${type === 'success' ? '#4CAF50' : type === 'error' ? '#f44336' : '#2196F3'};
        color: white;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        z-index: 10000;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(400px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(400px); opacity: 0; }
    }
`;
document.head.appendChild(style);
