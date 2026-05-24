patient_name = input("Nhập họ tên: ")
patient_age = int(input("Nhập tuổi: "))
oxygen_concentration = int(input("Nhập nồng độ oxi trong máu: "))
heart = int(input("Nhập nhịp tim (Nhịp/phút): "))
is_health_insurance = input("Có thẻ Bảo hiểm Y tế không?(yes or no): ")

if oxygen_concentration < 90 or heart > 120:
    print("Báo động ĐỎ (Cấp cứu khẩn)")
elif oxygen_concentration <= 95 or heart >= 100:
    print("Báo động VÀNG (Theo dõi sát)")
else:
    print("XANH (Khám thường)")

if patient_age < 6 or patient_age >= 80:
    print("Miễn phí (0 VNĐ)")
elif is_health_insurance == "yes":
    print("Giảm 50% (250,000 VNĐ)")
else:
    print("Thu 100% (500,000 VNĐ)")