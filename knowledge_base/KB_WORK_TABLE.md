# KB Restructure — Work Table

> ใช้ไฟล์นี้สำหรับ assign งาน และ track สถานะ  
> Template A = How-to | Template B = Troubleshooting | Template C = Service Request | Template D = Policy

---

## Phase 1 — AI Core (ทำก่อน — AI ต้องการเพื่อตอบลูกค้าได้)

### 05 Troubleshooting

| # | ไฟล์ที่ต้องสร้าง | เนื้อหาหลัก | ดึงจากไฟล์ต้นทาง | ข้อมูลที่ขาด | Template | ผู้รับผิดชอบ | สถานะ |
|---|---|---|---|---|---|---|---|
| 1 | `05_troubleshooting/login_issues.md` | เข้าไม่ได้/Error, ลืม User/PIN, Account inactive, ไม่พบร้านสาขา | Service catalog บรรทัด 69–73, 100 | — | B | | ⬜ |
| 2 | `05_troubleshooting/app_errors.md` | App ค้าง Logo, App crash/เด้งออก, Android Recovery, Boot ไม่ขึ้น, Clear Data WePOS | Service catalog บรรทัด 71–72, 117 | วิธี Clear Data บน SUNMI (มีแต่ iMIN) | B | | ⬜ |
| 3 | `05_troubleshooting/connectivity_sync_issues.md` | Sync ไม่สำเร็จ, อินเตอร์เน็ตหลุด — fix มาตรฐาน (Router/Hotspot/กด Sync) | Service catalog บรรทัด 73–74, 77–78 | Step-by-step กดปุ่ม Sync (ปัจจุบันมีแต่ link คลิป) | B | | ⬜ |
| 4 | `05_troubleshooting/sales_errors.md` | ขายสินค้าไม่ได้, ปิดบิลไม่ได้, เปิด/ปิดรอบไม่ได้, แป้นพิมพ์ไม่ขึ้น, บิลพักแล้วไม่หาย | Service catalog บรรทัด 75–76, 79–82, 89 | — | B | | ⬜ |
| 5 | `05_troubleshooting/data_discrepancy.md` | ราคาสินค้าเปลี่ยนเอง, สต็อกไม่ถูก, ยอดขายติดลบ, บิลใบเสร็จซ้ำ, ข้อมูลสินค้าหาย | Service catalog บรรทัด 77–78, 84, 87–88 | — | B | | ⬜ |
| 6 | `05_troubleshooting/payment_issues.md` | QR Promptpay ไม่ได้, TrueMoney ไม่ได้, ส่วนลดไม่ขึ้น | Service catalog บรรทัด 90 | — | B | | ⬜ |
| 7 | `05_troubleshooting/printer_issues.md` | Printer ไม่เชื่อมต่อ, ตั้งค่าไม่สำเร็จ, พิมพ์ไม่ออก, ตัวหนังสือเพี้ยน, กระดาษเปล่า | Service catalog บรรทัด 126–134 | — | B | | ⬜ |
| 8 | `05_troubleshooting/display_issues.md` | จอดำ, จอหลักไม่แสดงภาพ, Touchscreen ไม่ตอบ, จอเป็นเส้น, สีเพี้ยน, จอลูกค้าไม่แสดง | Service catalog บรรทัด 121–125 | — | B | | ⬜ |
| 9 | `05_troubleshooting/hardware_power_issues.md` | เปิดเครื่องไม่ติด, เครื่องค้าง, ไฟดูด, วันที่/เวลาไม่ตรง | Service catalog บรรทัด 114–119 | — | B | | ⬜ |
| 10 | `05_troubleshooting/cash_drawer_issues.md` | ลิ้นชักไม่เปิด, เปิดเอง, สายขาด, กลิ่นไหม้, ปรับช่องใส่เงิน | Service catalog บรรทัด 134–138 | — | B | | ⬜ |
| 11 | `05_troubleshooting/scanner_issues.md` | Scanner สายขาด, อ่านไม่ได้ — workaround, วิธีแจ้งซ่อม | Service catalog บรรทัด 139 | — | B | | ⬜ |
| 12 | `05_troubleshooting/web_backend_issues.md` | เข้า Web ไม่ได้, Dashboard ไม่แสดง, Report ดึงไม่ได้, Stock Management ไม่ได้ | Service catalog บรรทัด 99–113 | SUNMI Dashboard หมุนค้าง → ติดตั้ง Android WebView (step-by-step) | B | | ⬜ |

