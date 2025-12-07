# Migration Guide: CloudIDP v2.0 (AWS) → v3.0 (Multi-Cloud)

## 📋 Overview

This guide helps you migrate from CloudIDP v2.0 (AWS-only) to CloudIDP v3.0 (Multi-Cloud Platform supporting AWS, Azure, and GCP).

---

## 🔄 What's Changed

### Major Changes

1. **Multi-Cloud Support**
   - AWS remains fully supported (100% feature parity with v2.0)
   - Azure support added with all 16 modules
   - GCP support coming soon

2. **Cloud Provider Selection**
   - New radio button selector at the top of the application
   - Dynamic theme switching based on provider
   - Provider-specific filtering in sidebar

3. **File Structure**
   - AWS files remain unchanged (backward compatible)
   - New Azure service files (`azure_*.py`)
   - New Azure module files (`azure_modules_*.py`)
   - Enhanced navigation and sidebar components

4. **Themes**
   - AWS theme preserved from v2.0
   - New Azure theme added
   - Automatic theme application based on provider

5. **Configuration**
   - Enhanced `config_settings.py` for multi-cloud
   - Updated `core_session_manager.py` for cloud context
   - Backward compatible with existing AWS configs

---

## 🚀 Migration Steps

### Step 1: Backup Your Current Installation

```bash
# Backup your current CloudIDP v2.0
cp -r cloudidps_enhanced_v2 cloudidps_enhanced_v2_backup

# Backup your secrets
cp .streamlit/secrets.toml .streamlit/secrets.toml.backup
```

### Step 2: Install CloudIDP v3.0

```bash
# Option A: Fresh installation
git clone <cloudidp-multicloud-repo>
cd cloudidp_multicloud

# Option B: In-place upgrade
# Copy all new files to your existing directory
```

### Step 3: Update Dependencies

```bash
# Install new dependencies (includes Azure SDK)
pip install -r requirements.txt

# Or update existing environment
pip install --upgrade -r requirements.txt
```

### Step 4: Update Configuration

#### 4.1 Update secrets.toml

Add Azure credentials to your existing `.streamlit/secrets.toml`:

```toml
# ===== EXISTING AWS CONFIGURATION (Keep as is) =====
[aws]
access_key_id = "YOUR_AWS_ACCESS_KEY"
secret_access_key = "YOUR_AWS_SECRET_KEY"
region = "us-east-1"

# ===== NEW: Add Azure Configuration =====
[azure]
subscription_id = "YOUR_AZURE_SUBSCRIPTION_ID"
tenant_id = "YOUR_AZURE_TENANT_ID"
client_id = "YOUR_AZURE_CLIENT_ID"
client_secret = "YOUR_AZURE_CLIENT_SECRET"

# ===== EXISTING: Anthropic API (Keep as is) =====
[anthropic]
api_key = "YOUR_ANTHROPIC_API_KEY"
```

#### 4.2 Update Firebase/Firestore (if used)

Your existing Firebase configuration remains the same. No changes needed.

### Step 5: Migrate Custom Modules (If Any)

If you have custom modules in v2.0:

1. **Identify custom modules** - Any files you added beyond the default v2.0 files
2. **Review compatibility** - Check if they depend on AWS-specific code
3. **Update imports** - Update any changed import paths
4. **Test thoroughly** - Test in both AWS and Azure modes

Example migration of a custom module:

```python
# Before (v2.0)
from aws_theme import AWSTheme
from modules_dashboard import DashboardModule

# After (v3.0) - Make it cloud-aware
from aws_theme import AWSTheme
from azure_theme import AzureTheme
import streamlit as st

# Check cloud provider
cloud_provider = st.session_state.get('cloud_provider', 'AWS')
if cloud_provider == 'AWS':
    # Use AWS implementation
    pass
elif cloud_provider == 'Azure':
    # Use Azure implementation
    pass
```

### Step 6: Test Migration

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Test AWS mode**
   - Select "AWS" radio button
   - Navigate through all 16 modules
   - Verify all existing functionality works
   - Check data is loading correctly

3. **Test Azure mode**
   - Select "Azure" radio button
   - Navigate through modules
   - Verify Azure credentials work
   - Test basic operations

4. **Test provider switching**
   - Switch back and forth between AWS and Azure
   - Verify theme changes
   - Check filters update correctly

---

