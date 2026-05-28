# Knowledge Base Restructure — Team Guideline

**วัตถุประสงค์:** จัดระเบียบ Knowledge Base ใหม่ทั้งหมดให้เหมาะกับระบบ RAG AI Agent (Bell)
**ผู้รับผิดชอบ:** ทีม CS + Developer
**สถานะ:** รอทีมเตรียมเนื้อหา

---

## Structure ใหม่ (ภาพรวม)

```
knowledge_base/
├── 00_index.md
├── 01_product/
├── 02_software_pos/
├── 03_web_backend/
├── 04_hardware/
├── 05_troubleshooting/
├── 06_service_requests/
├── 07_policies/
├── 08_ai_escalation_guide/
└── 09_internal_reference/        ← ไม่ใส่ RAG
```

---

## หลักการสำคัญก่อนเริ่มงาน

| หลักการ | ความหมาย |
|---|---|
| **1 ไฟล์ = 1 Topic** | แต่ละไฟล์พูดเรื่องเดียว ไม่ปนกัน |
| **Format มาตรฐาน** | แต่ละประเภทไฟล์มี template ที่กำหนด (ดูส่วน Template ด้านล่าง) |
| **ภาษา** | เขียนเป็นภาษาไทยเป็นหลัก คำศัพท์เทคนิคใช้อังกฤษได้ |
| **ห้ามใส่ข้อมูล Internal** | ชื่อทีม, ลิงก์ Jira, ขั้นตอนภายใน → ย้ายไป `09_internal_reference/` |
| **ทดสอบก่อน Finalize** | ลอง "ถามตัวเอง" ว่าถ้า AI อ่านไฟล์นี้แล้วจะตอบลูกค้าได้ถูกต้องไหม |

---

## Templates มาตรฐาน

### Template A — How-to / วิธีใช้งาน
ใช้สำหรับ: `02_software_pos/`, `03_web_backend/`, `04_hardware/`

```markdown
# [ชื่อ Feature/ฟังก์ชัน]

## ใช้ทำอะไร
[อธิบาย 1-2 ประโยค]

## วิธีใช้งาน
1. [ขั้นตอนที่ 1]
2. [ขั้นตอนที่ 2]
3. [ขั้นตอนที่ 3]

## ข้อควรระวัง / เงื่อนไขสำคัญ
- [ข้อควรระวัง]

## คำถามที่พบบ่อย (ถ้ามี)
**Q: [คำถาม]**
A: [คำตอบ]
```

---

### Template B — Troubleshooting / แก้ปัญหา
ใช้สำหรับ: `05_troubleshooting/`

```markdown
# [ชื่อปัญหา]

## อาการที่ลูกค้าแจ้ง
- [อาการ 1]
- [อาการ 2]

## สาเหตุที่พบบ่อย
- [สาเหตุ]

## วิธีแก้ไข — L1 ทำได้เอง
1. [Step 1]
2. [Step 2]
3. [Step 3]

## ข้อมูลที่ต้องขอจากลูกค้า
- [ ] ชื่อร้าน / สาขา
- [ ] [ข้อมูลเพิ่มเติมที่จำเป็น]

## เมื่อไหร่ต้อง Escalate
| เงื่อนไข | Route ไปที่ |
|---|---|
| [เงื่อนไข 1] | L2-Tech |
| [เงื่อนไข 2] | L2-Dev |
| Hardware เสียหาย | Hardware Support |
```

---

### Template C — Service Request / คำขอดำเนินการ
ใช้สำหรับ: `06_service_requests/`

```markdown
# [ชื่อ Request]

## คืออะไร
[อธิบาย 1 ประโยค]

## ข้อมูลที่ต้องเก็บจากลูกค้า
- [ ] [ข้อมูล 1]
- [ ] [ข้อมูล 2]

## ขั้นตอนดำเนินการ (L1)
1. [Step 1]
2. [Step 2]

## ระยะเวลาดำเนินการ
[ระบุเวลาที่ลูกค้าคาดหวังได้]

## Script แจ้งลูกค้า
> [ข้อความตัวอย่างที่ใช้แจ้งลูกค้า]
```

---

### Template D — Policy / นโยบาย
ใช้สำหรับ: `07_policies/`

