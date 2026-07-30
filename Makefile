.PHONY: help install run test clean setup

help:
	@echo "🚀 Trợ Lý AI Đa Năng - Các lệnh hữu ích"
	@echo ""
	@echo "make install     - Cài đặt thư viện"
	@echo "make run         - Chạy ứng dụng"
	@echo "make test        - Test các công cụ"
	@echo "make setup       - Cài đặt và cấu hình ban đầu"
	@echo "make clean       - Xóa cache"
	@echo "make venv        - Tạo virtual environment"

setup:
	@echo "⚙️ Đang thiết lập dự án..."
	python -m venv venv
	@echo "✅ Virtual environment đã tạo"
	@echo ""
	@echo "Kích hoạt venv:"
	@echo "  Windows: venv\Scripts\activate"
	@echo "  macOS/Linux: source venv/bin/activate"

venv:
	@echo "📦 Tạo virtual environment..."
	python -m venv venv
	@echo "✅ Xong! Kích hoạt bằng:"
	@echo "  Windows: venv\Scripts\activate"
	@echo "  macOS/Linux: source venv/bin/activate"

install:
	@echo "📥 Cài đặt thư viện..."
	pip install --upgrade pip
	pip install -r requirements.txt
	@echo "✅ Cài đặt hoàn tất!"

run:
	@echo "🚀 Chạy ứng dụng..."
	streamlit run app.py

test:
	@echo "🧪 Chạy test công cụ..."
	python test_tools.py

clean:
	@echo "🗑️ Xóa cache..."
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	@echo "✅ Xong!"

freeze:
	@echo "📦 Cập nhật requirements.txt..."
	pip freeze > requirements.txt
	@echo "✅ Xong!"
