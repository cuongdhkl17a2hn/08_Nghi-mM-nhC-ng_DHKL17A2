radio_4_cho.grid(row=2, column=1, padx=10, pady=5, sticky="w")
radio_7_cho = tk.Radiobutton(root, text="7 chỗ", variable=var_loai_xe, value="7 chỗ")
radio_7_cho.grid(row=2, column=1, padx=10, pady=5, sticky="e")

# Tạo nút tính cước
button_tinh_cuoc = tk.Button(root, text="Tính cước", command=tinh_cuoc)
button_tinh_cuoc.grid(row=3, column=0, columnspan=2, pady=10)

# Nhãn hiển thị kết quả
label_ket_qua = tk.Label(root, text="Tiền cước: 0 đồng")
label_ket_qua.grid(row=4, column=0, columnspan=2, pady=5)

# Chạy ứng dụng
root.mainloop()