# 🔄 Merchant Integration Process - BPMN Viewer

This project contains BPMN workflows for the merchant integration process with interactive HTML viewers. Available in both **Full** and **Simplified** versions.

## 📁 Files

**BPMN Files:**
- `merchant_integration_process.bpmn` - Full BPMN 2.0 XML process definition (detailed)
- `merchant_integration_process_simple.bpmn` - Simplified BPMN 2.0 XML process definition

**Viewers:**
- `bpmn_viewer.html` - Interactive HTML viewer for the **full** BPMN process
- `bpmn_viewer_simple.html` - Interactive HTML viewer for the **simplified** BPMN process

**Server & Docs:**
- `serve.py` - Simple Python server to run the viewers locally
- `README.md` - This file

## 🎯 Two Versions Available

### 🔧 **Full BPMN** (`bpmn_viewer.html`)
- Complete process with all intermediate steps
- Detailed message flows and events
- Multiple start points across different actors
- Comprehensive task breakdown

### ⚡ **Simplified BPMN** (`bpmn_viewer_simple.html`)
- Single start point for the entire process
- Focus on Implementation Engineer core responsibilities
- Cleaner flow without intermediate "receive" tasks
- Streamlined loops and decision points

## 🚀 Quick Start

### Option 1: Using Python Server (Recommended)
```bash
python3 serve.py
```
This will:
- Start a local server on http://localhost:8000
- Automatically open your browser with the **full** BPMN viewer
- Navigate between versions using the toggle buttons

### Option 2: Using Node.js (if you have it)
```bash
npx http-server . -p 8000 -c-1
```
Then open:
- **Full BPMN**: http://localhost:8000/bpmn_viewer.html
- **Simple BPMN**: http://localhost:8000/bpmn_viewer_simple.html

### Option 3: Using any other web server
Place all files in your web server directory and open either:
- `bpmn_viewer.html` (Full version)
- `bpmn_viewer_simple.html` (Simplified version)

## 🏊‍♂️ Process Overview

The BPMN diagram shows the merchant integration workflow with three main actors:

### **Sales Engineer (SE)**
- Initiates the process
- Schedules handover with Implementation Engineer
- Sends merchant scope information

### **Implementation Engineer (IE)**
- Receives handover from SE
- Schedules and conducts kickoff meeting
- Validates scope with merchant
- Supports integration development
- Handles certification process
- Monitors for 30 days post go-live
- Hands over to TAM team

### **Merchant**
- Participates in kickoff meeting
- Develops integration with IE support
- Submits integration for certification
- Makes adjustments if needed
- Goes live when approved

## 🔄 Key Process Flow

1. **Handover** - SE to IE with merchant scope
2. **Kickoff** - IE schedules meeting with merchant
3. **Scope Validation** - If invalid, loops back to handover
4. **Integration** - Merchant develops with IE support
5. **Certification Loop** - IE certifies, merchant adjusts if needed
6. **Go Live** - When certification passes
7. **Monitoring** - IE monitors for 30 days
8. **TAM Handover** - IE transfers to TAM team

## 🎮 Viewer Controls

- **Zoom In/Out** - Use buttons or Ctrl/Cmd + +/-
- **Fit to Screen** - Use button or Ctrl/Cmd + 0
- **Pan** - Click and drag
- **Interactive Elements** - Click on process elements for details

## 🔧 Technical Details

- **BPMN Version**: 2.0
- **Viewer Library**: bpmn-js
- **File Format**: Standard BPMN XML
- **Compatible with**: Camunda, Flowable, jBPM, Zeebe, and other BPMN engines

## 📝 Notes

- The diagram uses pool lanes to clearly separate responsibilities
- Message flows show communication between actors
- Gateways handle decision points and loops
- Process is designed for both documentation and potential automation

## 🛠️ Troubleshooting

**If the BPMN doesn't load:**
1. Make sure you're using a web server (not opening HTML file directly)
2. Check that `merchant_integration_process.bpmn` is in the same directory
3. Check browser console for any error messages
4. Try the Python server method for best compatibility 