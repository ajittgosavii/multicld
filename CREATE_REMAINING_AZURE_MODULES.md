# Azure Modules to Create

This document lists all the Azure modules that need to be created to match AWS functionality.

## Core Azure Service Files (Similar to aws_*.py)

1. **azure_compute.py** - Azure VM, Scale Sets, Availability Sets
2. **azure_storage.py** - Storage Accounts, Blob, Files, Queues, Tables
3. **azure_networking.py** - Virtual Networks, Subnets, NSGs, Load Balancers
4. **azure_databases.py** - Azure SQL, Cosmos DB, PostgreSQL, MySQL
5. **azure_aks.py** - Azure Kubernetes Service management
6. **azure_monitor.py** - Azure Monitor, Log Analytics, Application Insights
7. **azure_security.py** - Security Center, Key Vault, Azure AD
8. **azure_cost_management.py** - Cost Analysis, Budgets, Recommendations
9. **azure_resource_manager.py** - ARM templates, deployments
10. **azure_devops.py** - Azure DevOps integration
11. **azure_identity.py** - Azure AD, Managed Identities, RBAC
12. **azure_policy.py** - Azure Policy, Blueprints
13. **azure_automation.py** - Automation accounts, Runbooks

## Azure Module Files (Similar to modules_*.py)

1. ✅ **azure_modules_dashboard.py** - CREATED
2. **azure_modules_subscription_management.py** - Subscription management
3. **azure_modules_resource_inventory.py** - Resource inventory and tracking
4. **azure_modules_network_management.py** - VNet, NSG, Load Balancer management
5. **azure_modules_management_groups.py** - Management Groups hierarchy
6. **azure_modules_design_planning.py** - Architecture planning and design
7. **azure_modules_provisioning.py** - Resource provisioning via ARM/Bicep
8. **azure_modules_cicd_unified.py** - Azure DevOps CI/CD pipelines
9. **azure_modules_operations.py** - Day-to-day operations
10. **azure_modules_advanced_operations.py** - Advanced ops, automation
11. **azure_modules_security_compliance.py** - Security Center, Compliance
12. **azure_modules_aks_management.py** - AKS cluster management
13. **azure_modules_finops.py** - Cost management and optimization
14. **azure_modules_subscription_lifecycle.py** - Subscription lifecycle
15. **azure_modules_devex.py** - Developer experience tools
16. **azure_modules_ai_assistant.py** - AI-powered assistance

## Implementation Pattern

Each Azure module should follow this pattern:

```python
"""
Azure Module: [Module Name]
[Description matching AWS equivalent]
"""

import streamlit as st
from azure_theme import AzureTheme
from config_settings import AppConfig
# ... other imports

class Azure[ModuleName]Module:
    """[Module description]"""
    
    @staticmethod
    def render():
        """Render Azure [module name]"""
        
        st.markdown("## [Icon] [Module Title]")
        st.caption("[Module description]")
        
        # Azure-specific implementation
        # ...
```

## Azure Service Equivalents

| AWS Service | Azure Equivalent |
|-------------|-----------------|
| EC2 | Virtual Machines |
| S3 | Blob Storage |
| RDS | Azure SQL Database |
| Lambda | Azure Functions |
| VPC | Virtual Network |
| IAM | Azure AD + RBAC |
| CloudFormation | ARM Templates/Bicep |
| CloudWatch | Azure Monitor |
| EKS | AKS |
| Organizations | Management Groups |
| Account | Subscription |
| Control Tower | Azure Landing Zones |
| Systems Manager | Automation Account |
| Secrets Manager | Key Vault |
| Security Hub | Security Center |
| Cost Explorer | Cost Management |

