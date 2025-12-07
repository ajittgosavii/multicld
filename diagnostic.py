#!/usr/bin/env python3
"""
Quick Diagnostic Script - Check if fix was applied
Run this in your project directory
"""

import os
import sys

def check_fix_applied():
    """Check if the fix was properly applied to modules_resource_inventory.py"""
    
    filename = "modules_resource_inventory.py"
    
    if not os.path.exists(filename):
        print(f"❌ ERROR: {filename} not found in current directory")
        print(f"   Current directory: {os.getcwd()}")
        print(f"   Run this script from your project root!")
        return False
    
    with open(filename, 'r') as f:
        content = f.read()
        lines = content.split('\n')
    
    print("=" * 70)
    print("DIAGNOSTIC REPORT - modules_resource_inventory.py")
    print("=" * 70)
    print()
    
    # Check 1: view_mode variable
    print("CHECK 1: Local 'view_mode' variable")
    if 'view_mode = st.radio' in content:
        print("   ❌ FAIL: Local toggle still exists (NOT FIXED)")
        print("   → The file was NOT updated correctly")
        
        # Find the line number
        for i, line in enumerate(lines, 1):
            if 'view_mode = st.radio' in line:
                print(f"   → Found at line {i}")
                print(f"   → Line content: {line.strip()}")
        return False
    else:
        print("   ✅ PASS: Local toggle removed")
    
    print()
    
    # Check 2: Global mode check
    print("CHECK 2: Global mode from session_state")
    if "session_state.get('mode'" in content or 'session_state.get("mode"' in content:
        print("   ✅ PASS: Using global mode from session_state")
        
        # Find the line
        for i, line in enumerate(lines, 1):
            if "session_state.get('mode'" in line or 'session_state.get("mode"' in line:
                print(f"   → Found at line {i}")
                print(f"   → Line: {line.strip()}")
                break
    else:
        print("   ❌ FAIL: NOT using session_state.get('mode')")
        print("   → The fix was NOT applied")
        return False
    
    print()
    
    # Check 3: Conditional check
    print("CHECK 3: Conditional logic")
    found_correct = False
    found_wrong = False
    
    for i, line in enumerate(lines, 1):
        # Old wrong way
        if 'if view_mode == "Demo Mode"' in line:
            print(f"   ❌ FAIL: Old conditional found at line {i}")
            print(f"   → Line: {line.strip()}")
            found_wrong = True
        
        # New correct way
        if "if st.session_state.get('mode'" in line or 'if global_mode ==' in line:
            print(f"   ✅ PASS: Correct conditional at line {i}")
            print(f"   → Line: {line.strip()}")
            found_correct = True
    
    if found_wrong:
        print("   ❌ Old conditional still exists!")
        return False
    elif found_correct:
        print("   ✅ Conditional is correct")
    else:
        print("   ⚠️  WARNING: Could not find conditional check")
    
    print()
    print("=" * 70)
    
    if not found_wrong and found_correct:
        print("✅ FIX APPEARS TO BE CORRECTLY APPLIED!")
        print()
        print("If you're still seeing demo data in Live mode, the issue is likely:")
        print("1. Streamlit cache needs clearing")
        print("2. Browser cache needs clearing")
        print("3. Sidebar isn't setting mode correctly")
        print()
        print("Try these steps:")
        print("  1. Stop Streamlit (Ctrl+C)")
        print("  2. Run: rm -rf ~/.streamlit/cache/")
        print("  3. Run: find . -name '__pycache__' -type d -exec rm -rf {} +")
        print("  4. Restart Streamlit")
        print("  5. Hard refresh browser (Ctrl+Shift+R)")
        return True
    else:
        print("❌ FIX WAS NOT CORRECTLY APPLIED!")
        print()
        print("The file still has the old code. You need to:")
        print("1. Download modules_resource_inventory_FIXED.py")
        print("2. Copy it over your current modules_resource_inventory.py")
        print("3. Run this script again to verify")
        return False

if __name__ == "__main__":
    print()
    print("Running diagnostic...")
    print()
    
    success = check_fix_applied()
    
    print()
    print("=" * 70)
    
    if success:
        print("STATUS: Ready to test")
    else:
        print("STATUS: Needs fix reapplication")
    
    print("=" * 70)
    print()
    
    sys.exit(0 if success else 1)
