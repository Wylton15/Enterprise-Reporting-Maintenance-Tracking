# Enterprise-Reporting-Maintenance-Tracking
Objective
The corporate client is highly satisfied with the initial Corporate Asset Tracker. However, the accounting and IT support departments have requested two major operational features: the ability to export the current asset inventory to a spreadsheet for financial auditing and a system to log and track repairs or maintenance performed on specific assets. In this activity, you will enhance the existing Django application by implementing pagination for better UI performance, building a new related database model, and generating downloadable files using Python.


requirements.txt
Django==6.0.2
django-simple-history==3.11.0
asgiref==3.11.1
sqlparse==0.5.5
tzdata==2025.3

🏠 Dashboard	http://127.0.0.1:8000/
📋 Asset List	http://127.0.0.1:8000/list/
📥 Export to CSV	http://127.0.0.1:8000/export/csv/
🔍 Asset Detail	http://127.0.0.1:8000/1/detail/
🔧 Add Maintenance	http://127.0.0.1:8000/1/maintenance/add/
🛠 Django Admin	http://127.0.0.1:8000/admin/

Login: Username: Admin | Password: admin1234

