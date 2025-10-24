"""
Weather Tool - Example tool for the agent.
This is a mock weather service that returns hardcoded data.
"""

from typing import Dict, Any, Optional
from datetime import datetime
import random


class WeatherTool:
    """
    Mock weather tool for agent.
    
    In a real application, this would call an actual weather API
    like OpenWeatherMap, Weather.gov, etc.
    """
    
    def __init__(self):
        """Initialize weather tool with mock data."""
        self.name = "weather"
        self.description = "Get current weather information for a location"
        
        # Mock weather data for different cities
        self.mock_data = {
            "madrid": {
                "temperature": 25,
                "condition": "Sunny",
                "humidity": 45,
                "wind_speed": 10
            },
            "london": {
                "temperature": 15,
                "condition": "Cloudy",
                "humidity": 70,
                "wind_speed": 15
            },
            "new york": {
                "temperature": 20,
                "condition": "Partly Cloudy",
                "humidity": 60,
                "wind_speed": 12
            },
            "tokyo": {
                "temperature": 22,
                "condition": "Rainy",
                "humidity": 80,
                "wind_speed": 8
            }
        }
    
    def get_weather(self, location: str = "madrid") -> Dict[str, Any]:
        """
        Get weather for a location.
        
        Args:
            location: City name (default: madrid)
            
        Returns:
            Dictionary with weather information
        """
        location_lower = location.lower()
        
        # Check if we have mock data for this location
        if location_lower in self.mock_data:
            data = self.mock_data[location_lower]
        else:
            # Return random data for unknown locations
            data = {
                "temperature": random.randint(15, 30),
                "condition": random.choice(["Sunny", "Cloudy", "Rainy", "Partly Cloudy"]),
                "humidity": random.randint(40, 90),
                "wind_speed": random.randint(5, 25)
            }
        
        return {
            "location": location.title(),
            "temperature": f"{data['temperature']}°C",
            "condition": data['condition'],
            "humidity": f"{data['humidity']}%",
            "wind_speed": f"{data['wind_speed']} km/h",
            "timestamp": datetime.now().isoformat(),
            "source": "mock_data"
        }
    
    def get_forecast(self, location: str = "madrid", days: int = 3) -> Dict[str, Any]:
        """
        Get weather forecast for multiple days.
        
        Args:
            location: City name
            days: Number of days (1-7)
            
        Returns:
            Dictionary with forecast information
        """
        forecast = []
        
        for day in range(min(days, 7)):
            day_data = {
                "day": day + 1,
                "temperature_high": random.randint(20, 35),
                "temperature_low": random.randint(10, 20),
                "condition": random.choice(["Sunny", "Cloudy", "Rainy", "Partly Cloudy"]),
                "precipitation_chance": random.randint(0, 100)
            }
            forecast.append(day_data)
        
        return {
            "location": location.title(),
            "forecast": forecast,
            "timestamp": datetime.now().isoformat()
        }
    
    def __call__(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """
        Make the tool callable by the agent.
        
        Args:
            query: Analysis from agent with keywords
            
        Returns:
            Weather information
        """
        # Extract location from query keywords if present
        keywords = query.get("keywords", [])
        location = "madrid"  # default
        
        # Simple location extraction
        known_locations = ["madrid", "london", "new", "york", "tokyo", "paris", "berlin"]
        for keyword in keywords:
            if keyword in known_locations:
                if keyword == "new" and "york" in keywords:
                    location = "new york"
                    break
                location = keyword
                break
        
        # Check if it's a forecast request
        if any(word in keywords for word in ["forecast", "tomorrow", "week"]):
            return self.get_forecast(location)
        else:
            return self.get_weather(location)


# Additional tools
class TimeTool:
    """Get current time information."""
    
    def __init__(self):
        self.name = "time"
        self.description = "Get current time and date"
    
    def get_time(self) -> Dict[str, Any]:
        """Get current time."""
        now = datetime.now()
        return {
            "current_time": now.strftime("%H:%M:%S"),
            "date": now.strftime("%Y-%m-%d"),
            "day_of_week": now.strftime("%A"),
            "timezone": "UTC",
            "timestamp": now.isoformat()
        }
    
    def __call__(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """Make tool callable."""
        return self.get_time()


class CalculatorTool:
    """Perform simple calculations."""
    
    def __init__(self):
        self.name = "calculator"
        self.description = "Perform mathematical calculations"
    
    def calculate(self, expression: str) -> Dict[str, Any]:
        """
        Evaluate a mathematical expression.
        
        Args:
            expression: Math expression as string
            
        Returns:
            Calculation result
        """
        try:
            # Safe evaluation of simple expressions
            # WARNING: In production, use a proper math parser!
            allowed_chars = set("0123456789+-*/(). ")
            if all(c in allowed_chars for c in expression):
                result = eval(expression)
                return {
                    "expression": expression,
                    "result": result,
                    "status": "success"
                }
            else:
                return {
                    "expression": expression,
                    "error": "Invalid characters in expression",
                    "status": "error"
                }
        except Exception as e:
            return {
                "expression": expression,
                "error": str(e),
                "status": "error"
            }
    
    def __call__(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """Make tool callable."""
        keywords = query.get("keywords", [])
        
        # Try to extract numbers and operators
        expression = " ".join(keywords)
        
        # Simple pattern matching
        if any(op in expression for op in ["+", "-", "*", "/"]):
            return self.calculate(expression)
        else:
            return {
                "error": "No valid calculation found in query",
                "status": "error"
            }


# Example usage
if __name__ == "__main__":
    print("🌤️  Weather Tool Demo\n")
    print("=" * 50)
    
    # Create weather tool
    weather = WeatherTool()
    
    # Test current weather
    print("\n📍 Current Weather in Madrid:")
    madrid_weather = weather.get_weather("madrid")
    for key, value in madrid_weather.items():
        print(f"  {key}: {value}")
    
    # Test forecast
    print("\n📅 3-Day Forecast for London:")
    forecast = weather.get_forecast("london", days=3)
    for day in forecast["forecast"]:
        print(f"  Day {day['day']}: {day['condition']}, "
              f"{day['temperature_low']}°C - {day['temperature_high']}°C")
    
    # Test time tool
    print("\n⏰ Time Tool Demo:")
    time_tool = TimeTool()
    time_info = time_tool.get_time()
    for key, value in time_info.items():
        print(f"  {key}: {value}")
    
    # Test calculator
    print("\n🔢 Calculator Tool Demo:")
    calc = CalculatorTool()
    result = calc.calculate("10 + 5 * 2")
    print(f"  Expression: {result['expression']}")
    print(f"  Result: {result.get('result', 'N/A')}")
    
    print("\n" + "=" * 50)
    print("✅ All tools tested successfully!")
