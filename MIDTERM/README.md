# 簡易虛擬機器 (SVM)

這是系統程式課程的期中專案，實現了一個具有自己指令集的簡易虛擬機器。

## 專案概述

本專案創建了一個可以使用自定義指令集執行程式的電腦軟體模擬。這個虛擬機器模擬了基本的電腦架構，包括暫存器、記憶體和一組指令。

## 功能特點

- **自定義指令集**：實現了19種不同的指令，包括算術、邏輯和控制流操作
- **暫存器架構**：8個通用暫存器（R0-R7）
- **記憶體管理**：256個記憶體位置，使用8位元定址
- **組譯器**：將人類可讀的組合語言轉換為位元碼
- **範例程式**：包含展示計數、斐波那契數列和階乘計算的程式

## 組件

1. **虛擬機器（`vm.py`）**：執行位元碼的核心VM實現
2. **組譯器（`assembler.py`）**：將組合語言轉換為位元碼
3. **主腳本（`main.py`）**：用戶友好的程式執行介面
4. **使用指南（`usage_guide.py`）**：全面的文檔
5. **範例程式**：位於`examples/`目錄中

## 指令集

| 操作碼 | 助記符 | 描述 | 操作數 |
|--------|----------|-------------|----------|
| 0x00   | HALT     | 停止執行 | 無 |
| 0x01   | LOAD     | 將值載入暫存器 | reg, value |
| 0x02   | STORE    | 將暫存器值存入記憶體 | address, reg |
| 0x03   | MOVE     | 將值從一個暫存器複製到另一個 | dest_reg, src_reg |
| 0x04   | ADD      | 兩個暫存器相加 | dest_reg, src_reg |
| 0x05   | SUB      | 從目標減去來源 | dest_reg, src_reg |
| 0x06   | MUL      | 兩個暫存器相乘 | dest_reg, src_reg |
| 0x07   | DIV      | 目標除以來源 | dest_reg, src_reg |
| 0x08   | JMP      | 跳轉到地址 | address |
| 0x09   | JZ       | 如果為零則跳轉 | reg, address |
| 0x0A   | JNZ      | 如果不為零則跳轉 | reg, address |
| 0x0B   | JGT      | 如果大於零則跳轉 | reg, address |
| 0x0C   | JLT      | 如果小於零則跳轉 | reg, address |
| 0x0D   | PRINT    | 列印暫存器中的值 | reg |
| 0x0E   | LOAD_M   | 從記憶體載入到暫存器 | reg, address |
| 0x0F   | AND      | 位元AND | dest_reg, src_reg |
| 0x10   | OR       | 位元OR | dest_reg, src_reg |
| 0x11   | XOR      | 位元XOR | dest_reg, src_reg |
| 0x12   | NOT      | 位元NOT | reg |

## 範例程式

### 計數器
```assembly
; 計數器範例
; 這個程式從1數到10並列印每個數字

; 在R0中初始化計數器
LOAD R0 1

; 循環開始
loop:
    ; 列印當前計數器值
    PRINT R0
    
    ; 增加計數器
    LOAD R1 1
    ADD R0 R1
    
    ; 檢查計數器是否 > 10
    LOAD R2 10
    LOAD R3 0
    SUB R3 R0
    ADD R3 R2
    
    ; 如果計數器 <= 10，繼續循環
    JGT R3 loop
    
    ; 否則停止
    HALT
```

### 斐波那契數列
```assembly
; 斐波那契數列計算器
; 這個程式計算並列印前10個斐波那契數

; 初始化前兩個斐波那契數
LOAD R0 0  ; F(0) = 0
LOAD R1 1  ; F(1) = 1

; 列印前兩個數字
PRINT R0
PRINT R1

; 初始化計數器
LOAD R3 2  ; 從F(2)開始
LOAD R4 10 ; 計算到F(9)

; 循環開始
loop:
    ; 計算下一個斐波那契數：F(n) = F(n-1) + F(n-2)
    MOVE R2 R1  ; R2 = F(n-1)
    ADD R2 R0   ; R2 = F(n-1) + F(n-2) = F(n)
    
    ; 列印新的斐波那契數
    PRINT R2
    
    ; 移動值：R0 = R1, R1 = R2
    MOVE R0 R1
    MOVE R1 R2
    
    ; 增加計數器
    LOAD R5 1
    ADD R3 R5
    
    ; 檢查我們是否計算了足夠的數字
    SUB R5 R3
    ADD R5 R4
    
    ; 如果計數器 < 10，繼續循環
    JGT R5 loop
    
    ; 否則停止
    HALT
```

## 使用方法

### 運行範例程式

```bash
python main.py examples/counter.asm
```

這將：
1. 將程式從組合語言組譯為位元碼
2. 將位元碼載入到VM中
3. 執行程式

### 編寫自己的程式

1. 創建一個新的`.asm`檔案，包含你的程式碼
2. 使用主腳本運行：
   ```bash
   python main.py your_program.asm
   ```

### 除錯模式

要以詳細執行資訊運行程式：

```bash
python main.py your_program.asm --debug
```

## 教育價值

本專案展示了幾個重要的系統程式概念：

1. **指令執行週期**：取指令、解碼、執行模式
2. **記憶體管理**：程式如何與記憶體互動
3. **控制流**：跳轉和條件執行的實現
4. **組合語言**：組合程式設計的基本原則
5. **電腦架構**：電腦如何在低層級工作的簡化模型

## 未來增強

虛擬機器可能的增強包括：

1. 函數調用的堆疊實現
2. 更複雜的定址模式
3. I/O操作
4. 中斷處理
5. 浮點操作

## 系統需求

- Python 3.6或更高版本

## 授權

本專案作為系統程式課程的期中作業提交。
