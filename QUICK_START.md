# CloudIDP Multi-Cloud Platform - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies (1 min)

```bash
pip install -r requirements.txt
```

### Step 2: Configure Credentials (2 min)

Create `.streamlit/secrets.toml`:

```toml
# AWS Configuration
[aws]
access_key_id = "YOUR_AWS_ACCESS_KEY"
secret_access_key = "YOUR_AWS_SECRET_KEY"
region = "us-east-1"

# Azure Configuration
[azure]
subscription_id = "YOUR_AZURE_SUBSCRIPTION_ID"
tenant_id = "YOUR_AZURE_TENANT_ID"
client_id = "YOUR_AZURE_CLIENT_ID"
client_secret = "YOUR_AZURE_CLIENT_SECRET"

# Optional: AI Features
[anthropic]
api_key = "YOUR_ANTHROPIC_API_KEY"
```

### Step 3: Run the Application (1 min)

```bash
streamlit run app.py
```

Open browser at: `http://localhost:8501`

### Step 4: Select Cloud Provider (30 sec)

1. At the top of the page, you'll see cloud provider selector
2. Choose **AWS** or **Azure** using radio buttons
3. The interface will update with provider-specific options

### Step 5: Explore Features (30 sec)

Navigate through 16 modules:
- 🏠 Dashboard - Overview
- 👥 Account/Subscription Management
- 📦 Resource Inventory
- 🌐 Network Management
- 🏢 Organizations/Management Groups
- ... and 11 more!

---

## 🎯 First Tasks

### In AWS Mode:
1. Go to Dashboard → View account metrics
2. Navigate to Resource Inventory → See AWS resources
3. Check FinOps & Cost → Review spending

### In Azure Mode:
1. Go to Dashboard → View subscription metrics
2. Navigate to Resource Inventory → See Azure resources
3. Check FinOps & Cost → Review spending

---

## 💡 Tips

- **Demo Mode**: Toggle Demo/Live in sidebar to test without real data
- **Filters**: Use sidebar filters to narrow down resources
- **Auto-Refresh**: Enable for real-time updates
- **AI Assistant**: Ask questions about your cloud infrastructure

---

## 🆘 Troubleshooting

### Issue: "No module named 'boto3'"
```bash
pip install boto3
```

### Issue: "No active accounts/subscriptions"
- Check credentials in secrets.toml
- Verify account/subscription IDs are correct

### Issue: "Permission denied"
- Verify IAM/RBAC permissions for AWS/Azure
- Check service principal has proper role assignments

---

## 📚 Learn More

- Full Documentation: `README.md`
- Migration Guide: `MIGRATION_GUIDE.md`
- Azure Modules: `CREATE_REMAINING_AZURE_MODULES.md`

---

**Ready to manage multi-cloud like a pro!** 🌐☁️
