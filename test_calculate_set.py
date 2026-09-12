"""
🧪 Tester สำหรับเครื่องคิดเลขจำนวนสมาชิกเซต
ทดสอบ Logic หลักๆ โดยไม่ต้องขึ้น GUI
"""

import sys
from io import StringIO

# ============= Mock StringVar เพื่อทดสอบโดยไม่ต้องขึ้น GUI =============
class MockStringVar:
    def __init__(self, value=""):
        self.value = value
    
    def get(self):
        return self.value
    
    def set(self, val):
        self.value = val

# ============= Import & Setup =============
sys.modules['tkinter'] = type(sys)('tkinter')
sys.modules['tkinter'].StringVar = MockStringVar
sys.modules['tkinter'].Tk = lambda: None
sys.modules['tkinter'].Frame = lambda **kwargs: None
sys.modules['tkinter'].Entry = lambda **kwargs: None
sys.modules['tkinter'].Label = lambda **kwargs: None
sys.modules['tkinter'].Button = lambda **kwargs: None

# Copy logic จาก calculate_set.py
num_vars = {
    1: MockStringVar(value=""),
    2: MockStringVar(value=""),
    3: MockStringVar(value=""),
    4: MockStringVar(value=""),
    5: MockStringVar(value=""),
    6: MockStringVar(value=""),
    7: MockStringVar(value=""),
    8: MockStringVar(value=""),
}

set_display = 1
result = ""
num_input = MockStringVar(value="n(A) = ")
na = nb = nc = nab = nac = nbc = nabc = naUbUc = 0


# ============= Functions ที่ต้องทดสอบ =============
def show_display():
    global set_display, num_input
    labels = {
        1: "n(A)",
        2: "n(B)",
        3: "n(C)",
        4: "n(A∩B)",
        5: "n(A∩C)",
        6: "n(B∩C)",
        7: "n(A∩B∩C)",
        8: "n(AUBUC)",
        9: "Enter '=' to calculate"
    }
    
    if set_display == 9:
        num_input.set(labels[9])
    else:
        label = labels.get(set_display, "")
        value = num_vars[set_display].get()
        if value == "":
            num_input.set(f"{label} = ")
        else:
            num_input.set(f"{label} = {value}")


def get_num():
    global set_display, na, nb, nc, nab, nac, nbc, nabc, naUbUc, num_input
    input_value = num_input.get()
    
    if input_value.startswith("n"):
        return
    
    if set_display in num_vars:
        num_vars[set_display].set(input_value)
        if input_value != "x":
            try:
                value = int(input_value)
                if set_display == 1: na = value
                elif set_display == 2: nb = value
                elif set_display == 3: nc = value
                elif set_display == 4: nab = value
                elif set_display == 5: nac = value
                elif set_display == 6: nbc = value
                elif set_display == 7: nabc = value
                elif set_display == 8: naUbUc = value
            except ValueError:
                pass


def show_num(num):
    global result, num_input
    
    if num_input.get().startswith("Error"):
        result = ""
        if num == "x":
            return
    
    if num_input.get().startswith("n") or num_input.get().startswith("E"):
        result = ""
    elif num == "x" and num_input.get() != "":
        result = "Error"
        num = ""
    elif num != "x" and num_input.get().startswith("x"):
        result = "Error"
        num = ""
    
    result += str(num)
    num_input.set(result)


def clear():
    global set_display, num_input
    
    if num_input.get().startswith("Error"):
        num_input.set("")
        show_display()
        return
    
    if set_display in num_vars and num_vars[set_display].get() != "":
        num_vars[set_display].set("")
        show_display()


def calculate():
    global result, na, nb, nc, nab, nac, nbc, nabc, naUbUc, num_input
    result = ""
    
    # ✅ ปรับปรุง: ตรวจสอบจำนวน unknowns และ Error ถ้ามีมากกว่า 1
    unknown_index = None
    unknown_count = 0
    
    for idx in range(1, 9):
        if num_vars[idx].get() == "x":
            unknown_count += 1
            unknown_index = idx
    
    # ✅ ปรับปรุง: ต้องมี unknown เพียง 1 ตัวพอดี
    if unknown_count == 0 or unknown_count > 1:
        result = "Error"
    elif unknown_index == 8:
        result = na + nb + nc - nab - nac - nbc + nabc
    elif unknown_index == 7:
        result = naUbUc - na - nb - nc + nab + nac + nbc
    elif unknown_index == 1:
        result = naUbUc - nb - nc + nab + nac + nbc - nabc
    elif unknown_index == 2:
        result = naUbUc - na - nc + nab + nac + nbc - nabc
    elif unknown_index == 3:
        result = naUbUc - nb - na + nab + nac + nbc - nabc
    elif unknown_index == 4:
        result = na + nb + nc - naUbUc - nac - nbc + nabc
    elif unknown_index == 5:
        result = na + nb + nc - nab - naUbUc - nbc + nabc
    elif unknown_index == 6:
        result = na + nb + nc - nab - nac - naUbUc + nabc
    
    num_input.set(result)