### 06 Service Requests

| # | ไฟล์ที่ต้องสร้าง | เนื้อหาหลัก | ดึงจากไฟล์ต้นทาง | ข้อมูลที่ขาด | Template | ผู้รับผิดชอบ | สถานะ |
|---|---|---|---|---|---|---|---|
| 13 | `06_service_requests/new_shop_creation.md` | ขั้นตอน 4 step, ราคา Package, Default PIN 123456, แจ้งข้อมูล User ให้ลูกค้า | `ขั้นตอนการสร้างร้านใหม่.md` ✅ | ฟอร์ม New Shop Creation (Google Form หรือ Excel?) | C | | ⬜ |
| 14 | `06_service_requests/terminal_management.md` | เพิ่ม Terminal (ข้อมูลที่ต้องขอ, ราคา), Unbind Terminal | Service catalog บรรทัด 62–64 | ราคาค่า Terminal เพิ่ม | C | | ⬜ |
| 15 | `06_service_requests/user_account_update.md` | เปลี่ยนชื่อ User, เปลี่ยนเบอร์โทร | Service catalog บรรทัด 62–63 | — | C | | ⬜ |
| 16 | `06_service_requests/shop_info_update.md` | เปลี่ยนชื่อร้าน, ที่อยู่, เบอร์ร้าน, อีเมล | Service catalog บรรทัด 57 | — | C | | ⬜ |
| 17 | `06_service_requests/payment_onboarding.md` | สมัคร SCB QR Promptpay (ลิงก์ฟอร์ม, ประสาน SCB), สมัคร TrueMoney (เอกสาร, ส่ง L2) | Service catalog บรรทัด 59, 68 | ยืนยัน link ฟอร์ม SCB / TMN ว่ายังใช้งานได้ | C | | ⬜ |
| 18 | `06_service_requests/master_file_import.md` | ประเภทไฟล์ที่ Import ได้, ขั้นตอนขอ Import, ตรวจสอบประวัติการ Upload | Service catalog บรรทัด 66 | — | C | | ⬜ |
| 19 | `06_service_requests/training_request.md` | แนะนำ self-service ก่อน, Training หน้างาน 3,000 บาท, ขั้นตอนนัดหมาย | Service catalog บรรทัด 67 | — | C | | ⬜ |
| 20 | `06_service_requests/cancel_shop.md` | Verify ลูกค้า (ชื่อเจ้าของ, ที่อยู่, เบอร์ Login), สาเหตุที่ยกเลิก, แจ้ง Manager | Service catalog บรรทัด 65 | — | C | | ⬜ |

### 08 AI Escalation Guide

| # | ไฟล์ที่ต้องสร้าง | เนื้อหาหลัก | ดึงจากไฟล์ต้นทาง | ข้อมูลที่ขาด | Template | ผู้รับผิดชอบ | สถานะ |
|---|---|---|---|---|---|---|---|
| 21 | `08_ai_escalation_guide/l1_resolution_checklist.md` | รายการปัญหาทั้งหมดที่ L1 แก้ได้เองโดยไม่ต้อง Escalate | จาก 05/ ทุกไฟล์ (ทำหลัง Phase 1 เสร็จ) | — | — | | ⬜ |
| 22 | `08_ai_escalation_guide/escalation_decision_tree.md` | Keyword → Route: L1 Human / L2-Tech / L2-Dev / Hardware Support | CLAUDE.md + Service catalog | — | — | | ⬜ |
| 23 | `08_ai_escalation_guide/customer_scripts.md` | Script แจ้งลูกค้า: กำลัง Escalate, Holding message (TH+EN), ยืนยันเลข ticket | CLAUDE.md (Agent prompt) + Service catalog | Script ภาษาอังกฤษ | — | | ⬜ |
| 24 | `08_ai_escalation_guide/missing_info_prompts.md` | คำถามที่ AI ต้องถามก่อน create ticket (ชื่อร้าน, สาขา, อาการ, SN, รูปหน้าจอ) | รวบรวมจาก Service catalog | — | — | | ⬜ |

---

## Phase 2 — How-to Content (ลูกค้าถามบ่อย)

### 02 Software POS

