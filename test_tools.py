"""
Test các công cụ - Để kiểm tra xem công cụ có hoạt động không
"""

from tools import AITools, execute_tool
import json


def test_calculator():
    """Test máy tính"""
    print("=" * 50)
    print("🧮 TEST: MÁY TÍNH")
    print("=" * 50)
    
    tests = [
        "2 + 2",
        "10 * 5",
        "(5 + 3) * 2",
        "100 / 4",
    ]
    
    for expr in tests:
        result = AITools.calculator(expr)
        print(f"Biểu thức: {expr}")
        print(f"Kết quả: {result}")
        print()


def test_weather():
    """Test thời tiết"""
    print("=" * 50)
    print("🌤️ TEST: THỜI TIẾT")
    print("=" * 50)
    
    cities = ["Hanoi", "Ho Chi Minh City", "Da Nang"]
    
    for city in cities:
        result = AITools.get_weather(city)
        print(f"Thành phố: {city}")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        print()


def test_translate():
    """Test dịch"""
    print("=" * 50)
    print("🗣️ TEST: DỊCH VĂN")
    print("=" * 50)
    
    tests = [
        ("Hello", "Vietnamese"),
        ("Good morning", "French"),
        ("Goodbye", "Spanish"),
    ]
    
    for text, lang in tests:
        result = AITools.translate_text(text, lang)
        print(f"Text: {text} → {lang}")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        print()


def test_time():
    """Test thời gian"""
    print("=" * 50)
    print("⏰ TEST: THỜI GIAN")
    print("=" * 50)
    
    result = AITools.get_current_time()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print()


def test_search():
    """Test tìm kiếm"""
    print("=" * 50)
    print("🔍 TEST: TÌM KIẾM")
    print("=" * 50)
    
    queries = ["Albert Einstein", "Python programming"]
    
    for query in queries:
        result = AITools.search_information(query)
        print(f"Tìm kiếm: {query}")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        print()


def test_json():
    """Test JSON"""
    print("=" * 50)
    print("📋 TEST: JSON")
    print("=" * 50)
    
    jsons = [
        '{"name": "John", "age": 30}',
        '{"students": ["Alice", "Bob", "Charlie"]}',
    ]
    
    for json_str in jsons:
        result = AITools.format_as_json(json_str)
        print(f"Input: {json_str}")
        print(f"Output:\n{result['formatted']}")
        print()


def test_execute_tool():
    """Test hàm execute_tool"""
    print("=" * 50)
    print("⚙️ TEST: EXECUTE_TOOL")
    print("=" * 50)
    
    result = execute_tool("calculator", {"expression": "5 + 5"})
    print(f"execute_tool('calculator', {{'expression': '5 + 5'}})")
    print(f"Kết quả: {result}")
    print()


if __name__ == "__main__":
    print("\n🚀 CHẠY TEST CÁC CÔNG CỤ\n")
    
    try:
        test_calculator()
    except Exception as e:
        print(f"❌ Lỗi test calculator: {e}\n")
    
    try:
        test_weather()
    except Exception as e:
        print(f"❌ Lỗi test weather: {e}\n")
    
    try:
        test_translate()
    except Exception as e:
        print(f"❌ Lỗi test translate: {e}\n")
    
    try:
        test_time()
    except Exception as e:
        print(f"❌ Lỗi test time: {e}\n")
    
    try:
        test_search()
    except Exception as e:
        print(f"❌ Lỗi test search: {e}\n")
    
    try:
        test_json()
    except Exception as e:
        print(f"❌ Lỗi test json: {e}\n")
    
    try:
        test_execute_tool()
    except Exception as e:
        print(f"❌ Lỗi test execute_tool: {e}\n")
    
    print("✅ Test hoàn tất!")