```markdown
# [ชื่อนโยบาย]

## สรุปสั้นๆ
[1-2 ประโยค]

## รายละเอียด
[เนื้อหา]

## คำถามที่พบบ่อย
**Q: [คำถาม]**
A: [คำตอบ]

## Script สำหรับแจ้งลูกค้า (ถ้ามี)
> [ข้อความ]
```

---

## Checklist งานทั้งหมด — แยกตาม Folder

---

### FOLDER 00 — Index

| ไฟล์ | งานที่ต้องทำ | แหล่งข้อมูล | สถานะ |
|---|---|---|---|
| `00_index.md` | สร้าง Master Index รวม link ไปทุกไฟล์ | สร้างใหม่หลังทำทุกไฟล์เสร็จ | ⬜ ยังไม่เริ่ม |

---

### FOLDER 01 — Product (ข้อมูลผลิตภัณฑ์)

| ไฟล์ | งานที่ต้องทำ | แหล่งข้อมูล | สถานะ |
|---|---|---|---|
| `product_overview.md` | WePOS คืออะไร, จุดเด่น, กลุ่มลูกค้า, Project ที่รองรับ (CPF, True Coffee ฯลฯ) | `[For Client] WePOS Product Introduction.md` + Day1 slides | ⬜ |
| `hardware_models.md` | Spec ครบทุกรุ่น: iMIN D4, D1, D2, Falcon1, Swan2, SUNMI D2s Plus — processor, RAM, จอ, พอร์ต, น้ำหนัก | `WePOS Service catalog.md` (แถว Enquiry > Hardware) | ⬜ |
| `accessories.md` | Barcode Scanner Codesoft CS6600 spec, Cash Drawer EC-410 spec, กระดาษ Thermal Paper (80mm / 58mm) | `WePOS Service catalog.md` (แถว Enquiry > Accessory) | ⬜ |
| `service_packages.md` | Package ราคา (Standard Plan 1/3/6/12 เดือน รวม VAT), terminal limit, วิธีต่อแพ็กเกจ, บัญชีโอนเงิน SCB | `ขั้นตอนการสร้างร้านใหม่.md` + FAQ2026.md | ⬜ |
| `warranty_policy.md` | รับประกัน 1 ปีนับจากวันติดตั้ง, ครอบคลุมอะไร, ไม่ครอบคลุมอะไร | `WePOS Service catalog.md` (แถว Enquiry > การรับประกัน) | ⬜ |

**⚠️ ข้อมูลที่ขาด (ต้องสร้างใหม่):**
- รายชื่อ Project ทั้งหมดที่ใช้ WePOS (CPF, True Coffee, Makro ฯลฯ) และลักษณะการใช้งานของแต่ละ Project
- Cash Drawer EC-410 spec (ใน Service catalog มีแถวว่างเปล่า)

---

### FOLDER 02 — Software POS (แอปหน้าร้าน)