| # | ไฟล์ที่ต้องสร้าง | เนื้อหาหลัก | ดึงจากไฟล์ต้นทาง | ข้อมูลที่ขาด | Template | ผู้รับผิดชอบ | สถานะ |
|---|---|---|---|---|---|---|---|
| 25 | `02_software_pos/login_and_account.md` | เข้าสู่ระบบ, เลือก Project/Brand/Shop, ลืม PIN (OTP reset), ออกจากระบบ | Service catalog บรรทัด 13–15 + wepos-master.md | — | A | | ⬜ |
| 26 | `02_software_pos/sales_workflow.md` | ขายสินค้า, สแกนบาร์โค้ด, เพิ่ม/ลดจำนวน, แก้ไขราคา, พักบิล, เรียกบิล, ลบบิล, ส่วนลด | Service catalog บรรทัด 16–21 + wepos-master.md | — | A | | ⬜ |
| 27 | `02_software_pos/product_management.md` | เพิ่มสินค้า, แก้ไขสินค้า, หมวดหมู่, ตัวเลือกสินค้า, ชั้นวาง, Import Master File | Service catalog บรรทัด 24–28 + User manual | — | A | | ⬜ |
| 28 | `02_software_pos/promotions.md` | สร้างโปรโมชั่น 3 รูปแบบ (ท้ายบิล/ราคาต่ำสุด/สินค้าร่วมรายการ), ใช้งานโปรโมชั่น | Service catalog บรรทัด 31 | โปรโมชั่น CPF (ดึงจาก FAQ2026.md) | A | | ⬜ |
| 29 | `02_software_pos/stock_management.md` | จัดการสต็อก, เพิ่ม/ลดสต็อก, ลงสต็อกแบบแพ็ค | Service catalog บรรทัด 36–37 | — | A | | ⬜ |
| 30 | `02_software_pos/cash_management.md` | เปิดรอบขาย, ปิดรอบขาย, นำเงินเข้า/ออก, ประวัติรอบขาย, ตั้งค่ารอบขาย, ส่งอีเมลสรุป | Service catalog บรรทัด 32–35 + wepos-master.md | — | A | | ⬜ |
| 31 | `02_software_pos/receipts_and_vat.md` | พิมพ์สำเนาใบเสร็จ, ยกเลิกใบเสร็จ, ออกใบกำกับภาษี (เฉพาะวันเดียวกัน), เปิด VAT Setting, RC vs IV | Service catalog บรรทัด 28–30, 47 | — | A | | ⬜ |
| 32 | `02_software_pos/employee_management.md` | สร้างบัญชีพนักงาน, สิทธิ์เจ้าของร้าน vs ผู้ดูแล, ปิดสถานะพนักงาน | Service catalog บรรทัด 40–41 | — | A | | ⬜ |
| 33 | `02_software_pos/printer_setup.md` | ตั้งค่าเครื่องพิมพ์ (USB), เลือกรุ่น iMIN D4 / SUNMI, เปลี่ยนโลโก้ใบเสร็จ, spec กระดาษ Thermal | Service catalog บรรทัด 44–45 | — | A | | ⬜ |
| 34 | `02_software_pos/offline_mode.md` | ทำอะไรได้/ไม่ได้ตอนออฟไลน์, sync อัตโนมัติเมื่อกลับออนไลน์ | Service catalog บรรทัด 23 | — | A | | ⬜ |
| 35 | `02_software_pos/reports_pos.md` | ดูสรุปยอดขาย, รายการขายสินค้า, พิมพ์ป้ายราคา | Service catalog บรรทัด 38–39 + wepos-master.md | — | A | | ⬜ |

### 03 Web Backend

