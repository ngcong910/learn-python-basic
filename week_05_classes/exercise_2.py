class Sach: # tạo lớp sách
    def __init__(self, tieu_de, tac_gia, ISBN):
        self.tieu_de = tieu_de
        self.tac_gia = tac_gia
        self.ISBN = ISBN

    def display_info(self):
        return f"{self.tieu_de},{self.tac_gia},{self.ISBN}\n" # lưu thông tin sách vô hàm này

    def from_string(sach_str): # dùng để tách riêng tieu đề tác giả cà isbn
        tieu_de, tac_gia, ISBN = sach_str.strip().split(',') # strip để bỏ \n, split lọc các tieu de ...
        return Sach(tieu_de, tac_gia, ISBN)


class ThuVien: # tao lớp thư viện
    TEN_TEP = "data.txt"

    def __init__(self):
        self.sach_list = self.tai_sach()    

    def tai_sach(self): # mở hàm sách 
        sach_list = [] # tạo danh sách
        try:
            with open(self.TEN_TEP, "r", encoding="utf-8") as file: # nếu có danh sách và tệp thì tồn tại và lưu list
                sach_list = [Sach.from_string(line) for line in file.readlines()]
        except FileNotFoundError:
            pass  # Nếu tệp không tồn tại, trả về danh sách rỗng
        return sach_list

    def luu_sach(self):
        with open(self.TEN_TEP, "w", encoding="utf-8") as file: # lưu sách trên lớp sách
            for sach in self.sach_list:
                file.write(sach.display_info())

    def them_sach(self, sach):
        self.sach_list.append(sach)
        self.luu_sach()
        print("Thêm sách thành công!")

    def xoa_sach(self, ISBN): # xóa sách bằng sibn
        sach_moi = [sach for sach in self.sach_list if sach.ISBN != ISBN]
        if len(sach_moi) == len(self.sach_list):
            print("Không tìm thấy sách với ISBN đã nhập.")
        else:
            self.sach_list = sach_moi
            self.luu_sach()
            print("Xóa sách thành công!")

    def tim_kiem_sach(self, tieu_de):
        sach_tim_thay = [sach for sach in self.sach_list if tieu_de.lower() in sach.tieu_de.lower()]
        if sach_tim_thay:
            for sach in sach_tim_thay:
                sach.hien_thi_thong_tin()
        else:
            print("Không tìm thấy sách nào với tiêu đề đó.")


# Chương trình chính
if __name__ == "__main__":
    thu_vien = ThuVien()
    
    while True:
        print("\nHệ thống quản lý thư viện")
        print("1. Thêm sách")
        print("2. Xóa sách")
        print("3. Tìm kiếm sách")
        print("4. Thoát")
        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == "1":
            tieu_de = input("Nhập tiêu đề sách: ")
            tac_gia = input("Nhập tên tác giả: ")
            ISBN = input("Nhập ISBN của sách: ")
            sach = Sach(tieu_de, tac_gia, ISBN)
            thu_vien.them_sach(sach)
        elif lua_chon == "2":
            ISBN = input("Nhập ISBN của sách cần xóa: ")
            thu_vien.xoa_sach(ISBN)
        elif lua_chon == "3":
            tieu_de = input("Nhập tiêu đề sách cần tìm: ")
            thu_vien.tim_kiem_sach(tieu_de)
        elif lua_chon == "4":
            print("Thoát... Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng thử lại.")
