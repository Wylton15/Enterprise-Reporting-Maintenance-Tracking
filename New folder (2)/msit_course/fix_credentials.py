import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from assets.models import User
from django.contrib.auth import authenticate

# Ensure 'Admin' superuser exists with correct password
user, created = User.objects.get_or_create(username='Admin')
user.set_password('admin1234')
user.is_superuser = True
user.is_staff = True
user.role = 'ADMIN'
user.email = 'admin@example.com'
user.save()
print(f"Admin user {'created' if created else 'updated'}: username=Admin, password=admin1234")

# Test authentication
result = authenticate(username='Admin', password='admin1234')
if result:
    print(f"Authentication SUCCESS: username=Admin, superuser={result.is_superuser}, staff={result.is_staff}")
else:
    print("Authentication FAILED for Admin/admin1234")

# Also fix lowercase admin
try:
    u2 = User.objects.get(username='admin')
    u2.set_password('admin1234')
    u2.is_superuser = True
    u2.is_staff = True
    u2.role = 'ADMIN'
    u2.save()
    r2 = authenticate(username='admin', password='admin1234')
    print(f"admin user updated: auth={'SUCCESS' if r2 else 'FAILED'}")
except User.DoesNotExist:
    print("No lowercase admin user found")

print("\n--- FINAL CREDENTIALS ---")
print("For Django App Login  -> Username: Admin  | Password: admin1234")
print("For Django Admin (/admin/) -> Username: Admin  | Password: admin1234")
