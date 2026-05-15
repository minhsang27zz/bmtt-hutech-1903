def tinh_tong_so_chan(lst):
    tong = 0 
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong
innput_list = input("Nhập một danh sách số, cách nhau bởi dấu phẩy): ")
numbers = list(map(int, innput_list.split(',')))
tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong danh sách là:", tong_chan)