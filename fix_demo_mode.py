#!/usr/bin/env python3
"""
CloudIDP Demo/Live Mode Fix Automation Script
Helps identify and fix demo mode issues across the codebase
"""

import os
import re
from typing import List, Dict, Tuple

class DemoModeFixer:
    """Automated fixer for demo mode issues"""
    
    def __init__(self, directory: str = "."):
        self.directory = directory
        self.issues_found = []
        
    def scan_files(self) -> Dict[str, List[Tuple[int, str, str]]]:
        """
        Scan all Python files for demo mode issues
        
        Returns:
            Dict mapping filename to list of (line_number, issue_type, line_content)
        """
        issues_by_file = {}
        
        for filename in os.listdir(self.directory):
            if not filename.endswith('.py'):
                continue
                
            filepath = os.path.join(self.directory, filename)
            file_issues = []
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    
                for line_num, line in enumerate(lines, 1):
                    # Check for local demo mode toggles
                    if self._is_local_toggle(line):
                        file_issues.append((
                            line_num,
                            "LOCAL_TOGGLE",
                            line.strip()
                        ))
                    
                    # Check for hardcoded demo_mode
                    if self._is_hardcoded_demo(line):
                        file_issues.append((
                            line_num,
                            "HARDCODED_DEMO",
                            line.strip()
                        ))
                    
                    # Check for direct "Demo Mode" string checks
                    if self._is_direct_demo_check(line):
                        file_issues.append((
                            line_num,
                            "DIRECT_DEMO_CHECK",
                            line.strip()
                        ))
                    
                    # Check for view_mode variable usage
                    if self._uses_view_mode_var(line):
                        file_issues.append((
                            line_num,
                            "VIEW_MODE_VAR",
                            line.strip()
                        ))
            
                if file_issues:
                    issues_by_file[filename] = file_issues
                    
            except Exception as e:
                print(f"Error scanning {filename}: {e}")
        
        return issues_by_file
    
    def _is_local_toggle(self, line: str) -> bool:
        """Check if line contains a local demo mode toggle"""
        return ('st.radio' in line and 
                ('Demo Mode' in line or 'Real Mode' in line))
    
    def _is_hardcoded_demo(self, line: str) -> bool:
        """Check if line contains hardcoded demo_mode = True"""
        return re.search(r'demo_mode\s*=\s*True', line) is not None
    
    def _is_direct_demo_check(self, line: str) -> bool:
        """Check if line directly checks for 'Demo Mode' string"""
        return (re.search(r'if.*["\']Demo Mode["\']', line) and
                'session_state' not in line)
    
    def _uses_view_mode_var(self, line: str) -> bool:
        """Check if line uses view_mode variable"""
        return (re.search(r'\bview_mode\s*==', line) is not None and
                'session_state' not in line)
    
    def print_report(self, issues_by_file: Dict[str, List[Tuple[int, str, str]]]):
        """Print a formatted report of all issues found"""
        
        if not issues_by_file:
            print("✅ No demo mode issues found!")
            return
        
        print("=" * 80)
        print("DEMO MODE ISSUES FOUND")
        print("=" * 80)
        print()
        
        total_issues = sum(len(issues) for issues in issues_by_file.values())
        print(f"Found {total_issues} issues across {len(issues_by_file)} files\n")
        
        issue_type_names = {
            "LOCAL_TOGGLE": "Local Demo/Real Mode Toggle",
            "HARDCODED_DEMO": "Hardcoded demo_mode = True",
            "DIRECT_DEMO_CHECK": "Direct 'Demo Mode' string check",
            "VIEW_MODE_VAR": "Uses view_mode variable"
        }
        
        for filename, issues in sorted(issues_by_file.items()):
            print(f"\n📄 {filename}")
            print("-" * 80)
            
            for line_num, issue_type, line_content in issues:
                print(f"  Line {line_num:4d} | {issue_type_names[issue_type]}")
                print(f"           | {line_content[:70]}")
            
        print("\n" + "=" * 80)
        print("\n📋 RECOMMENDED ACTIONS:\n")
        
        # Provide specific recommendations
        for filename, issues in sorted(issues_by_file.items()):
            issue_types = {issue[1] for issue in issues}
            
            if "LOCAL_TOGGLE" in issue_types:
                print(f"  {filename}:")
                print(f"    • Remove local st.radio toggle")
                print(f"    • Replace with: st.session_state.get('mode', 'Demo')")
                print()
            
            if "HARDCODED_DEMO" in issue_types:
                print(f"  {filename}:")
                print(f"    • Remove hardcoded demo_mode = True")
                print(f"    • Add method: is_demo_mode() to check session state")
                print()
            
            if "DIRECT_DEMO_CHECK" in issue_types or "VIEW_MODE_VAR" in issue_types:
                print(f"  {filename}:")
                print(f"    • Replace view_mode checks with session_state.mode checks")
                print()
    
    def generate_fix_snippets(self, filename: str) -> List[str]:
        """Generate code snippets to fix issues in a specific file"""
        
        snippets = []
        
        # Global mode check snippet
        snippets.append("""
# Add this at the top of your render function:
global_mode = st.session_state.get('mode', 'Demo')

# Replace local toggle with mode indicator:
if global_mode == 'Demo':
    st.info("🎯 **Mode:** Demo Mode - Using sample data")
else:
    st.success("🔴 **Mode:** Real AWS Account - Showing actual data")
st.caption("Change mode in sidebar →")
""")
        
        # Conditional check snippet
        snippets.append("""
# Replace all view_mode checks with:
if st.session_state.get('mode', 'Demo') == 'Demo':
    # Demo mode code
else:
    # Real mode code
""")
        
        # Helper function snippet
        snippets.append("""
# Add helper function to your module:
def is_demo_mode():
    \"\"\"Check if currently in demo mode\"\"\"
    return st.session_state.get('mode', 'Demo') == 'Demo'

def is_live_mode():
    \"\"\"Check if currently in live mode\"\"\"
    return st.session_state.get('mode', 'Demo') == 'Live'
""")
        
        return snippets


def main():
    """Main execution function"""
    
    print("🔍 CloudIDP Demo/Live Mode Issue Scanner")
    print("=" * 80)
    print()
    
    # Get directory from user or use current
    import sys
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print(f"Scanning directory: {directory}")
    print()
    
    # Run the scan
    fixer = DemoModeFixer(directory)
    issues = fixer.scan_files()
    
    # Print report
    fixer.print_report(issues)
    
    # Offer to generate fix snippets
    if issues:
        print("\n" + "=" * 80)
        print("\n💡 For detailed fix instructions, see:")
        print("   - DEMO_LIVE_MODE_FIX_GUIDE.md")
        print("   - modules_resource_inventory_PATCH.md")
        print("   - resource_dependencies_enhanced_PATCH.md")
        print()


if __name__ == "__main__":
    main()
