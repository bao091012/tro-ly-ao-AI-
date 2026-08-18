"""
Các công cụ hỗ trợ cho Trợ lý AI
"""
import json
import os
from datetime import datetime
import requests


class AITools:
    """Bộ công cụ cho AI sử dụng"""

    def __init__(self, google_api_key: str = None, openweather_key: str = None):
        self.google_api_key = google_api_key or os.getenv("GOOGLE_API_KEY", "AQ.Ab8RN6LasT9VWVMeub7XXB4VPt0v9X5qQAjEKOBMBLSNGxqIZA")
        self.openweather_key = openweather_key or os.getenv("OPENWEATHER_API_KEY", "614859b889a9e5d051c60d45643f2de6")

    # Các phương thức instance làm alias để tương thích với app.py
    def weather(self, city: str) -> dict:
        return self.get_weather(city, self.openweather_key)

    def translate(self, text: str, target_language: str) -> dict:
        return self.translate_text(text, target_language)

    def get_time(self) -> dict:
        return self.get_current_time()

    def search(self, query: str) -> dict:
        return self.search_information(query)

    def format_json(self, expression: str) -> dict:
        return self.format_as_json(expression)

    @staticmethod
    def calculator(expression: str) -> dict:
        """Máy tính: Tính toán biểu thức toán học"""
        try:
            allowed_chars = set('0123456789+-*/.()% ')
            if not all(c in allowed_chars for c in expression):
                return {"error": "Biểu thức không hợp lệ"}
            
            result = eval(expression)
            return {
                "expression": expression,
                "result": result,
                "status": "success"
            }
        except Exception as e:
            return {"error": f"Lỗi tính toán: {str(e)}"}

    @staticmethod
    def get_weather(city: str, api_key: str = "") -> dict:
        """Dự báo thời tiết - Dùng OpenWeatherMap"""
        try:
            # Sử dụng OpenWeatherMap API
            if not api_key:
                api_key = os.getenv("OPENWEATHER_API_KEY", "614859b889a9e5d051c60d45643f2de6")
            
            if not api_key:
                return {"error": "Chưa nhập OpenWeather API Key"}
            
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=vi"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "city": data.get('name', city),
                    "temperature": f"{data['main']['temp']:.1f}°C",
                    "description": data['weather'][0]['description'],
                    "humidity": f"{data['main']['humidity']}%",
                    "wind_speed": f"{data['wind']['speed']:.1f} m/s",
                    "status": "success"
                }
            elif response.status_code == 401:
                return {"error": "API Key không hợp lệ"}
            else:
                return {"error": "Không tìm thấy thành phố"}
        except Exception as e:
            return {"error": f"Lỗi lấy thời tiết: {str(e)}"}

    @staticmethod
    def translate_text(text: str, target_language: str) -> dict:
        """Dịch văn bản"""
        try:
            from_lang = "vi"
            to_lang_map = {
                "Tiếng Việt": "vi",
                "English": "en", 
                "French": "fr", 
                "Spanish": "es",
                "Chinese": "zh", 
                "Japanese": "ja", 
                "Korean": "ko",
                "German": "de", 
                "Russian": "ru"
            }
            
            to_lang = to_lang_map.get(target_language, "en")
            url = f"https://api.mymemory.translated.net/get?q={text}&langpair={from_lang}|{to_lang}"
            
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data['responseStatus'] == 200:
                    return {
                        "original": text,
                        "translated": data['responseData']['translatedText'],
                        "target_language": target_language,
                        "status": "success"
                    }
            return {"error": "Không thể dịch văn bản"}
        except Exception as e:
            return {"error": f"Lỗi dịch: {str(e)}"}

    @staticmethod
    def get_current_time() -> dict:
        """Lấy thời gian hiện tại"""
        try:
            now = datetime.now()
            return {
                "time": now.strftime("%H:%M:%S"),
                "date": now.strftime("%d/%m/%Y"),
                "day_of_week": now.strftime("%A"),
                "status": "success"
            }
        except Exception as e:
            return {"error": f"Lỗi lấy thời gian: {str(e)}"}

    @staticmethod
    def search_information(query: str) -> dict:
        """Tìm kiếm thông tin"""
        try:
            url = "https://en.wikipedia.org/w/api.php"
            params = {
                "action": "query",
                "format": "json",
                "srsearch": query,
                "list": "search"
            }
            response = requests.get(url, params=params, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                results = data['query']['search']
                
                if results:
                    return {
                        "query": query,
                        "results": [
                            {
                                "title": r['title'],
                                "snippet": r['snippet']
                            }
                            for r in results[:3]
                        ],
                        "status": "success"
                    }
                else:
                    return {"error": "Không tìm thấy kết quả"}
            return {"error": "Lỗi tìm kiếm"}
        except Exception as e:
            return {"error": f"Lỗi tìm kiếm: {str(e)}"}

    @staticmethod
    def format_as_json(expression: str) -> dict:
        """Định dạng JSON"""
        try:
            parsed = json.loads(expression)
            formatted = json.dumps(parsed, indent=2, ensure_ascii=False)
            return {
                "formatted": formatted,
                "status": "success"
            }
        except Exception as e:
            return {"error": f"JSON không hợp lệ: {str(e)}"}


def execute_tool(tool_name: str, tool_input: dict) -> str:
    """Thực thi công cụ"""
    tools = {
        "calculator": AITools.calculator,
        "get_weather": AITools.get_weather,
        "translate_text": AITools.translate_text,
        "get_current_time": AITools.get_current_time,
        "search_information": AITools.search_information,
        "format_as_json": AITools.format_as_json,
    }
    
    if tool_name in tools:
        result = tools[tool_name](**tool_input)
        return json.dumps(result, ensure_ascii=False)
    
    return json.dumps({"error": f"Công cụ '{tool_name}' không tồn tại"})