| ไฟล์ | งานที่ต้องทำ | แหล่งข้อมูล | สถานะ |
|---|---|---|---|
| `login_and_account.md` | เข้าสู่ระบบ, เลือก Project/Brand/Shop, ลืม PIN (OTP reset), ออกจากระบบ, เงื่อนไขรหัสผ่าน | `WePOS Service catalog.md` + `wepos-master.md` | ⬜ |
| `sales_workflow.md` | ขายสินค้า, สแกนบาร์โค้ด, เพิ่ม/ลดจำนวน, แก้ไขราคา, พักบิล, เรียกบิล, ลบบิล, ส่วนลด | `WePOS Service catalog.md` + `wepos-master.md` | ⬜ |
| `product_management.md` | เพิ่มสินค้า, แก้ไขสินค้า, หมวดหมู่สินค้า, ตัวเลือกสินค้า, ชั้นวางสินค้า, Import Master File | `WePOS Service catalog.md` + `คู่มือการใช้งาน WePOS User manual.md` | ⬜ |
| `promotions.md` | สร้างโปรโมชั่น (3 รูปแบบ: ท้ายบิล/ราคาต่ำสุด/สินค้าร่วมรายการ), ใช้งานโปรโมชั่น, โปรโมชั่น CPF | `WePOS Service catalog.md` | ⬜ |
| `stock_management.md` | จัดการสต็อก, เพิ่ม/ลดสต็อก, ลงสต็อกแบบแพ็ค (ดูคลิป) | `WePOS Service catalog.md` | ⬜ |
| `cash_management.md` | เปิดรอบขาย, ปิดรอบขาย, นำเงินเข้า/ออก, ประวัติรอบขาย, ตั้งค่ารอบขาย, ส่งอีเมลสรุป | `WePOS Service catalog.md` + `wepos-master.md` | ⬜ |
| `receipts_and_vat.md` | พิมพ์สำเนาใบเสร็จ, ยกเลิกใบเสร็จ, ออกใบกำกับภาษี (เฉพาะวันเดียวกัน), เปิด VAT Setting, RC vs IV | `WePOS Service catalog.md` | ⬜ |
| `employee_management.md` | สร้างบัญชีพนักงาน, สิทธิ์เจ้าของร้าน vs ผู้ดูแล, ปิดสถานะพนักงาน | `WePOS Service catalog.md` | ⬜ |
| `printer_setup.md` | ตั้งค่าเครื่องพิมพ์ (USB), เลือกรุ่น iMIN D4 / SUNMI, เปลี่ยนโลโก้ใบเสร็จ, spec กระดาษ Thermal | `WePOS Service catalog.md` | ⬜ |
| `offline_mode.md` | ทำอะไรได้/ไม่ได้ตอนออฟไลน์, sync อัตโนมัติเมื่อกลับออนไลน์ | `WePOS Service catalog.md` | ⬜ |
| `reports_pos.md` | ดูสรุปยอดขาย, รายการขายสินค้า, ประวัติป้ายราคา, พิมพ์ป้ายราคา | `WePOS Service catalog.md` + `wepos-master.md` | ⬜ |

**⚠️ ข้อมูลที่ขาด:**
- วิธี Sync ข้อมูล (กดปุ่มไหน อยู่เมนูไหน) — มีแต่ link ไปคลิป ต้องเขียน step-by-step
- ภาษาที่ระบบรองรับ (ไทย/อังกฤษ?)

---

### FOLDER 03 — Web Backend (หลังบ้าน)

| ไฟล์ | งานที่ต้องทำ | แหล่งข้อมูล | สถานะ |
|---|---|---|---|
| `backoffice_access.md` | URL (marketplace.weomni.com), login, Forgot Password, เงื่อนไข password 7 ข้อ, เลือก All branches | `wepos-master.md` + `WePOS Service catalog.md` | ⬜ |
| `dashboard_metrics.md` | อธิบาย 7 ตัวชี้วัด: Total Sales Before/After Discount, Discount, Total Cancel, Tax (VAT), Cost, Profit | `wepos-master.md` | ⬜ |
| `product_management_web.md` | จัดการสินค้าจากหลังบ้าน, Import Master Product, Import File, Product Management menu | `WePOS Service catalog.md` + `คู่มือการใช้งาน WePOS Web Backend.md` | ⬜ |
| `reports_web.md` | Report ประเภทต่างๆ (Tender Report, Order Transaction Report ฯลฯ), download, ส่งอีเมล | `WePOS Service catalog.md` + `คู่มือการใช้งาน WePOS Web Backend.md` | ⬜ |
| `multi_branch_management.md` | จัดการหลายสาขา, เลือก All/เฉพาะสาขา, User Management หลังบ้าน | `คู่มือการใช้งาน WePOS Web Backend.md` | ⬜ |

**⚠️ ข้อมูลที่ขาด:**
- รายชื่อ Report ทั้งหมดที่มีในระบบ และอธิบายว่าแต่ละ Report แสดงข้อมูลอะไร
- สร้าง/แก้ไขช่องทางชำระเงินจากหลังบ้าน

---

### FOLDER 04 — Hardware (ติดตั้งและ After-sale)