| # | ไฟล์ที่ต้องสร้าง | เนื้อหาหลัก | ดึงจากไฟล์ต้นทาง | ข้อมูลที่ขาด | Template | ผู้รับผิดชอบ | สถานะ |
|---|---|---|---|---|---|---|---|
| 36 | `03_web_backend/backoffice_access.md` | URL (marketplace.weomni.com), login, Forgot Password, เงื่อนไข password 7 ข้อ, เลือก All branches | wepos-master.md + Service catalog | — | A | | ⬜ |
| 37 | `03_web_backend/dashboard_metrics.md` | อธิบาย 7 ตัวชี้วัด: Total Sales Before/After Discount, Discount, Total Cancel, Tax (VAT), Cost, Profit | wepos-master.md ✅ มีครบ | — | A | | ⬜ |
| 38 | `03_web_backend/product_management_web.md` | จัดการสินค้าจากหลังบ้าน, Import Master Product, Import File อื่นๆ | Service catalog บรรทัด 107–109 + Web Backend manual | — | A | | ⬜ |
| 39 | `03_web_backend/reports_web.md` | Report ประเภทต่างๆ, download, ส่งอีเมล | Service catalog บรรทัด 103–105 + Web Backend manual | รายชื่อ Report ทั้งหมดในระบบ + คำอธิบาย | A | | ⬜ |
| 40 | `03_web_backend/multi_branch_management.md` | จัดการหลายสาขา, เลือก All/เฉพาะสาขา, User Management หลังบ้าน | Web Backend manual | — | A | | ⬜ |

---

## Phase 3 — Reference

### 01 Product

| # | ไฟล์ที่ต้องสร้าง | เนื้อหาหลัก | ดึงจากไฟล์ต้นทาง | ข้อมูลที่ขาด | Template | ผู้รับผิดชอบ | สถานะ |
|---|---|---|---|---|---|---|---|
| 41 | `01_product/product_overview.md` | WePOS คืออะไร, จุดเด่น, กลุ่มลูกค้า, Project ที่รองรับ | `[For Client] WePOS Product Introduction.md` + Day1 slides | รายชื่อ Project ทั้งหมดที่ใช้งาน (CPF, True Coffee ฯลฯ) | A | | ⬜ |
| 42 | `01_product/hardware_models.md` | Spec ครบทุกรุ่น: iMIN D4, D1, D2, Falcon1, Swan2, SUNMI D2s Plus | Service catalog บรรทัด 50–56 | — | D | | ⬜ |
| 43 | `01_product/accessories.md` | Barcode Scanner Codesoft CS6600 spec, Cash Drawer EC-410 spec, กระดาษ Thermal Paper | Service catalog บรรทัด 52–53 | Cash Drawer EC-410 spec (แถวว่างเปล่า) | D | | ⬜ |
| 44 | `01_product/service_packages.md` | Package ราคา Standard Plan 1/3/6/12 เดือน (รวม VAT), terminal limit, วิธีต่อแพ็กเกจ, บัญชีโอน SCB | `ขั้นตอนการสร้างร้านใหม่.md` ✅ | — | D | | ⬜ |
| 45 | `01_product/warranty_policy.md` | รับประกัน 1 ปีนับจากวันติดตั้ง, ครอบคลุมอะไร, ไม่ครอบคลุมอะไร | Service catalog บรรทัด 49 + aftersale support | — | D | | ⬜ |

### 04 Hardware

| # | ไฟล์ที่ต้องสร้าง | เนื้อหาหลัก | ดึงจากไฟล์ต้นทาง | ข้อมูลที่ขาด | Template | ผู้รับผิดชอบ | สถานะ |
|---|---|---|---|---|---|---|---|
| 46 | `04_hardware/installation_imin_d4.md` | ขั้นตอนติดตั้ง iMIN D4 ทั้งหมด | Day2 slides | คู่มือติดตั้ง iMIN D4 (ไม่มีไฟล์ปัจจุบัน — ต้องขอจากทีม) | A | | ⬜ |
| 47 | `04_hardware/installation_imin_falcon1.md` | ขั้นตอนติดตั้ง iMIN Falcon1 | `คู่มือการติดตั้ง iMIN Falcon1.md` ✅ | — | A | | ⬜ |
| 48 | `04_hardware/installation_imin_swan2.md` | ขั้นตอนติดตั้ง iMIN Swan2 | `คู่มือการติดตั้ง iMIN Swan2.md` ✅ | — | A | | ⬜ |
| 49 | `04_hardware/installation_sunmi_d2s.md` | ขั้นตอนติดตั้ง SUNMI D2s Plus | Day2 slides | คู่มือติดตั้ง SUNMI D2s+ (ต้องขอจากทีม) | A | | ⬜ |
| 50 | `04_hardware/serial_number_lookup.md` | วิธีดู Serial Number ทุกรุ่น (iMIN D4/D1/D2/Falcon1, SUNMI D2s+, Scanner, Cash Drawer) | `how to check serial no.md` ✅ มีครบ | — | A | | ⬜ |
| 51 | `04_hardware/aftersale_hardware.md` | กระบวนการแจ้งซ่อม/เคลม, ข้อมูลที่ต้องเก็บ (SN, คลิป, ที่อยู่, เบอร์), ส่งซ่อมกับใคร | `WePOS iMin Device aftersale support.md` + Service catalog (Hardware แถว) | Email/ช่องทางติดต่อศูนย์ซ่อม | C | | ⬜ |

