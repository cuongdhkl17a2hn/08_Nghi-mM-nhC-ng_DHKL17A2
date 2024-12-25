import threading
import requests

# Hàm tải xuống tệp
def tai_tep(url, ten_tep):
    try:
        response = requests.get(url)
        with open(ten_tep, 'wb') as file:
            file.write(response.content)
        print(f"Tải xong tệp: {ten_tep}")
    except Exception as e:
        print(f"Lỗi khi tải tệp {ten_tep}: {e}")

# Danh sách các URL cần tải
urls = ["http://example.com/file1.jpg", "http://example.com/file2.jpg"]
ten_teps = ["file1.jpg", "file2.jpg"]

# Tạo và khởi chạy các luồng
threads = []
for url, ten_tep in zip(urls, ten_teps):
    thread = threading.Thread(target=tai_tep, args=(url, ten_tep))
    threads.append(thread)
    thread.start()

# Đợi tất cả các luồng hoàn thành
for thread in threads:
    thread.join()