| ไฟล์ | งานที่ต้องทำ | แหล่งข้อมูล | สถานะ |
|---|---|---|---|
| `installation_imin_d4.md` | ขั้นตอนติดตั้ง iMIN D4 ทั้งหมด พร้อมรูป/ไดอะแกรม (ถ้ามี) | `คู่มือการติดตั้ง iMIN Falcon1.md` (เปรียบเทียบ), Day2 slides | ⬜ |
| `installation_imin_falcon1.md` | ขั้นตอนติดตั้ง iMIN Falcon1 | `คู่มือการติดตั้ง iMIN Falcon1_31Aug2025.md` | ⬜ |
| `installation_imin_swan2.md` | ขั้นตอนติดตั้ง iMIN Swan2 | `คู่มือการติดตั้ง iMIN Swan2_Nov2025.md` | ⬜ |
| `installation_sunmi_d2s.md` | ขั้นตอนติดตั้ง SUNMI D2s Plus | Day2 slides | ⬜ |
| `serial_number_lookup.md` | วิธีดู Serial Number ทุกรุ่น (iMIN D4, D1, D2, Falcon1, Swan2, SUNMI D2s+, Scanner, Cash Drawer) | `how to check serial no.md` ✅ มีครบ | ⬜ |
| `aftersale_hardware.md` | กระบวนการแจ้งซ่อม/เคลม, ข้อมูลที่ต้องเก็บ (SN, คลิป, ที่อยู่, เบอร์), ส่งซ่อมกับใคร | `WePOS iMin Device aftersale support.md` + Service catalog (แถว Hardware) | ⬜ |

**⚠️ ข้อมูลที่ขาด:**
- คู่มือติดตั้ง iMIN D1 (ไม่พบในไฟล์ปัจจุบัน)
- ชื่อและช่องทางติดต่อศูนย์บริการ (email ศูนย์ซ่อม)

---

### FOLDER 05 — Troubleshooting (แก้ปัญหา L1)

> **หลักการเขียน:** ทุกไฟล์ต้องระบุชัดว่า "L1 แก้ได้เอง" vs "ต้อง Escalate"

| ไฟล์ | ปัญหาที่ครอบคลุม | แหล่งข้อมูล | สถานะ |
|---|---|---|---|
| `login_issues.md` | เข้าไม่ได้/Error, ลืม User/PIN, Account inactive, ไม่พบร้านสาขา | Service catalog แถว Login (บรรทัด 69–73, 100) | ⬜ |
| `app_errors.md` | App ค้าง Logo, App crash/เด้งออก, Android Recovery, Boot ไม่ขึ้น, Clear Data WePOS | Service catalog แถว Error (บรรทัด 71–72, 117) | ⬜ |
| `connectivity_sync_issues.md` | Sync ไม่สำเร็จ, อินเตอร์เน็ตหลุด — fix มาตรฐาน (Router/Hotspot/กด Sync) | Service catalog แถว Sync/Internet (บรรทัด 73–74, 77–78) | ⬜ |
| `sales_errors.md` | ขายสินค้าไม่ได้, ปิดบิลไม่ได้, เปิด/ปิดรอบไม่ได้, แป้นพิมพ์ไม่ขึ้น, บิลพักแล้วไม่หาย | Service catalog (บรรทัด 75–76, 79–82, 89) | ⬜ |
| `data_discrepancy.md` | ราคาสินค้าเปลี่ยนเอง, สต็อกไม่ถูก, ยอดขายติดลบ, บิลใบเสร็จซ้ำ, ข้อมูลสินค้าหาย | Service catalog (บรรทัด 77–78, 84, 87–88) | ⬜ |
| `payment_issues.md` | ชำระเงินด้วย QR Promptpay ไม่ได้, TrueMoney ไม่ได้, ส่วนลดไม่ขึ้น | Service catalog (บรรทัด 90) | ⬜ |
| `printer_issues.md` | Printer ไม่เชื่อมต่อ, ตั้งค่าไม่สำเร็จ, พิมพ์ไม่ออก, ตัวหนังสือเพี้ยน, ปิดฝาไม่ได้, กระดาษเปล่า | Service catalog (บรรทัด 126–134) | ⬜ |
| `display_issues.md` | จอดำ, จอหลักไม่แสดงภาพ, Touchscreen ไม่ตอบ, จอเป็นเส้น, สีเพี้ยน, จอลูกค้าไม่แสดง | Service catalog (บรรทัด 121–125) | ⬜ |
| `hardware_power_issues.md` | เปิดเครื่องไม่ติด, เครื่องค้าง, ไฟดูด, วันที่/เวลาไม่ตรง | Service catalog (บรรทัด 114–119) | ⬜ |
| `cash_drawer_issues.md` | ลิ้นชักไม่เปิด, เปิดเอง, สายขาด, กลิ่นไหม้, ปรับช่องใส่เงิน | Service catalog (บรรทัด 134–138) | ⬜ |
| `scanner_issues.md` | Scanner สายขาด, อ่านไม่ได้ — workaround, วิธีแจ้งซ่อม | Service catalog (บรรทัด 139) | ⬜ |
| `web_backend_issues.md` | เข้า Web ไม่ได้, Dashboard ไม่แสดง, Report ดึงไม่ได้, Stock Management ไม่ได้ | Service catalog (บรรทัด 99–113) | ⬜ |

