# AWS Infrastructure Automation with Terraform & Python

## 🚀 Project Overview
This project automates AWS infrastructure deployment using **Terraform** and **Python**. It sets up essential cloud resources such as:

- **VPC (Virtual Private Cloud)**
- **Security Groups**
- **Key Pairs** (for SSH access)

The deployment process is automated using a Python script that interacts with Terraform.

---

## 📂 Project Structure
```
📦 aws-infrastructure
├── terraform/                  # Terraform scripts
│   ├── main.tf                 # Defines AWS resources
│   ├── variables.tf            # Terraform variables
│   ├── outputs.tf              # Terraform outputs
│   ├── providers.tf            # AWS provider configuration
│   ├── terraform.tfvars        # Variable values
├── scripts/
│   ├── terraform_automation.py # Python script to run Terraform commands
├── README.md                   # Project documentation
```

---

## ⚡ Prerequisites
Before running this project, ensure you have the following installed:

- **Python 3.x**
- **Terraform** ([Install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli))
- **AWS CLI** ([Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html))
- **Git**
- AWS credentials configured (`aws configure`)

---

## 🔧 Setup & Usage
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/aws-infrastructure.git
cd aws-infrastructure
```

### **2️⃣ Initialize Terraform**
```sh
python scripts/terraform_automation.py init
```

### **3️⃣ Plan & Apply Infrastructure**
```sh
python scripts/terraform_automation.py plan
python scripts/terraform_automation.py apply
```

### **4️⃣ Destroy Infrastructure (if needed)**
```sh
python scripts/terraform_automation.py destroy
```

---

## 🛠️ How It Works
The Python script automates Terraform commands:
```python
import subprocess

def terraform_run(command):    
    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.stdout.decode()

directory = "C:/Users/sarth/Downloads/aws/Wanderlust-Mega-Project/terraform"

command_init = f'terraform -chdir={directory} init'
command_plan = f'terraform -chdir={directory} plan'
command_apply = f'terraform -chdir={directory} apply -auto-approve'
command_destroy = f'terraform -chdir={directory} destroy -auto-approve'

output = terraform_run(command_init)
print(output)
```

---

## 🔥 Enhancements
Want to take this project to the next level? Consider adding:
- **EC2 instance deployment** inside the VPC
- **Load Balancer integration**
- **CI/CD pipeline using GitHub Actions or Jenkins**
- **Terraform state management with AWS S3 & DynamoDB**

---

## 🤝 Contributing
Feel free to fork this repository and submit a pull request with improvements!

---

## 📜 License
This project is licensed under the MIT License.

---

### 🌟 Show Some Love
If you found this project helpful, give it a ⭐ on GitHub!

