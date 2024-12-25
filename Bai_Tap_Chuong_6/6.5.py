import threading
import requests

# Hàm thực hiện yêu cầu HTTP
def gui_yeu_cau_http(url):
    try:
        response = requests.get(url)
        print(f"Trạng thái HTTP của {url}: {response.status_code}")
    except Exception as e:
        print(f"Lỗi khi yêu cầu {url}: {e}")

# Danh sách các URL cần gửi yêu cầu HTTP
urls = ["http://example.com", "http://example.org", "http://example.net"]

# Tạo và khởi chạy các luồng
threads = []
for url in urls:
    thread = threading.Thread(target=gui_yeu_cau_http, args=(url,))
    threads.append(thread)
    thread.start()

# Đợi tất cả các luồng hoàn thành
for thread in threads:
    thread.join()