**⚠️ ข้อมูลที่ขาด:**
- วิธีแก้เฉพาะ SUNMI D2s+ Dashboard หมุนค้าง (ต้องติดตั้ง Android WebView) — มีแต่ link ต้องเขียน step
- วิธี Clear Data WePOS บน SUNMI (ปัจจุบันมีแต่ iMIN)

---

### FOLDER 06 — Service Requests (คำขอดำเนินการ)

| ไฟล์ | งานที่ต้องทำ | แหล่งข้อมูล | สถานะ |
|---|---|---|---|
| `new_shop_creation.md` | ขั้นตอน 4 step (ลูกค้ากรอกฟอร์ม → CS สร้าง → SO L1 → แจ้งลูกค้า), ราคา Package, Default PIN | `ขั้นตอนการสร้างร้านใหม่.md` | ⬜ |
| `terminal_management.md` | เพิ่ม Terminal (ข้อมูลที่ต้องขอ, ราคา), Unbind Terminal | Service catalog (บรรทัด 62–64) | ⬜ |
| `user_account_update.md` | เปลี่ยนชื่อ User, เปลี่ยนเบอร์โทร | Service catalog (บรรทัด 62–63) | ⬜ |
| `shop_info_update.md` | เปลี่ยนชื่อร้าน, ที่อยู่, เบอร์ร้าน, อีเมล | Service catalog (บรรทัด 57) | ⬜ |
| `payment_onboarding.md` | สมัคร SCB QR Promptpay (ลิงก์ฟอร์ม, ประสาน SCB), สมัคร TrueMoney (เอกสาร, ส่ง L2) | Service catalog (บรรทัด 59, 68) | ⬜ |
| `master_file_import.md` | ประเภทไฟล์ที่ Import ได้, ขั้นตอนขอ Import, ตรวจสอบประวัติการ Upload | Service catalog (บรรทัด 66) | ⬜ |
| `training_request.md` | แนะนำ self-service ก่อน, Training หน้างานราคา 3,000 บาท, ขั้นตอนนัดหมาย | Service catalog (บรรทัด 67) | ⬜ |
| `cancel_shop.md` | ขั้นตอน verify ลูกค้า (ชื่อเจ้าของ, ที่อยู่, เบอร์ Login), สาเหตุที่ยกเลิก, แจ้ง Manager | Service catalog (บรรทัด 65) | ⬜ |

**⚠️ ข้อมูลที่ขาด:**
- Link ฟอร์ม SCB QR Promptpay ปัจจุบัน (มีแต่ tinyurl เก่า — ยืนยันว่ายังใช้งานได้)
- ฟอร์ม WePOS New Shop Creation Request (ใช้ Google Form หรือ Excel?)
- ระยะเวลาดำเนินการแต่ละ Request (SLA ของ CS เอง)

---

### FOLDER 07 — Policies (นโยบาย)

