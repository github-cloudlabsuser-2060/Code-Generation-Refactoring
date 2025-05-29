/**Fetch weather data from OpenWeatherMap API */

async function fetchWeather(city, apiKey) {
    const endpoint = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${apiKey}&units=metric`;
    const response = await fetch(endpoint);
    if (!response.ok) {
        throw new Error(`Error fetching weather data: ${response.statusText}`);
    }
    return await response.json();
}

async function displayWeather(city, apiKey) {
    try {
        const data = await fetchWeather(city, apiKey);
        const temp = data.main.temp;
        const humidity = data.main.humidity;
        const weatherDesc = data.weather[0].description;
        const extreme = data.weather.some(w =>
            w.main === 'Extreme' ||
            w.main === 'Thunderstorm' ||
            w.main === 'Tornado' ||
            w.main === 'Squall'
        );

        console.log(`Weather for ${city}:`);
        console.log(`Temperature: ${temp}°C`);
        console.log('Temperature in Fahrenheit:', celsiusToFahrenheit(temp).toFixed(2), '°F');
        console.log(`Humidity: ${humidity}%`);
        console.log(`Description: ${weatherDesc}`);
        if (extreme) {
            console.log('Warning: Extreme weather conditions detected!');
        }
    } catch (error) {
        console.error(error.message);
    }
}

function celsiusToFahrenheit(celsius) {
    return (celsius * 9/5) + 32;
}
// Example usage:
// displayWeather('London', 'YOUR_API_KEY');
//MY API key is include because I'm using it for testing purposes.

//0da3956caf4a4e94bfa7d3607e9dadd7

displayWeather('Santa Marta', '0da3956caf4a4e94bfa7d3607e9dadd7');

