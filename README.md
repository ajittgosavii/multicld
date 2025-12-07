# CloudIDP Multi-Cloud Platform v3.0

## 🌐 Enterprise Multi-Cloud Infrastructure Development Platform

CloudIDP Multi-Cloud Platform is a comprehensive enterprise-grade cloud infrastructure management platform that supports **AWS**, **Azure**, and **GCP** (coming soon). It provides a unified interface for managing multi-cloud environments with advanced features for operations, security, compliance, and cost management.

---

## ✨ Key Features

### 🔷 Multi-Cloud Support
- **AWS** - Full feature parity with v2.0
- **Azure** - Complete Azure service coverage
- **GCP** - Coming in next release
- Seamless cloud provider switching with radio button selector

### 📊 16 Core Modules (Available for Both AWS & Azure)
1. **Dashboard** - Enterprise overview with real-time metrics
2. **Account/Subscription Management** - Centralized account lifecycle
3. **Resource Inventory** - Complete resource tracking and analysis
4. **Network Management** - VPC/VNet, subnets, security groups
5. **Organizations/Management Groups** - Hierarchical organization management
6. **Design & Planning** - Architecture planning and design tools
7. **Provisioning** - Infrastructure as Code deployment
8. **CI/CD** - Integrated DevOps pipelines
9. **Operations** - Day-to-day operational tasks
10. **Advanced Operations** - Automation and advanced workflows
11. **Security & Compliance** - Security posture and compliance tracking
12. **Container Management** - EKS/AKS cluster management
13. **FinOps & Cost** - Cost optimization and analysis
14. **Lifecycle Management** - Account/subscription lifecycle
15. **Developer Experience** - Developer productivity tools
16. **AI Assistant** - AI-powered cloud management assistance

### 🎨 Cloud-Specific Theming
- **AWS Orange Theme** - Professional AWS-branded interface
- **Azure Blue Theme** - Microsoft Azure styled interface
- **Automatic theme switching** based on selected provider

### 🔐 Enterprise Features
- Multi-account/subscription support
- Role-based access control (RBAC)
- Compliance tracking and reporting
- Cost management and optimization
- AI-powered insights and recommendations
- Real-time monitoring and alerting

---

## 🏗️ Architecture

```
cloudidp_multicloud/
├── app.py                          # Main application entry point
├── requirements.txt                # Python dependencies
├── config_settings.py              # Multi-cloud configuration
├── core_session_manager.py         # Session state management
│
├── # Themes
├── aws_theme.py                    # AWS styling and components
├── azure_theme.py                  # Azure styling and components
│
├── # Navigation & UI Components
├── components_navigation.py        # Multi-cloud navigation
├── components_sidebar.py           # Cloud-aware sidebar
│
├── # AWS Service Files
├── aws_*.py                        # AWS service implementations
│
├── # Azure Service Files
├── azure_compute.py                # Azure VM management
├── azure_storage.py                # Azure storage services
├── azure_networking.py             # Azure networking
├── azure_*.py                      # Other Azure services
│
├── # AWS Modules
├── modules_*.py                    # 16 AWS modules
│
├── # Azure Modules
├── azure_modules_dashboard.py      # Azure dashboard
├── azure_modules_*.py              # 15+ Azure modules
│
└── # Documentation
    ├── README.md
    ├── MIGRATION_GUIDE.md
    └── CREATE_REMAINING_AZURE_MODULES.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- AWS Account (for AWS mode)
- Azure Subscription (for Azure mode)
- Anthropic API Key (for AI features)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd cloudidp_multicloud

# Install dependencies
pip install -r requirements.txt

# Configure secrets
# Create .streamlit/secrets.toml with your credentials
```

### Configuration

Create `.streamlit/secrets.toml`:

```toml
# AWS Credentials
[aws]
access_key_id = "YOUR_AWS_ACCESS_KEY"
secret_access_key = "YOUR_AWS_SECRET_KEY"
region = "us-east-1"

# Azure Credentials
[azure]
subscription_id = "YOUR_SUBSCRIPTION_ID"
tenant_id = "YOUR_TENANT_ID"
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

# Anthropic API (for AI features)
[anthropic]
api_key = "YOUR_ANTHROPIC_API_KEY"
```

### Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

---

## 🎯 Usage Guide

### Switching Cloud Providers

1. At the top of the application, you'll see the cloud provider selector
2. Use the radio buttons to switch between:
   - **AWS** - Amazon Web Services
   - **Azure** - Microsoft Azure
   - **GCP** - Google Cloud Platform (Coming Soon)
3. The entire UI will update to reflect the selected provider

### Working with AWS Mode

When in AWS mode:
- Manage multiple AWS accounts
- Navigate using AWS regions
- Access AWS-specific services (EC2, S3, RDS, etc.)
- Orange AWS theme applied

### Working with Azure Mode