| ไฟล์ | งานที่ต้องทำ | แหล่งข้อมูล | สถานะ |
|---|---|---|---|
| `warranty_terms.md` | รับประกัน 1 ปีนับจากวันติดตั้ง, ครอบคลุมอะไร, กระบวนการเคลม | Service catalog + `WePOS iMin Device aftersale support.md` | ⬜ |
| `vat_and_tax_rules.md` | เปิด VAT Setting บน POS, ออกใบกำกับภาษี, ใช้ 2 ระบบพร้อมกัน (แยกเล่ม), เลข RD | `POS tax.md` ✅ มีครบ + Service catalog | ⬜ |
| `data_privacy_pdpa.md` | กรณีลูกค้า Makro ขอข้อมูลคืน — script ปฏิเสธ + คำอธิบาย PDPA | `FAQ2026.md` (บรรทัด 20–25) ✅ มี script แล้ว | ⬜ |
| `sla_targets.md` | SLA ตาม Priority 1-4: First Response, Escalate, Resolution — ตาม CLAUDE.md | CLAUDE.md (ส่วน SLA) | ⬜ |
| `package_pricing_policy.md` | ราคา Package ทุก Tier, วิธีชำระ, ต่ออายุภายใน 30 นาที (ชั่วโมง 9-18), บัญชี SCB | `ขั้นตอนการสร้างร้านใหม่.md` | ⬜ |

---

### FOLDER 08 — AI Escalation Guide (สำหรับ AI Agent เท่านั้น)

> ไฟล์ใน Folder นี้ **ไม่ใช่สำหรับลูกค้า** — เป็นคู่มือให้ AI ตัดสินใจ

| ไฟล์ | งานที่ต้องทำ | แหล่งข้อมูล | สถานะ |
|---|---|---|---|
| `l1_resolution_checklist.md` | รายการปัญหาทั้งหมดที่ L1 แก้ได้เองโดยไม่ต้อง Escalate | จาก `05_troubleshooting/` ทุกไฟล์ | ⬜ |
| `escalation_decision_tree.md` | Keyword → Route: L1 Human / L2-Tech / L2-Dev / Hardware Support (จาก CLAUDE.md) | CLAUDE.md + Service catalog | ⬜ |
| `customer_scripts.md` | Script แจ้งลูกค้า: กำลัง Escalate, Holding message (TH+EN), ยืนยันเลข ticket | CLAUDE.md (Agent prompt) + Service catalog | ⬜ |
| `missing_info_prompts.md` | คำถามที่ AI ต้องถามก่อน create ticket (ชื่อร้าน, สาขา, อาการ, SN, รูปหน้าจอ) | รวบรวมจาก Service catalog | ⬜ |

---

### FOLDER 09 — Internal Reference (ไม่ใส่ RAG)

| ไฟล์ | งานที่ต้องทำ | แหล่งข้อมูล |
|---|---|---|
| `team_contacts.md` | ชื่อทีม, เบอร์/ช่องทาง, ใครดูแลอะไร | Day1 slides |
| `jira_workflow.md` | ขั้นตอนเปิด Jira Ticket (Ascend + WePOS), Template, Status | Service catalog (ทุกแถวที่มี Jira) |
| `tools_and_system_access.md` | URL Jira, WePOS Backend, เครื่องมือภายใน | Day1 slides |
| `cs_training_notes/` | ย้าย Day1–Day5 slides ทั้งหมดมาที่นี่ | Day1–5 slides ทั้งหมด |

---

## ไฟล์ปัจจุบัน → ทำอะไร

| ไฟล์ปัจจุบัน | Action | ย้ายไปที่ |
|---|---|---|
| `WePOS Service catalog.md` | **แตก** → หลายไฟล์ใน 05/ และ 06/ | — |
| `wepos-master.md` | **แตก** → หลายไฟล์ใน 02/ และ 03/ | — |
| `คู่มือการใช้งาน WePOS User manual.md` | **Merge** เข้า 02/ | — |
| `คู่มือการใช้งาน WePOS Web Backend.md` | **Merge** เข้า 03/ | — |
| `how to check serial no.md` | **Copy** ไป 04/ | `04_hardware/serial_number_lookup.md` |
| `POS tax.md` | **Copy** ไป 07/ | `07_policies/vat_and_tax_rules.md` |
| `FAQ2026.md` | **แตก** → เนื้อหาลงใน 05/, 06/, 07/ ที่เกี่ยวข้อง | — |
| `WePOS iMin Device aftersale support.md` | **Merge** เข้า 04/ | `04_hardware/aftersale_hardware.md` |
| `[For Client] WePOS Product Introduction.md` | **Merge** เข้า 01/ | `01_product/product_overview.md` |
| `คู่มือการติดตั้ง iMIN Falcon1.md` | **Copy** ไป 04/ | `04_hardware/installation_imin_falcon1.md` |
| `คู่มือการติดตั้ง iMIN Swan2.md` | **Copy** ไป 04/ | `04_hardware/installation_imin_swan2.md` |
| `ขั้นตอนการสร้างร้านใหม่.md` | **Merge** เข้า 06/ | `06_service_requests/new_shop_creation.md` |
| `Day1–Day5 slides (.md)` | **ย้าย** ไม่ใส่ RAG | `09_internal_reference/cs_training_notes/` |
| `sample_faq.md` | **ลบ** (ไม่มีเนื้อหาจริง) | — |
| `pdfs/` ทั้งหมด | **เก็บไว้** — Dev ใช้สำหรับ Gemini RAG | ไม่ต้องแตะ |

