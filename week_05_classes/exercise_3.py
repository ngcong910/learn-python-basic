class CauThu:
    # Lớp lưu trữ thông tin cầu thủ
    def __init__(self, chieu_cao, can_nang):
        self.chieu_cao = chieu_cao  # Chiều cao của cầu thủ (m)
        self.can_nang = can_nang  # Cân nặng của cầu thủ (kg)

    def display_info(self):
        # Chuyển thông tin cầu thủ thành chuỗi để lưu vào file
        return f"{self.chieu_cao}\n{self.can_nang}\n"

    def from_string(self, chieu_cao, can_nang):
        # Tạo đối tượng CauThu từ dữ liệu chuỗi
        return CauThu(float(chieu_cao), float(can_nang))

def luu_cau_thu(ds_cau_thu):
    # Ghi danh sách cầu thủ vào file
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write(f"{len(ds_cau_thu)}\n")  # Ghi số lượng cầu thủ
        for cau_thu in ds_cau_thu:
            file.write(cau_thu.display_info())

def doc_cau_thu():
    # Đọc danh sách cầu thủ từ file
    ds_cau_thu = []
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            so_cau_thu = int(file.readline().strip())  # Đọc số lượng cầu thủ
            for _ in range(so_cau_thu):
                chieu_cao = file.readline().strip()
                can_nang = file.readline().strip()
                cau_thu = CauThu(0, 0)  # Tạo một đối tượng tạm thời
                ds_cau_thu.append(cau_thu.from_string(chieu_cao, can_nang))
    except FileNotFoundError:
        print("Không tìm thấy tệp dữ liệu!")
    except ValueError:
        print("Dữ liệu trong file không hợp lệ!")
    return ds_cau_thu


# Chương trình chính
if __name__ == "__main__":
    ds_cau_thu = []  # Danh sách cầu thủ
    so_cau_thu = int(input("Nhập số lượng cầu thủ: "))  # Nhập số lượng cầu thủ

    for i in range(1, so_cau_thu + 1):
        chieu_cao = float(input(f"Nhập chiều cao của cầu thủ {i} (m): "))
        can_nang = float(input(f"Nhập cân nặng của cầu thủ {i} (kg): "))
        ds_cau_thu.append(CauThu(chieu_cao, can_nang))

    luu_cau_thu(ds_cau_thu)  # Lưu thông tin cầu thủ vào file
    print("Dữ liệu cầu thủ đã được lưu vào file.")

    # Đọc dữ liệu từ file và hiển thị thông tin
    ds_cau_thu = doc_cau_thu()
    print("\nDanh sách cầu thủ:")
    for i, cau_thu in enumerate(ds_cau_thu, start=1):
        cau_thu.hien_thi_thong_tin(i)