### 07 Policies

| # | ไฟล์ที่ต้องสร้าง | เนื้อหาหลัก | ดึงจากไฟล์ต้นทาง | ข้อมูลที่ขาด | Template | ผู้รับผิดชอบ | สถานะ |
|---|---|---|---|---|---|---|---|
| 52 | `07_policies/warranty_terms.md` | รับประกัน 1 ปีนับจากวันติดตั้ง, ครอบคลุมอะไร, กระบวนการเคลม | Service catalog + aftersale support | — | D | | ⬜ |
| 53 | `07_policies/vat_and_tax_rules.md` | เปิด VAT Setting บน POS, ออกใบกำกับภาษี, ใช้ 2 ระบบพร้อมกัน (แยกเล่ม), เลข RD | `POS tax.md` ✅ มีครบ | — | D | | ⬜ |
| 54 | `07_policies/data_privacy_pdpa.md` | กรณีลูกค้า Makro ขอข้อมูลคืน — script ปฏิเสธ + คำอธิบาย PDPA | `FAQ2026.md` บรรทัด 20–25 ✅ | — | D | | ⬜ |
| 55 | `07_policies/sla_targets.md` | SLA ตาม Priority 1-4: First Response, Escalate, Resolution | CLAUDE.md (ส่วน SLA) | — | D | | ⬜ |
| 56 | `07_policies/package_pricing_policy.md` | ราคา Package ทุก Tier, วิธีชำระ, ต่ออายุภายใน 30 นาที (9:00–18:00), บัญชี SCB | `ขั้นตอนการสร้างร้านใหม่.md` ✅ | — | D | | ⬜ |

---

## Phase 4 — Finalize

| # | ไฟล์ที่ต้องสร้าง | เนื้อหาหลัก | ดึงจากไฟล์ต้นทาง | ข้อมูลที่ขาด | Template | ผู้รับผิดชอบ | สถานะ |
|---|---|---|---|---|---|---|---|
| 57 | `00_index.md` | Master index รวม link ทุกไฟล์ + คำอธิบายสั้น | สร้างหลังทุกไฟล์เสร็จ | — | — | | ⬜ |

---

## ไฟล์เดิม → Action

| ไฟล์เดิม | Action | ย้ายไปที่ |
|---|---|---|
| `WePOS Service catalog.md` | แตกเนื้อหา → หลายไฟล์ใน 05/ และ 06/ | — |
| `wepos-master.md` | แตกเนื้อหา → หลายไฟล์ใน 02/ และ 03/ | — |
| `คู่มือการใช้งาน WePOS User manual.md` | Merge เนื้อหา → 02/ | — |
| `คู่มือการใช้งาน WePOS Web Backend.md` | Merge เนื้อหา → 03/ | — |
| `how to check serial no.md` | Copy → 04/ | `04_hardware/serial_number_lookup.md` |
| `POS tax.md` | Copy → 07/ | `07_policies/vat_and_tax_rules.md` |
| `FAQ2026.md` | แตกเนื้อหา → 05/, 06/, 07/ | — |
| `WePOS iMin Device aftersale support.md` | Merge → 04/ | `04_hardware/aftersale_hardware.md` |
| `[For Client] WePOS Product Introduction.md` | Merge → 01/ | `01_product/product_overview.md` |
| `คู่มือการติดตั้ง iMIN Falcon1.md` | Copy → 04/ | `04_hardware/installation_imin_falcon1.md` |
| `คู่มือการติดตั้ง iMIN Swan2.md` | Copy → 04/ | `04_hardware/installation_imin_swan2.md` |
| `ขั้นตอนการสร้างร้านใหม่.md` | Merge → 06/ | `06_service_requests/new_shop_creation.md` |
| `Day1–Day5 slides (.md)` | ย้าย — ไม่ใส่ RAG | `09_internal_reference/cs_training_notes/` |
| `sample_faq.md` | ลบ | — |
| `pdfs/` ทั้งหมด | เก็บไว้ — Dev ใช้สำหรับ Gemini RAG | ไม่ต้องแตะ |

