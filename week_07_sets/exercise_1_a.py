N=input("Nhập dãy số ngẫu nhiên ( cách nhau dấu cách): ")
N=N.strip().split() # đưa N sang một danh sách
diff=set(map(int,N)) # loại bỏ cách số trùng lập
print(f"Có {len(diff)} khác nhau")
