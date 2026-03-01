import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from decimal import Decimal
from datetime import date
from assets.models import Asset, MaintenanceLog, User

# Get users for assignment
admin = User.objects.filter(username='Admin').first() or User.objects.filter(username='admin').first()
juan  = User.objects.filter(username='juan').first()
user  = User.objects.filter(username='user').first()

# ---------------------------------------------------------------
# STEP 1: Add more assets to reach 15 total
# ---------------------------------------------------------------
new_assets = [
    dict(name='Dell XPS 15',         asset_type='LAPTOP',    cost=Decimal('75000.00'), assigned_to=admin),
    dict(name='HP EliteDesk 800',     asset_type='LAPTOP',    cost=Decimal('42000.00'), assigned_to=juan),
    dict(name='Samsung 32" Monitor',  asset_type='MONITOR',   cost=Decimal('18000.00'), assigned_to=admin),
    dict(name='LG UltraWide 34"',     asset_type='MONITOR',   cost=Decimal('22500.00'), assigned_to=user),
    dict(name='iPhone 14 Pro Max',    asset_type='PHONE',     cost=Decimal('68000.00'), assigned_to=admin),
    dict(name='Samsung Galaxy S23',   asset_type='PHONE',     cost=Decimal('55000.00'), assigned_to=juan),
    dict(name='Ergonomic Chair Pro',  asset_type='FURNITURE', cost=Decimal('12000.00'), assigned_to=user),
    dict(name='Standing Desk 180cm',  asset_type='FURNITURE', cost=Decimal('28000.00'), assigned_to=admin),
    dict(name='MacBook Pro 14"',      asset_type='LAPTOP',    cost=Decimal('95000.00'), assigned_to=None),
]

created = 0
for data in new_assets:
    if Asset.objects.count() < 15:
        Asset.objects.get_or_create(name=data['name'], defaults=data)
        created += 1

print(f"Assets now: {Asset.objects.count()} (added {created} new)")

# ---------------------------------------------------------------
# STEP 2: Add maintenance logs to reach 5 total
# ---------------------------------------------------------------
logs = [
    dict(asset=Asset.objects.get(name='ASUS 2026'),        service_date=date(2026, 1, 10), description='Fan cleaning and thermal paste replacement', cost=Decimal('800.00')),
    dict(asset=Asset.objects.get(name='N-Vision 2025'),    service_date=date(2026, 1, 22), description='Backlight repair and panel calibration',       cost=Decimal('3500.00')),
    dict(asset=Asset.objects.get(name='ACER 2000'),        service_date=date(2026, 2, 5),  description='SSD upgrade from 512GB to 1TB',               cost=Decimal('4200.00')),
    dict(asset=Asset.objects.get(name='Iphone 13 Pro'),    service_date=date(2026, 2, 18), description='Battery replacement - reduced to 79% capacity', cost=Decimal('2800.00')),
    dict(asset=Asset.objects.get(name='LazyBoy'),          service_date=date(2026, 3, 1),  description='Hydraulic pump replacement and upholstery cleaning', cost=Decimal('1500.00')),
]

log_created = 0
for log in logs:
    if MaintenanceLog.objects.count() < 5:
        obj, created_flag = MaintenanceLog.objects.get_or_create(
            asset=log['asset'],
            service_date=log['service_date'],
            defaults={'description': log['description'], 'cost': log['cost']}
        )
        if created_flag:
            log_created += 1

print(f"Maintenance Logs now: {MaintenanceLog.objects.count()} (added {log_created} new)")

# ---------------------------------------------------------------
# STEP 3: Final summary
# ---------------------------------------------------------------
print("\n=== FINAL DATABASE SUMMARY ===")
print(f"Total Assets        : {Asset.objects.count()}")
print(f"Total Maint. Logs   : {MaintenanceLog.objects.count()}")
print(f"Total Users         : {User.objects.count()}")
print("\n--- ASSETS ---")
for a in Asset.objects.select_related('assigned_to').order_by('id'):
    print(f"  #{a.pk}: {a.name:30s} | {a.get_asset_type_display():10s} | ${a.cost:>10} | {a.assigned_to.username if a.assigned_to else 'Unassigned'}")

print("\n--- MAINTENANCE LOGS ---")
for m in MaintenanceLog.objects.select_related('asset').order_by('id'):
    print(f"  #{m.pk}: [{m.asset.name}] {m.service_date} | ${m.cost} | {m.description[:50]}")