---

## ข้อมูลที่ต้องเตรียมเพิ่ม (Missing Info)

| # | ข้อมูลที่ขาด | ใช้ใน | ผู้รับผิดชอบ | Priority | สถานะ |
|---|---|---|---|---|---|
| 1 | รายชื่อ Project ทั้งหมดที่ใช้ WePOS + ลักษณะการใช้งาน | `01_product/product_overview.md` | CS Lead | 🔴 High | ⬜ |
| 2 | Email / ช่องทางติดต่อศูนย์ซ่อม iMIN | `04_hardware/aftersale_hardware.md` | CS Lead | 🔴 High | ⬜ |
| 3 | Step-by-step กดปุ่ม Sync (ไม่ใช่แค่ link คลิป) | `05_troubleshooting/connectivity_sync_issues.md` | CS | 🔴 High | ⬜ |
| 4 | ยืนยัน link ฟอร์ม SCB QR / TrueMoney ว่าใช้งานได้ | `06_service_requests/payment_onboarding.md` | CS | 🔴 High | ⬜ |
| 5 | Cash Drawer EC-410 spec ครบ (ปัจจุบันว่างเปล่า) | `01_product/accessories.md` | CS / Vendor | 🟡 Medium | ⬜ |
| 6 | คู่มือติดตั้ง iMIN D4 และ SUNMI D2s+ (ไม่มีไฟล์) | `04_hardware/installation_*.md` | CS Lead / Vendor | 🟡 Medium | ⬜ |
| 7 | วิธี Clear Data WePOS บน SUNMI (มีแต่ iMIN) | `05_troubleshooting/app_errors.md` | CS / L2-Tech | 🟡 Medium | ⬜ |
| 8 | รายชื่อ Report ทั้งหมดในหลังบ้าน + คำอธิบาย | `03_web_backend/reports_web.md` | CS | 🟡 Medium | ⬜ |
| 9 | ราคาค่า Terminal เพิ่ม | `06_service_requests/terminal_management.md` | CS Lead | 🟡 Medium | ⬜ |
| 10 | Script Escalation ภาษาอังกฤษ (มีแต่ภาษาไทย) | `08_ai_escalation_guide/customer_scripts.md` | CS Lead | 🟡 Medium | ⬜ |

---

## Templates มาตรฐาน

### Template A — How-to
```markdown
# [ชื่อ Feature]

## ใช้ทำอะไร
[อธิบาย 1-2 ประโยค]

## วิธีใช้งาน
1. [Step 1]
2. [Step 2]

## ข้อควรระวัง
- [ข้อควรระวัง]

## คำถามที่พบบ่อย
**Q:** [คำถาม]  
**A:** [คำตอบ]
```

### Template B — Troubleshooting
```markdown
# [ชื่อปัญหา]

## อาการที่ลูกค้าแจ้ง
- [อาการ 1]

## วิธีแก้ไข — L1 ทำได้เอง
1. [Step 1]
2. [Step 2]

## ข้อมูลที่ต้องขอจากลูกค้า
- [ ] ชื่อร้าน / สาขา
- [ ] [ข้อมูลอื่นๆ]

## เมื่อไหร่ต้อง Escalate
| เงื่อนไข | Route ไปที่ |
|---|---|
| [เงื่อนไข] | L2-Tech / L2-Dev / Hardware Support |
```

### Template C — Service Request
```markdown
# [ชื่อ Request]

## ข้อมูลที่ต้องเก็บจากลูกค้า
- [ ] [ข้อมูล 1]
- [ ] [ข้อมูล 2]

## ขั้นตอนดำเนินการ (L1)
1. [Step 1]
2. [Step 2]

## ระยะเวลาดำเนินการ
[ระบุเวลา]

## Script แจ้งลูกค้า
> [ข้อความ]
```

### Template D — Policy / ข้อมูลอ้างอิง
```markdown
# [ชื่อนโยบาย / ข้อมูล]

## สรุป
[1-2 ประโยค]

## รายละเอียด
[เนื้อหา]

## Script สำหรับแจ้งลูกค้า (ถ้ามี)
> [ข้อความ]
```

---

*อัพเดทล่าสุด: 2026-05-19*