When in Azure mode:
- Manage multiple Azure subscriptions
- Navigate using Azure locations
- Access Azure-specific services (VMs, Storage Accounts, SQL, etc.)
- Blue Azure theme applied

### Common Workflows

#### 1. Dashboard Overview
- View multi-account/subscription metrics
- Monitor costs across all accounts
- Track resource distribution
- Review recent activity

#### 2. Provisioning Resources
1. Select **Provisioning** module
2. Choose deployment method (CloudFormation/ARM Template)
3. Configure resources
4. Deploy with one click

#### 3. Cost Optimization
1. Navigate to **FinOps & Cost**
2. Review cost trends
3. Get AI-powered recommendations
4. Implement cost-saving measures

#### 4. Security & Compliance
1. Open **Security & Compliance** module
2. View security posture
3. Track compliance status
4. Remediate findings

---

## 📋 Module Details

### Dashboard
- Real-time metrics across all accounts/subscriptions
- Cost breakdown by account/subscription
- Resource distribution charts
- Activity feed

### Account/Subscription Management
- Onboard new accounts/subscriptions
- Configure cross-account/subscription access
- Manage account/subscription lifecycle
- View account/subscription health

### Resource Inventory
- Complete resource catalog
- Tag management
- Resource dependencies
- Search and filter

### Network Management
- VPC/VNet creation and management
- Subnet configuration
- Security groups and NSGs
- Load balancer setup

### CI/CD
- Pipeline creation and management
- Deployment automation
- Multi-stage deployments
- Approval workflows

### Container Management
- EKS/AKS cluster management
- Node pool configuration
- Application deployment
- Monitoring and logging

### AI Assistant
- Natural language queries
- Infrastructure recommendations
- Troubleshooting assistance
- Best practice guidance

---

## 🔧 Configuration Options

### Demo vs Live Mode
Toggle between:
- **Live Mode** - Real cloud data from your accounts
- **Demo Mode** - Sample data for testing and demos

### Filters
- Account/Subscription selection
- Region/Location filtering
- Environment filtering (Prod, Dev, Staging)
- Time range selection

### Auto-Refresh
- Enable/disable automatic data refresh
- Configurable refresh interval
- Manual refresh option

---

## 🛠️ Development

### Adding New Azure Modules

1. Create module file: `azure_modules_[name].py`
2. Follow the template pattern:

```python
"""
Azure Module: [Name]
[Description]
"""

import streamlit as st
from azure_theme import AzureTheme

class Azure[Name]Module:
    @staticmethod
    def render():
        st.markdown("## [Icon] [Title]")
        # Module implementation
```

3. Register in `components_navigation.py`

### Adding New Cloud Services

1. Create service file: `azure_[service].py`
2. Implement service methods
3. Use in modules

See `CREATE_REMAINING_AZURE_MODULES.md` for detailed guidelines.

---

## 🔒 Security

- Credentials stored in Streamlit secrets
- No hardcoded credentials
- Role-based access control
- Audit logging
- Encryption at rest and in transit

---

## 📚 Cloud Service Mapping

| AWS Service | Azure Equivalent | GCP Equivalent |
|-------------|-----------------|----------------|
| EC2 | Virtual Machines | Compute Engine |
| S3 | Blob Storage | Cloud Storage |
| RDS | Azure SQL | Cloud SQL |
| Lambda | Azure Functions | Cloud Functions |
| VPC | Virtual Network | VPC |
| EKS | AKS | GKE |
| IAM | Azure AD + RBAC | IAM |
| Organizations | Management Groups | Organization |
| CloudFormation | ARM/Bicep | Deployment Manager |
| CloudWatch | Azure Monitor | Cloud Monitoring |

---

## 🤝 Contributing

We welcome contributions! See `CONTRIBUTING.md` for guidelines.

---

## 📄 License

[Your License Here]

---

## 🆘 Support

- Documentation: `/docs`
- Issues: GitHub Issues
- Email: support@yourcompany.com

---

## 🗺️ Roadmap

### Current (v3.0)
- ✅ AWS full feature set
- ✅ Azure foundation
- ✅ Multi-cloud navigation
- ✅ Cloud-specific theming

### Next Release (v3.1)
- 🔲 Complete all Azure modules
- 🔲 GCP foundation
- 🔲 Multi-cloud resource comparison
- 🔲 Cross-cloud migration tools

### Future
- 🔲 Multi-cloud orchestration
- 🔲 Unified billing across clouds
- 🔲 AI-powered multi-cloud optimization
- 🔲 Disaster recovery across clouds

---

## ⭐ Acknowledgments

Built with:
- Streamlit
- AWS SDK (boto3)
- Azure SDK
- Anthropic Claude AI
- Plotly for visualizations

---

**CloudIDP Multi-Cloud Platform v3.0** - Manage any cloud, from one place