# ============= HELPER FUNCTIONS =============
def reset_state():
    """Reset ทุกตัวแปรเพื่อเตรียม test ใหม่"""
    global set_display, result, na, nb, nc, nab, nac, nbc, nabc, naUbUc, num_input
    global num_vars
    
    set_display = 1
    result = ""
    na = nb = nc = nab = nac = nbc = nabc = naUbUc = 0
    num_input.set("n(A) = ")
    
    for i in range(1, 9):
        num_vars[i].set("")
def test_show_display():
    """ทดสอบแสดง Label ถูกต้องหรือไม่"""
    global set_display, num_input
    print("\n📋 TEST: show_display()")
    
    test_cases = [
        (1, "n(A)", "n(A) = "),
        (2, "n(B)", "n(B) = "),
        (8, "n(AUBUC)", "n(AUBUC) = "),
    ]
    
    for display_num, label, expected in test_cases:
        reset_state()
        set_display = display_num
        num_input.set(expected)
        show_display()
        status = "✅ PASS" if num_input.get() == expected else "❌ FAIL"
        print(f"  {status}: set_display={display_num} → {num_input.get()}")


def test_get_num():
    """ทดสอบเก็บค่าตัวเลข"""
    global set_display, na, nb, num_input, num_vars
    print("\n📋 TEST: get_num()")
    
    test_cases = [
        (1, "5", 5),
        (2, "10", 10),
        (3, "15", 15),
    ]
    
    for display_num, input_val, expected_value in test_cases:
        reset_state()
        set_display = display_num
        num_input.set(input_val)
        get_num()
        
        # ตรวจสอบว่า num_vars เก็บค่าถูกไม่
        stored_value = num_vars[display_num].get()
        status = "✅ PASS" if stored_value == input_val else "❌ FAIL"
        print(f"  {status}: set_display={display_num}, input={input_val} → stored={stored_value}")


def test_calculate_n_aubuc():
    """ทดสอบคำนวณ n(AUBUC) เมื่อ n(A)=5, n(B)=10, n(C)=8, n(A∩B)=2, n(A∩C)=3, n(B∩C)=1, n(A∩B∩C)=0"""
    global na, nb, nc, nab, nac, nbc, nabc, num_vars, num_input
    print("\n📋 TEST: calculate() - n(AUBUC)")
    
    reset_state()
    # Setup test data
    na, nb, nc, nab, nac, nbc, nabc = 5, 10, 8, 2, 3, 1, 0
    
    # Setup num_vars (all filled except index 8 which is "x")
    num_vars[1].set("5")
    num_vars[2].set("10")
    num_vars[3].set("8")
    num_vars[4].set("2")
    num_vars[5].set("3")
    num_vars[6].set("1")
    num_vars[7].set("0")
    num_vars[8].set("x")  # unknown
    
    calculate()
    # Expected: 5 + 10 + 8 - 2 - 3 - 1 + 0 = 17
    expected = 17
    status = "✅ PASS" if num_input.get() == expected else "❌ FAIL"
    print(f"  {status}: n(AUBUC) = {num_input.get()}, expected = {expected}")


def test_calculate_n_a():
    """ทดสอบคำนวณ n(A) เมื่อ n(AUBUC)=20, n(B)=8, n(C)=5, n(A∩B)=2, n(A∩C)=1, n(B∩C)=3, n(A∩B∩C)=1"""
    global na, nb, nc, nab, nac, nbc, nabc, naUbUc, num_vars, num_input
    print("\n📋 TEST: calculate() - n(A)")
    
    reset_state()
    # Setup test data
    nb, nc, nab, nac, nbc, nabc, naUbUc = 8, 5, 2, 1, 3, 1, 20
    
    num_vars[1].set("x")  # unknown
    num_vars[2].set("8")
    num_vars[3].set("5")
    num_vars[4].set("2")
    num_vars[5].set("1")
    num_vars[6].set("3")
    num_vars[7].set("1")
    num_vars[8].set("20")
    
    calculate()
    # Expected: 20 - 8 - 5 + 2 + 1 + 3 - 1 = 12
    expected = 12
    status = "✅ PASS" if num_input.get() == expected else "❌ FAIL"
    print(f"  {status}: n(A) = {num_input.get()}, expected = {expected}")


def test_error_handling():
    """ทดสอบ error handling"""
    global num_input
    print("\n📋 TEST: error_handling()")
    
    reset_state()
    # Test 1: Double x
    num_input.set("x")
    show_num("x")
    status = "✅ PASS" if num_input.get() == "Error" else "❌ FAIL"
    print(f"  {status}: Double 'x' → {num_input.get()}")
    
    # Test 2: Clear error
    clear()
    status = "✅ PASS" if not num_input.get().startswith("Error") else "❌ FAIL"
    print(f"  {status}: Clear error → {num_input.get()}")


