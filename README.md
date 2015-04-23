# wlstdo
A simple wrapper for wlst

# Start managed servers by name or app
./wlst.sh do.py --config=./domainEx01.properties --action=start --server=managed01,managed02
./wlst.sh do.py --config=./domainEx01.properties --action=start --app=cakeShop,accountingApp

# Stop managed servers by name or app
./wlst.sh do.py --config=./domainEx01.properties --action=stop --server=managed01,managed02
./wlst.sh do.py --config=./domainEx01.properties --action=stop --app=cakeShop,accountingApp

# Deploy an app
./wlst.sh do.py --config=./domainEx01.properties --action=deploy --file=/opt/deployment/accounting.war --app accountingApp
./wlst.sh do.py --config=./domainEx01.properties --action=deploy --file=/opt/deployment/sale_03_04.war --app cakeShop --appVersion 03.04

# Undeploy an app
./wlst.sh do.py --config=./domainEx01.properties --action=undeploy --app accountingApp