---

## ลำดับการทำงานที่แนะนำ

```
Phase 1 — สำคัญที่สุด ทำก่อน (AI ต้องการเพื่อตอบลูกค้าได้)
  ├── 05_troubleshooting/ ทั้งหมด
  ├── 06_service_requests/ ทั้งหมด
  └── 08_ai_escalation_guide/ ทั้งหมด

Phase 2 — How-to Content (ลูกค้าถามบ่อย)
  ├── 02_software_pos/ ทั้งหมด
  └── 03_web_backend/ ทั้งหมด

Phase 3 — Reference (ไม่เร่งด่วน)
  ├── 01_product/ ทั้งหมด
  ├── 04_hardware/ ทั้งหมด
  └── 07_policies/ ทั้งหมด

Phase 4 — Finalize
  ├── 00_index.md
  └── 09_internal_reference/ (ย้ายของเก่า)
```

---

## สิ่งที่ทีมต้องเตรียมเพิ่มเติม (ข้อมูลที่หายไปจากเอกสารปัจจุบัน)

| # | ข้อมูลที่ขาด | ผู้รับผิดชอบ | Priority |
|---|---|---|---|
| 1 | รายชื่อ Project ทั้งหมดที่ใช้ WePOS และลักษณะการใช้งาน | CS Lead | High |
| 2 | Spec ครบ Cash Drawer EC-410 (ตอนนี้แถวว่าง) | CS / Vendor | Medium |
| 3 | คู่มือติดตั้ง iMIN D1 (ไม่มีในไฟล์ปัจจุบัน) | CS Lead / Vendor | Medium |
| 4 | ช่องทางติดต่อและ Email ศูนย์ซ่อม | CS Lead | High |
| 5 | Step-by-step วิธีกดปุ่ม Sync (ไม่ใช่แค่ link คลิป) | CS | High |
| 6 | วิธี Clear Data WePOS บน SUNMI (ปัจจุบันมีแต่ iMIN) | CS / L2-Tech | Medium |
| 7 | รายชื่อ Report ทั้งหมดในหลังบ้าน + อธิบายแต่ละ Report | CS | Medium |
| 8 | Link ฟอร์ม SCB QR / TrueMoney — ยืนยันว่า link ยังใช้งานได้ | CS | High |
| 9 | ระยะเวลาดำเนินการแต่ละ Service Request (SLA ของ CS เอง) | CS Lead | Medium |
| 10 | Script แจ้ง Escalate ภาษาอังกฤษ (ปัจจุบันมีแต่ภาษาไทย) | CS Lead | Medium |

---

## สรุปจำนวนไฟล์ที่ต้องสร้าง

| Folder | จำนวนไฟล์ |
|---|---|
| 01_product | 5 ไฟล์ |
| 02_software_pos | 11 ไฟล์ |
| 03_web_backend | 5 ไฟล์ |
| 04_hardware | 6 ไฟล์ |
| 05_troubleshooting | 12 ไฟล์ |
| 06_service_requests | 8 ไฟล์ |
| 07_policies | 5 ไฟล์ |
| 08_ai_escalation_guide | 4 ไฟล์ |
| 09_internal_reference | ย้ายของเดิม |
| **รวม** | **56 ไฟล์** |

---

*อัพเดทล่าสุด: 2026-05-19 | สร้างโดย: Bell Agent Project*
