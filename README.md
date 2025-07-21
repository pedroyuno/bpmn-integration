# 🔄 Merchant Integration Process - BPMN Viewer

This project contains BPMN workflows for the merchant integration process with interactive HTML viewers. Available in both **Full** and **Simplified** versions with **download functionality**.

## 📁 Files

**BPMN Files:**
- `merchant_integration_process.bpmn` - Full BPMN 2.0 XML process definition (4-lane detailed process)
- `merchant_integration_process_simple.bpmn` - Simplified BPMN 2.0 XML process definition

**Viewers:**
- `bpmn_viewer.html` - Interactive HTML viewer for the **full** BPMN process
- `bpmn_viewer_simple.html` - Interactive HTML viewer for the **simplified** BPMN process

**Server & Docs:**
- `serve.py` - Simple Python server to run the viewers locally
- `README.md` - This file

## 🎯 Two Versions Available

### 🔧 **Full BPMN** (`bpmn_viewer.html`)
- Complete 4-lane process (BDM/TAM/Merchant/KAM)
- Detailed message flows and events
- Comprehensive task breakdown with escalation paths
- Enterprise-grade BPMN structure

### ⚡ **Simplified BPMN** (`bpmn_viewer_simple.html`)
- Streamlined 4-lane process focused on core workflow
- Emphasis on TAM core responsibilities
- Cleaner flow without intermediate "receive" tasks
- Streamlined loops and decision points

## ✨ Key Features

- 📥 **Download as PNG** - Export diagrams as high-quality images
- 🖱️ **Interactive Viewers** - Zoom, pan, and explore process details
- 🔄 **Version Toggle** - Switch between full and simplified views
- ⌨️ **Keyboard Shortcuts** - Quick access to common functions
- 📱 **Responsive Design** - Works on desktop and mobile devices

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

Both BPMN diagrams show the merchant integration workflow with **four main actors** in separate pool lanes:

### **🔧 Full BPMN Process (`merchant_integration_process.bpmn`)**
**Complete detailed workflow with:**
- 4-lane structure with escalation support
- Detailed message flows between all participants
- Comprehensive event handling and decision points
- KAM escalation path for unresponsive merchants
- Professional enterprise-grade BPMN structure

**Flow:** BDM Handover → TAM Kickoff → Scope Validation → Integration Support → Certification Loop → Monitoring → Support Handover

### **⚡ Simplified BPMN Process (`merchant_integration_process_simple.bpmn`)**
**Streamlined workflow focused on core actions:**
- 4-lane structure with TAM-focused responsibilities
- Direct action-oriented tasks without intermediate steps
- Clear focus on TAM decision points and merchant interactions
- Simplified certification and escalation flows
- Clean, easy-to-follow process flow

**Flow:** Start → TAM Kickoff & Scope Validation → TAM Integration Support → TAM Certification → (if adjustments needed: back to certification) → TAM Monitoring → TAM Support Handover

## 👥 **Actor Responsibilities**

### **BDM (Business Development Manager)**
- Initiates the integration process
- Schedules handover with TAM
- Provides merchant scope information
- Handles scope revision requests

### **TAM (Technical Account Manager)** ⭐ *Main Process Owner*
- Receives handover from BDM
- Schedules and conducts kickoff meeting
- Validates scope with merchant
- Supports integration development **(TAM handles integration)**
- Handles certification process and merchant escalations
- Monitors for 30 days post go-live
- Hands over to Support team

### **Merchant**
- Participates in kickoff meeting
- Develops integration with TAM support
- Submits integration for certification
- Makes adjustments if needed
- Goes live when approved

### **KAM (Key Account Manager)**
- Engages unresponsive merchants
- Facilitates integration when escalated
- Handles merchant relationship issues

## 🔄 Key Differences Between Versions

| Feature | **Full BPMN** 🔧 | **Simple BPMN** ⚡ |
|---------|------------------|-------------------|
| **Lanes** | 4 (BDM/TAM/Merchant/KAM) | 4 (BDM/TAM/Merchant/KAM) |
| **Start Points** | Multiple with handover flow | Single TAM-driven process |
| **Task Detail** | Complete with receive/send tasks | Action-focused, streamlined steps |
| **Escalation** | Full KAM escalation path | Simplified escalation handling |
| **Message Flows** | Comprehensive cross-lane communication | Essential communication only |
| **Use Case** | Documentation, enterprise implementation | Training, quick reference |
| **Complexity** | High - enterprise grade | Medium - easy to understand |

## 🔄 Core Process Flow

1. **BDM Handover** - BDM to TAM with merchant scope
2. **Kickoff** - TAM schedules meeting with merchant  
3. **Scope Validation** - If invalid, loops back for revision
4. **Integration** - Merchant develops with TAM support
5. **Escalation** - KAM engages if merchant unresponsive
6. **Certification Loop** - TAM certifies, merchant adjusts if needed
7. **Go Live** - When certification passes
8. **Monitoring** - TAM monitors for 30 days
9. **Support Handover** - TAM transfers to Support team

## 🎮 Viewer Controls

### Navigation & Zoom
- **Zoom In/Out** - Use buttons or `Ctrl/Cmd + +/-`
- **Fit to Screen** - Use button or `Ctrl/Cmd + 0`
- **Reset Zoom** - Return to default zoom level
- **Pan** - Click and drag to move around

### Download Feature 📥
- **Download Button** - Green "📥 Download as Image" button
- **Keyboard Shortcut** - `Ctrl/Cmd + D` for quick download
- **High Quality** - PNG format with white background
- **Smart Naming** - Automatic descriptive filenames

### Interactive Elements
- Click on process elements for details
- Hover over elements for additional information

## 🔧 Technical Details

- **BPMN Version**: 2.0
- **Viewer Library**: bpmn-js v17.0.2
- **File Format**: Standard BPMN XML
- **Image Export**: PNG format via HTML5 Canvas
- **Compatible with**: Camunda, Flowable, jBPM, Zeebe, and other BPMN engines

## 📝 Process Notes

- **4-lane structure** clearly separates responsibilities across BDM, TAM, Merchant, and KAM
- **Message flows** show communication between actors
- **Gateways** handle decision points and process loops
- **Escalation path** through KAM for unresponsive merchants
- **Designed for** both documentation and potential automation

## 🛠️ Troubleshooting

**If the BPMN doesn't load:**
1. Make sure you're using a web server (not opening HTML file directly)
2. Check that the `.bpmn` files are in the same directory
3. Check browser console for any error messages
4. Try the Python server method for best compatibility

**If download doesn't work:**
1. Ensure the diagram has loaded completely
2. Check browser permissions for downloads
3. Try using the keyboard shortcut `Ctrl/Cmd + D`

## 📈 Recent Updates

- ✅ **Fixed BPMN structure** - Corrected 4-lane process (BDM/TAM/Merchant/KAM)
- ✅ **Added download functionality** - Export diagrams as PNG images
- ✅ **Updated actor information** - Reflects current organizational structure
- ✅ **Enhanced viewers** - Improved UI and user experience
- ✅ **Keyboard shortcuts** - Added quick access controls 