def test_no_unknown():
    """ทดสอบ calculate เมื่อไม่มี unknown"""
    global num_vars, num_input
    print("\n📋 TEST: calculate() - no unknown")
    
    reset_state()
    # Set ทั้งหมดเป็นตัวเลข (ไม่มี "x")
    for i in range(1, 9):
        num_vars[i].set("5")
    
    calculate()
    status = "✅ PASS" if num_input.get() == "Error" else "❌ FAIL"
    print(f"  {status}: No unknown → {num_input.get()}, expected = Error")


def test_show_num_sequence():
    """ทดสอบการกดปุ่มตัวเลขลำดับต่อเนื่อง"""
    global num_input
    print("\n📋 TEST: show_num() - sequence")
    
    reset_state()
    # Test: กดลำดับ 1, 2, 3
    show_num(1)
    show_num(2)
    show_num(3)
    
    status = "✅ PASS" if num_input.get() == "123" else "❌ FAIL"
    print(f"  {status}: Sequence 1→2→3 → {num_input.get()}, expected = 123")


def test_mixed_with_x():
    """ทดสอบ error เมื่อกด x แล้วกดตัวเลขอื่น"""
    global num_input
    print("\n📋 TEST: show_num() - mixed x")
    
    reset_state()
    # Test: กด 5, แล้ว x ต้องได้ Error (เพราะ 5 ≠ "")
    show_num(5)
    show_num("x")  # → "Error" (ถูกต้อง)
    
    status = "✅ PASS" if num_input.get() == "Error" else "❌ FAIL"
    print(f"  {status}: 5 then x → {num_input.get()}, expected = Error")


def test_x_first():
    """ทดสอบ x ครั้งแรก (ต้องได้ x ไม่ error)"""
    global num_input
    print("\n📋 TEST: show_num() - x first")
    
    reset_state()
    show_num("x")
    
    status = "✅ PASS" if num_input.get() == "x" else "❌ FAIL"
    print(f"  {status}: First x → {num_input.get()}, expected = x")


def test_error_recovery_by_number():
    """ทดสอบ recovery จาก error โดยกดตัวเลข"""
    global num_input
    print("\n📋 TEST: show_num() - error recovery")
    
    reset_state()
    # Test: x → Error → กดตัวเลข 5
    show_num("x")
    status1 = num_input.get() == "x"
    
    show_num("x")  # Error
    status2 = num_input.get() == "Error"
    
    show_num(5)  # Recovery - เคลียร์ error และเริ่มใหม่
    status3 = num_input.get() == "5"
    
    status = "✅ PASS" if (status1 and status2 and status3) else "❌ FAIL"
    print(f"  {status}: x → Error → 5 → {num_input.get()}, expected = 5")


def test_multiple_unknowns():
    """ทดสอบ calculate เมื่อมี multiple unknowns"""
    global num_vars, num_input
    print("\n📋 TEST: calculate() - multiple unknowns")
    
    reset_state()
    # Set หลายอันเป็น "x"
    num_vars[1].set("x")
    num_vars[2].set("x")
    num_vars[8].set("10")
    
    calculate()
    # ต้องให้ Error เพราะมี multiple unknowns
    status = "✅ PASS" if num_input.get() == "Error" else "❌ FAIL"
    print(f"  {status}: Multiple x → {num_input.get()}, expected = Error")


def test_boundary_values():
    """ทดสอบ calculate ด้วย boundary values"""
    global num_vars, num_input, na, nb, nc, nab, nac, nbc, nabc, naUbUc
    print("\n📋 TEST: calculate() - boundary values")
    
    reset_state()
    # Test: ทั้งหมด 0
    na, nb, nc, nab, nac, nbc, nabc = 0, 0, 0, 0, 0, 0, 0
    
    for i in range(1, 8):
        num_vars[i].set("0")
    num_vars[8].set("x")
    
    calculate()
    expected = 0
    status = "✅ PASS" if num_input.get() == expected else "❌ FAIL"
    print(f"  {status}: All zeros → {num_input.get()}, expected = {expected}")


# ============= RUN ALL TESTS =============
if __name__ == "__main__":
    print("=" * 60)
    print("🧪 TESTER: เครื่องคิดเลขจำนวนสมาชิกเซต")
    print("=" * 60)
    
    test_show_display()
    test_get_num()
    test_calculate_n_aubuc()
    test_calculate_n_a()
    test_error_handling()
    test_no_unknown()
    test_show_num_sequence()
    test_mixed_with_x()
    test_x_first()
    test_error_recovery_by_number()
    test_multiple_unknowns()
    test_boundary_values()
    
    print("\n" + "=" * 60)
    print("✅ ทดสอบเสร็จสิ้น!")
    print("=" * 60)