## 🔧 Troubleshooting

### Issue: AWS functionality not working after migration

**Solution:**
1. Verify AWS credentials in secrets.toml
2. Check that all original AWS files are present
3. Ensure boto3 is installed: `pip install boto3`

### Issue: Azure credentials error

**Solution:**
1. Verify all 4 Azure credentials are in secrets.toml:
   - subscription_id
   - tenant_id
   - client_id
   - client_secret
2. Test Azure CLI access: `az login`
3. Verify service principal has proper permissions

### Issue: Module not found errors

**Solution:**
```bash
# Reinstall all dependencies
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
```

### Issue: Theme not switching

**Solution:**
1. Clear Streamlit cache: Press 'C' in the app
2. Hard refresh browser: Ctrl+Shift+R (or Cmd+Shift+R on Mac)
3. Check session state: `st.session_state.cloud_provider`

---

## 📊 Feature Comparison

| Feature | v2.0 (AWS Only) | v3.0 (Multi-Cloud) |
|---------|----------------|-------------------|
| Cloud Providers | AWS only | AWS + Azure (+ GCP coming) |
| Account Management | AWS Accounts | Accounts + Subscriptions |
| Themes | AWS Orange | AWS Orange + Azure Blue |
| Modules | 16 AWS modules | 16 modules per cloud |
| Navigation | AWS tabs | Cloud-aware navigation |
| Sidebar | AWS filters | Provider-specific filters |
| Session State | AWS-specific | Multi-cloud context |
| Configuration | AWS config | Multi-cloud config |

---

## ✅ Migration Checklist

- [ ] Backup v2.0 installation
- [ ] Backup secrets.toml
- [ ] Install v3.0 files
- [ ] Update requirements.txt dependencies
- [ ] Add Azure credentials to secrets.toml
- [ ] Test AWS mode functionality
- [ ] Test Azure mode functionality
- [ ] Test cloud provider switching
- [ ] Migrate any custom modules
- [ ] Update documentation
- [ ] Train team on new features
- [ ] Update deployment pipelines (if any)

---

## 🆕 New Features to Explore

After migration, explore these new v3.0 features:

1. **Cloud Provider Selector**
   - Top of page radio buttons
   - Seamless switching between clouds

2. **Azure Modules**
   - All 16 modules available for Azure
   - Azure-specific services and features

3. **Enhanced Theming**
   - Azure Blue theme
   - Automatic theme switching

4. **Multi-Cloud Context**
   - Session manager tracks current cloud
   - Filters adapt to provider

5. **Unified Interface**
   - Same workflows across clouds
   - Consistent user experience

---

## 📚 Additional Resources

- **Full Documentation**: `README.md`
- **Azure Module Guide**: `CREATE_REMAINING_AZURE_MODULES.md`
- **Architecture Diagrams**: `/docs/architecture`
- **API Reference**: `/docs/api`

---

## 🆘 Getting Help

If you encounter issues during migration:

1. **Check logs**
   ```bash
   streamlit run app.py --logger.level=debug
   ```

2. **Review error messages**
   - Most errors will indicate missing credentials or dependencies

3. **Contact support**
   - Email: support@yourcompany.com
   - Slack: #cloudidp-support
   - GitHub Issues: [repository]/issues

---

## 💡 Best Practices

1. **Test in Demo Mode First**
   - Use demo mode to familiarize with Azure features
   - No risk to production resources

2. **Gradual Rollout**
   - Start with development accounts/subscriptions
   - Move to production after thorough testing

3. **Documentation**
   - Update your internal documentation
   - Document any custom configurations

4. **Training**
   - Train team on multi-cloud features
   - Create runbooks for common tasks

---

## 🎯 Next Steps

After successful migration:

1. **Onboard Azure Subscriptions**
   - Use Subscription Lifecycle module
   - Configure subscriptions in Azure mode

2. **Set Up Azure Resources**
   - Create resource groups
   - Deploy test resources
   - Configure monitoring

3. **Explore Azure Modules**
   - Dashboard
   - Resource Inventory
   - Cost Management
   - Security & Compliance

4. **Optimize Costs**
   - Use FinOps module for both clouds
   - Compare costs across providers
   - Implement cost controls

---

**Successfully migrated? Start exploring the power of multi-cloud management!**

For questions or assistance, reach out to the CloudIDP team.
