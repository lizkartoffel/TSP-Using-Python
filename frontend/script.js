let CurrentCities = [];

document.getElementById('load-cities-btn').addEventListener('click', async () => {
    try { 
        const response = await fetch('/api/cities');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        // Moved inside the try block!
        const data = await response.json();
        
        // Safeguard: If backend returns { cities: [...] }, use data.cities. 
        // If it just returns [...], use data directly.
        CurrentCities = data.cities || data;

        const canvas = document.getElementById('tsp-canvas');
        const minLat = Math.min(...CurrentCities.map(c => c.lat));
        const maxLat = Math.max(...CurrentCities.map(c => c.lat));
        const minLon = Math.min(...CurrentCities.map(c => c.lon));
        const maxLon = Math.max(...CurrentCities.map(c => c.lon));
        
        CurrentCities = CurrentCities.map(city => ({
            ...city,
            x: ((city.lon - minLon) / (maxLon - minLon)) * (canvas.width - 20) + 10,
            y: ((maxLat - city.lat) / (maxLat - minLat)) * (canvas.height - 20) + 10
        }));
        
        console.log("Current cities:", CurrentCities);
        drawCities(CurrentCities);
        
    } catch (error) {
        // This will now catch network errors AND any JSON parsing errors
        console.error("Failed to load cities:", error);
        alert(error.message);
    }
});
document.getElementById('solve-btn').addEventListener('click', async () => {
    const response = await fetch('/api/solve', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ cities: CurrentCities })
    });
    const result = await response.json();
    console.log("Best route:", result.route);
    // Map route to include x,y for drawing
    const routeWithCoords = result.route.map(city => {
        const match = CurrentCities.find(c => c.lat === city.lat && c.lon === city.lon);
        return { ...city, x: match.x, y: match.y };
    });
    drawRoute(routeWithCoords);
});


function drawCities(cities) {
    const canvas = document.getElementById('tsp-canvas');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    cities.forEach(city => {
        ctx.beginPath();
        ctx.arc(city.x, city.y, 5, 0, 2 * Math.PI);
        ctx.fillStyle = 'blue';
        ctx.fill();
    });
}

function drawRoute(route) {
    const canvas = document.getElementById('tsp-canvas');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    route.forEach((city, index) => {
        ctx.beginPath();
        ctx.arc(city.x, city.y, 5, 0, 2 * Math.PI);
        ctx.fillStyle = 'blue';
        ctx.fill();
        if (index > 0) {
            const prevCity = route[index - 1];
            ctx.beginPath();
            ctx.moveTo(prevCity.x, prevCity.y);
            ctx.lineTo(city.x, city.y);
            ctx.strokeStyle = 'red';
            ctx.stroke();
        }   
    });
    // Connect last city to first to complete the loop
    const firstCity = route[0];
    const lastCity = route[route.length - 1];
    ctx.beginPath();
    ctx.moveTo(lastCity.x, lastCity.y);
    ctx.lineTo(firstCity.x, firstCity.y);
    ctx.strokeStyle = 'red';
    ctx.stroke();
}